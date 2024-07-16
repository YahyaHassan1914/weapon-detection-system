import cv2 as cv
import numpy as np
import threading
import datetime
from storage import handle_detection
from ultralytics import YOLO


class Camera:
    out = None

    def __init__(self):
        self.armed = False
        self.camera_thread = None
    
    def arm(self):
        if not self.armed and not self.camera_thread:
            self.camera_thread = threading.Thread(target=self.run)
        
        self.camera_thread.start()
        self.armed = True
        print("Camera armed.")

    def disarm(self):
        self.armed = False
        self.camera_thread = None
        print("Camera disarmed.")

    def run(self):
            weapon_detected = False
            non_detected_counter = 0
            current_recording_name = None

            # Load the YOLO model
            pt_file = 'models/weapons.pt'
            model = YOLO(pt_file)

            self.cap = cv.VideoCapture(0)
            print("Camera started...")

            while self.armed:
                ret, frame = self.cap.read()
                if not ret:
                    break

                # Process the frame using the YOLO model
                results = model(frame)[0]

                threshold = 0.5 # Threshold for displaying boxes, 0.5 is a good threashold
                weapon_detected = False
                for result in results.boxes.data.tolist():
                    x1, y1, x2, y2, score, class_id = result

                    if score > threshold:
                        # Assuming class_id of the weapon is known and is 0, otherwise adjust accordingly
                        if int(class_id) == 0:
                            cv.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 0, 255), 2)
                            cv.putText(frame, results.names[int(class_id)].upper(), (int(x1), int(y1 - 10)),
                                    cv.FONT_HERSHEY_SIMPLEX, 1.3, (0, 0, 255), 3, cv.LINE_AA)
                            weapon_detected = True

                # If a weapon is detected, start/continue recording
                if weapon_detected:
                    non_detected_counter = 0  # reset the counter
                    if self.out is None:  # if VideoWriter isn't initialized, initialize it
                        now = datetime.datetime.now()
                        formatted_now = now.strftime("%d-%m-%y-%H-%M-%S")
                        print("Weapon detected at", formatted_now)
                        current_recording_name = f'{formatted_now}.mp4'
                        fourcc = cv.VideoWriter_fourcc(*'mp4v')  # or use 'XVID'
                        self.out = cv.VideoWriter(current_recording_name, fourcc, 20.0, (frame.shape[1], frame.shape[0]))

                    # Write the frame into the file
                    self.out.write(frame)

                # If no weapon is detected, stop recording after 50 frames
                else:
                    non_detected_counter += 1  # increment the counter
                    if non_detected_counter >= 50:  # if 50 frames have passed without a detection
                        if self.out is not None:  # if VideoWriter is initialized, release it
                            self.out.release()
                            self.out = None  # set it back to None
                            handle_detection(current_recording_name)
                            current_recording_name = None

            self.cap.release()
            print("Camera released...")

    def __del__(self):
        self.cap.release()
        if self.out is not None:
            self.out.release()