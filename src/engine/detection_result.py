from dataclasses import dataclass


@dataclass
class DetectionResult:

    frame: any

    face_detected: bool = False

    ear: float = 0.0

    mar: float = 0.0

    pitch: float = 0.0

    yaw: float = 0.0

    roll: float = 0.0

    direction: str = "FORWARD"

    blink_count: int = 0

    yawn_count: int = 0

    fatigue_score: int = 0

    is_drowsy: bool = False

    is_distracted: bool = False
    
    phone_detected: bool = False

    phone_confidence: float = 0.0

    phone_bbox: tuple = None
    
    ml_state: str = "UNKNOWN"

    ml_confidence: float = 0.0