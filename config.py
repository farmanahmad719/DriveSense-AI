# COLOR SCHEME

COLORS = {
    # Primary colors
    "green": "#00b894",
    "yellow": "#fdcb6e",
    "pink": "#fd79a8",
    "blue": "#0984e3",
    "purple": "#6c5ce7",
    "red": "#e17055",
    
    # UI colors
    "gray": "#888",
    "gray_light": "#aaa",
    "gray_dark": "#555",
    "bg": "#0d0e1a",
    "card": "#151625",
    "sidebar": "#1a1b2e",
    "border": "#2a2d3e",
    "text": "#ffffff",
    "text_dim": "#666",
}

# ============================================
# WINDOW SETTINGS
# ============================================
WINDOW_WIDTH = 1500
WINDOW_HEIGHT = 900
MIN_WIDTH = 1300
MIN_HEIGHT = 800


# ============================================
# GAUGE SETTINGS
# ============================================
GAUGE_SIZE = 180
GAUGE_RADIUS = 75
GAUGE_MIN = 0
GAUGE_MAX = 100


HEAD_POSE_THRESHOLD = 30    # Degrees - above this = looking away
PHONE_CONFIDENCE = 0.5      # YOLO confidence threshold for phone detection

# ============================================
# ATTENTION SCORE SETTINGS
# ============================================
ATTENTION_START = 100
ATTENTION_DECREMENT = 2     # Points to subtract per violation frame
ATTENTION_INCREMENT = 1     # Points to add per normal frame
ATTENTION_WARNING = 60      # Below this = warning level
ATTENTION_DANGER = 40       # Below this = danger level

# ============================================
# DROWSINESS LEVELS
# ============================================
DROWSINESS_GOOD = 30        # Below 30% = Good
DROWSINESS_MODERATE = 60    # 30-60% = Moderate
DROWSINESS_BAD = 80         # Above 60% = Bad

# ============================================
# FPS & PERFORMANCE
# ============================================
TARGET_FPS = 30
CAMERA_UPDATE_MS = 33       # ~30 FPS (1000/30)
STATUS_UPDATE_MS = 5000     # Update status cards every 5 seconds
GAUGE_UPDATE_MS = 3000      # Update gauges every 3 seconds

# ============================================
# PATHS
# ============================================
import os

# Base directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Model paths
YOLO_MODEL_PATH = os.path.join(BASE_DIR, "assets", "models", "yolov8n.pt")


# Database & Logs
DB_PATH = os.path.join(BASE_DIR, "data", "driver_history.db")
LOG_PATH = os.path.join(BASE_DIR, "logs", "events.log")

# ============================================
# CAMERA SETTINGS
# ============================================

CAMERA_WIDTH = 640
CAMERA_HEIGHT = 480

# ============================================
# ALERT SETTINGS
# ============================================
ALERT_DURATION = 3000       # Alert duration in milliseconds
SIREN_VOLUME = 0.7          # 0.0 to 1.0

# ============================================
# DATABASE SETTINGS
# ============================================
DB_TABLES = {
    "sessions": """
        CREATE TABLE IF NOT EXISTS sessions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            session_id TEXT NOT NULL,
            start_time TEXT NOT NULL,
            end_time TEXT,
            duration INTEGER,
            driver_name TEXT
        )
    """,
    "events": """
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            session_id TEXT NOT NULL,
            timestamp TEXT NOT NULL,
            event_type TEXT NOT NULL,
            severity TEXT NOT NULL,
            duration INTEGER,
            details TEXT
        )
    """
}

CAMERA_INDEX = 0

EAR_THRESHOLD = 0.25

DROWSINESS_FRAMES = 20

MAR_THRESHOLD = 0.70

DISTRACTION_LEFT_RIGHT_TIME = 3.0

DISTRACTION_UP_DOWN_TIME = 1.5

ALARM_FILE = "assets/alarm.wav"

WINDOW_NAME = "DriveSense AI"

SHOW_FPS = True

SHOW_LANDMARKS = True
INPUT_SOURCE = "camera"

VIDEO_PATH = "videos/demo.mp4"