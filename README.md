🚗 DriveSense AI

An AI-powered real-time Driver Monitoring System that detects drowsiness, yawning, distraction, and unsafe driver behaviour using computer vision.

📌 Overview

DriveSense AI is a real-time driver monitoring application designed to improve road safety by continuously analysing the driver's face and behaviour through a webcam or recorded video.

The system uses OpenCV for video processing and MediaPipe Face Mesh for facial landmark detection. These landmarks are used to calculate important driver-monitoring features such as the Eye Aspect Ratio (EAR), Mouth Aspect Ratio (MAR), and head orientation.

When unsafe behaviour is detected, the system updates the dashboard, generates alerts, triggers an audio warning, and records session information for analysis and reporting.

✨ Key Features
👁️ Real-time face and facial landmark detection
😴 Driver drowsiness detection
👀 Eye blink detection and blink counting
🥱 Yawn detection and yawn counting
🧭 Head-pose-based distraction detection
📊 Real-time attention score
📈 Fatigue monitoring
🔊 Audio alarm for critical events
🚨 Alert history with severity levels
📉 Real-time analytics and monitoring dashboard
📄 Session report generation
🎥 Support for live camera and recorded video input
🧠 How It Works
Camera / Recorded Video
            │
            ▼
        OpenCV
            │
            ▼
MediaPipe Face Mesh
            │
            ▼
Facial Landmarks
            │
            ▼
Feature Extraction
(EAR, MAR, Head Pose)
            │
            ▼
Detection Engine
            │
            ▼
Driver Monitoring Result
            │
     ┌──────┼──────┐
     ▼      ▼      ▼
Dashboard  Alerts  Reports
🔍 Detection Modules
👁️ Blink Detection

DriveSense AI calculates the Eye Aspect Ratio (EAR) using eye landmarks.

EAR decreases when the eyes close and increases when the eyes open. This helps the system detect eye blinks and monitor prolonged eye closure.

😴 Drowsiness Detection

The system monitors the EAR value over consecutive video frames.

If the driver's eyes remain closed below the configured EAR threshold for a specified number of frames, the driver is classified as drowsy.

When drowsiness is detected:

The driver status is updated
A warning is displayed on the dashboard
An audio alarm is triggered
A critical alert is recorded
🥱 Yawn Detection

The system calculates the Mouth Aspect Ratio (MAR) using facial mouth landmarks.

When the mouth opening exceeds the configured threshold, a yawn is detected and the yawn count is updated.

🧭 Distraction Detection

DriveSense AI uses facial landmarks and head-pose estimation to determine whether the driver is looking away from the road.

If the driver's head remains turned away for longer than the configured duration, the system generates a distraction warning.

📊 Attention Score

The attention score represents the driver's current attentiveness.

The score starts at 100
Unsafe behaviour decreases the score
Normal behaviour gradually restores the score
Warning and danger levels are displayed on the dashboard
📈 Fatigue Score

The fatigue score provides an estimate of the driver's fatigue level using detected indicators such as:

Drowsiness
Yawning

The score is displayed on the dashboard to help monitor the driver's condition during a session.

🚨 Alert System

Important safety events are stored with:

Time
Severity
Alert message
Screenshot information, when available

Alert severity levels:

Level	Meaning
🟢 INFO	General system information
🟠 WARNING	Potentially unsafe behaviour
🔴 CRITICAL	High-risk driver condition

Users can also:

View alert history
Clear alerts
Export alert logs
📄 Session Reports

The report page provides a summary of the monitoring session, including:

Total blink count
Total yawn count
Average fatigue score
Drowsiness events
Distraction events
Average EAR
Average MAR
Overall risk level
🖥️ Dashboard

The application provides an interactive desktop dashboard with pages for:

🏠 Dashboard
🎥 Live Monitoring
📊 Analytics
🚨 Alerts
📄 Reports
⚙️ Settings
❓ Help
🛠️ Technology Stack
Technology	Purpose
Python	Main programming language
OpenCV	Camera handling and video-frame processing
MediaPipe Face Mesh	Facial landmark detection
NumPy	Numerical calculations
CustomTkinter	Desktop dashboard user interface
Matplotlib	Graphs and analytics
Pygame	Audio alarm system
Pandas	Data handling and logging
ReportLab	Session report generation
📂 Project Structure
DriveSense-AI/
│
├── app.py
├── dashboard_app.py
├── config.py
├── requirements.txt
├── README.md
│
├── src/
│   ├── engine/
│   │   ├── detection_engine.py
│   │   └── detection_result.py
│   │
│   ├── camera/
│   │   └── camera_manager.py
│   │
│   ├── detectors/
│   │   ├── face_detector.py
│   │   ├── blink_detector.py
│   │   ├── drowsiness_detector.py
│   │   ├── yawn_detector.py
│   │   └── distraction_detector.py
│   │
│   ├── alerts/
│   │   └── alert_system.py
│   │
│   ├── reports/
│   │   └── report_generator.py
│   │
│   ├── pages/
│   │   ├── dashboard_page.py
│   │   ├── live_monitoring_page.py
│   │   ├── analytics_page.py
│   │   ├── alerts_page.py
│   │   ├── reports_page.py
│   │   ├── settings_page.py
│   │   └── help_page.py
│   │
│   └── components/
│
├── assets/
│   └── alarm.wav
│
├── alerts/
├── reports/
├── outputs/
└── logs/

Update the file names above if your actual folder structure is different.

⚙️ Installation
1. Clone the repository
git clone YOUR_REPOSITORY_URL
2. Open the project folder
cd DriveSense-AI
3. Create a virtual environment
python -m venv venv
4. Activate the virtual environment

Windows:

venv\Scripts\activate
5. Install dependencies
pip install -r requirements.txt
▶️ Run the Project

To start the dashboard:

python dashboard_app.py

If your project starts from app.py, use:

python app.py
⚠️ Current Limitations

The current prototype may be affected by:

Low-light conditions
Face occlusion
Extreme head rotation
Camera position and angle
Glasses or facial accessories
Limited system hardware

This project is an academic prototype and is not a replacement for certified vehicle safety systems.

🚀 Future Improvements
Night-time monitoring using infrared cameras
Improved detection under low-light conditions
Mobile application integration
Cloud-based monitoring
GPS-based safety tracking
Driver identification
Vehicle-system integration
Embedded-device deployment
Improved model optimisation
Testing with larger and more diverse datasets
👥 Team Contributions
Team Member	Contribution
## 👥 Team Contributions

| Team Member | Contribution |
|---|---|
| **FARMAN AHMAD** | Backend development, computer vision modules, detection logic, alerts, reports, and backend–frontend integration |
| **Abida Kulsoom** | Dashboard UI, frontend components, visual design, and interface development |
🎓 Project Information

Developed as an AI/ML Club Internship Project.

🙏 Acknowledgements
OpenCV
MediaPipe
CustomTkinter
Matplotlib
<div align="center">
🚗 DriveSense AI
Monitor • Detect • Alert • Improve Road Safety
</div>w
