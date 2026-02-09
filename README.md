# Autonomous Drone AI – Face Tracking with DJI Tello

Real-time face tracking using a DJI Tello drone and OpenCV.  
The drone autonomously rotates and adjusts its distance to keep a detected face centered in view.

Built for the Warwick AI society **Autonomous Drone AI** track (2025/26).

---

## Demo

- Live video feed from the drone  
- Real-time face detection  
- Autonomous tracking and distance control  

---

## Tech Stack

- Python  
- OpenCV  
- NumPy  
- djitellopy (DJI Tello SDK)

---

## How It Works

1. The drone streams live video from its onboard camera  
2. Faces are detected using a Haar Cascade classifier  
3. The largest detected face is selected as the target  
4. A PID-style controller:
   - Rotates the drone to center the face
   - Moves forward/backward to maintain distance  
5. Control commands are sent continuously to the drone

---

## Setup

### Requirements
- DJI Tello drone  
- Python 3.8+  
- Wi-Fi connection to the drone  

### Install Dependencies
```bash
pip install opencv-python numpy djitellopy

## Safety

1. Ensure batteries are fully charged/close to fully charged to avoid the drone malfunctioning
2. Press q to land the drone


