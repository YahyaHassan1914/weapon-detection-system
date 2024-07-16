# Weapon Detection Desktop Application

This repo implements a weapon detection desktop application that uses PySide6 and YOLO models for detecting weapons and police outfits in video streams. It features the following:

- Real-time Weapon Detection
- Real-time Police Outfit Detection
- Video Source Selection (File/Webcam)
- Display of Detection Results in a Table
- User-Friendly GUI

## Installation

Before starting, make sure you have the following installed:

- Python 3.9+
- PySide6
- OpenCV
- ultralytics (YOLO)

Install the Python dependencies by running: `pip install -r requirements.txt` from the root directory.

## Running The Application

To run the application, execute the `main.py` file with the following command:

```
python main.py
```

## Features

### Weapon Detection

The application uses a YOLO model trained to detect weapons in real-time from video streams. Detected weapons are highlighted with bounding boxes and displayed on the interface.

### Police Outfit Detection

Similarly, the application uses another YOLO model to detect police outfits in real-time. Detected outfits are highlighted with bounding boxes and displayed on the interface.

### Video Source Selection

You can select the video source from which to perform detection:

- **File**: Choose a video file from your system.
- **Webcam**: Use your system's webcam for real-time detection.

### Display Detection Results

Detection results are displayed in a table showing the class name (e.g., Guns, Police) and the number of detections. The table updates dynamically as new classes appear in the detection.

## User Interface

The user interface is built using PySide6 and provides a user-friendly experience. It includes buttons to browse video files, start/stop detection, and view detection results in a table.

### Table Styling

The table displaying detection results is styled to match the overall theme of the application, ensuring a consistent and visually appealing look.

## Example Usage

1. Run the application:
    ```
    python main.py
    ```

2. Select a video source by clicking on "Browse" to choose a video file or "Webcam" to use your system's webcam.

3. Click "Start Detection" to start the detection process. The video stream will be displayed, and detected objects will be highlighted.

4. Click "Stop Detection" to stop the detection process.

5. Click "Results" to see the detection results in a table.

## Additional Information

For any questions or further information, feel free to reach out to the project maintainers. This application is a powerful tool for real-time weapon and police outfit detection, providing accurate and efficient results.