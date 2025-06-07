# Face Detection Project

This project implements real-time face detection using OpenCV and Haar Cascade Classifiers. It captures video from your webcam and detects faces in real-time, drawing rectangles around detected faces.

## Features

- Real-time face detection using webcam
- Uses OpenCV's Haar Cascade Classifier
- Visual feedback with rectangle overlays on detected faces
- Simple keyboard control (press 'q' to quit)

## Requirements

- Python 3.x
- OpenCV (cv2)
- Webcam

## Installation

1. Make sure you have Python installed on your system
2. Install the required package:
```bash
pip install opencv-python
```

## Usage

1. Navigate to the project directory
2. Run the face detection script:
```bash
python face_detection.py
```

3. A window will open showing the webcam feed with face detection
4. Press 'q' to quit the application

## How it Works

The program uses OpenCV's Haar Cascade Classifier, which is a machine learning-based approach where a cascade function is trained from many positive and negative images. The classifier is trained to detect faces in images and video streams.

The main components of the code:
- Uses the default Haar Cascade Classifier for frontal face detection
- Captures video from the default webcam (index 0)
- Processes each frame to detect faces
- Draws rectangles around detected faces
- Displays the processed video feed in real-time

## Notes

- The face detection accuracy may vary depending on lighting conditions and face orientation
- The program requires a working webcam
- Make sure you have sufficient lighting for better face detection results

## License

This project is open source and available under the MIT License. 