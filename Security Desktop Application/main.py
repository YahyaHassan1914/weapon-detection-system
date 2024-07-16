import os, sys, cv2, torch
import numpy as np
from ultralytics import YOLO
from ui_main import Ui_MainWindow
from ui_results_table import Ui_Form

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QDialog, QVBoxLayout, QTableWidget, QTableWidgetItem
from PySide6.QtCore import QThread, Signal, Slot, Qt
from PySide6.QtGui import QImage, QPixmap

class YOLOThread(QThread):
    # Define signals
    frame_processed = Signal(QImage, int, int)  # Signal emits QImage and int (number of targets)

    def __init__(self, video_source, range_threshold=50, parent=None):
        super().__init__(parent)

        self.video_source = video_source 
        self.range_threshold = range_threshold
        self.stopped = False

        # Initialize YOLO models
        self.weapons_pt = 'models\\weapons.pt'
        self.outfits_pt = 'models\\outfits.pt'
        self.yolo_weapons = YOLO(self.weapons_pt)
        self.yolo_outfits = YOLO(self.outfits_pt)
        # self.yolo_weapons.to('cuda')
        # self.yolo_outfits.to('cuda')
        print(f"Weapons model running on: {self.yolo_weapons.device}")
        print(f"Outfits model running on: {self.yolo_outfits.device}")

    def run(self):
        if self.video_source is None:
            print("No video source provided.")
            return

        # Open video source
        cap = cv2.VideoCapture(self.video_source)
        if not cap.isOpened():
            print("Error: Could not open video source.")
            return

        while not self.stopped:
            ret, frame = cap.read()
            if not ret:
                break

            # Run both models on the frame
            weapon_results = self.yolo_weapons(frame)[0]
            outfit_results = self.yolo_outfits(frame)[0]

            # Process results and draw bounding boxes
            self.process_results(frame, weapon_results, outfit_results)

            # Convert OpenCV frame to QImage
            rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = rgb_image.shape
            qimage = QImage(rgb_image.data, w, h, ch * w, QImage.Format_RGB888)

            # Emit processed frame and number of targets
            num_weapons = len(weapon_results.boxes)
            num_outfits = len(outfit_results.boxes)
            self.frame_processed.emit(qimage, num_weapons, num_outfits)

        # Release resources
        cap.release()

    def stop(self):
        self.stopped = True # Stops the execution of the thread

    def process_results(self, frame, weapon_results, outfit_results):
        # Processes the results of YOLO model inference for weapons and outfits.
        self.draw_boxes(frame, weapon_results, (0, 0, 255))
        self.draw_boxes(frame, outfit_results, (0, 255, 0))

    def draw_boxes(self, frame, results, color):
        boxes = []
        for result in results.boxes.data.tolist():
            x1, y1, x2, y2, score, class_id = result
            if score > 0.0:  # Threshold for displaying boxes, 0.5 is a good threashold
                boxes.append((x1, y1, x2, y2))
                # Draw bounding box
                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), color, 2)
                # Draw class label
                cv2.putText(frame, results.names[int(class_id)].upper(), (int(x1), int(y1 - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 1.3, color, 3, cv2.LINE_AA)
                # Draw confidence score
                cv2.putText(frame, f" {score:.2f}", (int(x1 + 110), int(y1 - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 1.0, (20, 50, 150), 2, cv2.LINE_AA)
        return boxes

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # init vars
        self.video_source = None
        self.thread = None

        # Store results for displaying in the table
        self.results = {"Guns": 0, "Police": 0}

        # browseVideos
        self.ui.pushButton_browse_media.clicked.connect(self.browse_videos)

        # Select source as webcam
        self.ui.pushButton_webcam.clicked.connect(self.select_webcam)

        # play and stop buttons
        self.ui.pushButton_play.clicked.connect(self.start_thread)
        self.ui.pushButton_stop.clicked.connect(self.stop_thread)

        # View Results
        self.ui.pushButton_results.clicked.connect(self.view_results)

    def browse_videos(self):
        options = QFileDialog.Options()
        video_file, _ = QFileDialog.getOpenFileName(self, "Select Video File", "", "Video Files (*.mp4 *.avi *.mkv);;Image Files (*.jpg *.png *.bmp)", options=options)
        if video_file:
            self.video_source = video_file

    def select_webcam(self):
        self.video_source = 0

    def update_results(self, class_name, count):
        if class_name in self.results:
            self.results[class_name] = max(self.results[class_name], count)
        else:
            self.results[class_name] = count

    def view_results(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Detection Results")

        ui_form = Ui_Form()
        ui_form.setupUi(dialog)

        # Set the number of rows based on the number of classes detected
        ui_form.results_table.setRowCount(len(self.results))
        ui_form.results_table.setColumnCount(2)
        ui_form.results_table.setHorizontalHeaderLabels(["Class Name", "Detection Number"])

        # Populate the table with results
        for row, (class_name, count) in enumerate(self.results.items()):
            ui_form.results_table.setItem(row, 0, QTableWidgetItem(class_name))
            ui_form.results_table.setItem(row, 1, QTableWidgetItem(str(count)))
        
        dialog.exec()

    def start_thread(self):
        self.stop_thread()

        # Reset results
        self.results = {"Guns": 0, "Police": 0}
        
        if self.thread is None:
            self.thread = YOLOThread(self.video_source)
            self.thread.frame_processed.connect(self.update_frame)  # Connect signal to slot
            self.thread.start()

    def stop_thread(self):

        if self.thread is not None:
            self.thread.stop()
            self.thread.wait()
            self.thread = None

    @Slot(QImage, int, int)
    def update_frame(self, qimage, num_weapons, num_outfits):
        pixmap = QPixmap.fromImage(qimage)
        
        # Get the size of the label
        label_size = self.ui.label_display.size()
        label_width = label_size.width()
        label_height = label_size.height()
        
        # Scale pixmap to fit label while maintaining aspect ratio
        scaled_pixmap = pixmap.scaled(label_width, label_height, Qt.KeepAspectRatio)
        self.ui.label_display.setPixmap(scaled_pixmap)

        # Update results for display in the table
        self.update_results("Guns", num_weapons)
        self.update_results("Police", num_outfits)

        # Update label_Targets with number of targets detected
        self.ui.label_targets_guns.setText(f"Guns detected: {num_weapons}")
        self.ui.label_targets_individual.setText(f"Police detected: {num_outfits}")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
