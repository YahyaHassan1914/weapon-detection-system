# Python Security System

This repository implements a Python-based security system using OpenCV and a basic weapon detection model to record and save video. It features the following functionalities:

- Weapon Detection
- Video Storage (Google Cloud Object Storage)
- Text Notifications
- Arming & Disarming the System
- Activity Logs

## Installation

Before starting, ensure you have the following installed:

- Python 3.9+
- Node.js
- ffmpeg

To install the Python dependencies, run:
```bash
pip install -r requirements.txt
```
from the root directory.

Next, navigate to the frontend directory and install the necessary packages:
```bash
cd frontend && npm install
```

## Running the Backend

To run the backend, navigate to the backend directory and execute the `main.py` file:
```bash
cd backend && python main.py
```

## Running the Frontend

To run the frontend, execute the following command from the `frontend` directory:
```bash
npm start
```