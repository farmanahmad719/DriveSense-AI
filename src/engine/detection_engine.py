from src.camera.camera import CameraManager
from src.detection.face_detector import FaceDetector
from src.engine.detection_result import DetectionResult
from src.blink.blink_detector import BlinkDetector
from src.drowsiness.drowsiness_detector import DrowsinessDetector
from src.yawn.yawn_detector import YawnDetector
from src.scoring.fatigue_score import FatigueScore
from src.head_pose.head_pose_estimator import HeadPoseEstimator
from src.distraction.distraction_detector import DistractionDetector
from src.alerts.alarm import AlarmManager
from src.utils.eye_utils import (
    LEFT_EYE,
    RIGHT_EYE,
    get_eye_landmarks,
    get_mouth_landmarks,
    landmarks_to_pixels,
    calculate_ear,
    calculate_mar,
    draw_eye_points,
)


class DetectionEngine:

    def __init__(self):

        self.camera = CameraManager()
        self.face_detector = FaceDetector()
        self.blink_detector = BlinkDetector()
        self.drowsiness_detector = DrowsinessDetector()
        self.yawn_detector = YawnDetector()
        self.fatigue_score = FatigueScore()
        self.head_pose = HeadPoseEstimator()
        self.distraction_detector = DistractionDetector()
        self.alarm = AlarmManager()
    def start(self, source):

        self.camera.open_camera(source)

    def stop(self):

        self.alarm.stop_alarm()
        self.camera.release_camera()

    def get_width(self):

        return self.camera.get_width()

    def get_height(self):

        return self.camera.get_height()

    def get_fps(self):

        return self.camera.get_fps()

    def process_frame(self):
        print("process_frame() called")

        ret, frame = self.camera.read_frame()

        if not ret:
            return False, None

        result = DetectionResult(frame=frame)

        results = self.face_detector.detect_faces(frame)

        if not results.multi_face_landmarks:
            return True, result

        result.face_detected = True

        face_landmarks = results.multi_face_landmarks[0]

        left_eye_pixels, right_eye_pixels, mouth_pixels = self._extract_landmarks(
            face_landmarks,
            frame,
        )

        ear, mar = self._calculate_metrics(
            left_eye_pixels,
            right_eye_pixels,
            mouth_pixels,
        )

        result.ear = ear
        result.mar = mar
        print(f"EAR = {ear:.3f}   MAR = {mar:.3f}")

        # Blink Detection
        self.blink_detector.update(ear)
        print(
    "Blink Count:",
    self.blink_detector.total_blinks
)
        result.blink_count = self.blink_detector.total_blinks

        # Yawn Detection
        self.yawn_detector.update(mar)
        
        result.yawn_count = self.yawn_detector.total_yawns

        # Drowsiness
        result.is_drowsy = self.drowsiness_detector.update(ear)
        if result.is_drowsy:
            self.alarm.play_alarm()
        else:
            self.alarm.stop_alarm()
     

        # Fatigue Score
        result.fatigue_score = self.fatigue_score.update(
            result.is_drowsy,
            result.yawn_count,
        )

        # Head Pose
        pose = self.head_pose.estimate_pose(
            frame,
            face_landmarks,
        )

        if pose is not None:

            result.pitch, result.yaw, result.roll = pose

            result.direction = self.get_head_direction(
                result.pitch,
                result.yaw,
            )
            print(
            f"Pitch={result.pitch:.1f}, "
            f"Yaw={result.yaw:.1f}, "
            f"Direction={result.direction}"
        )

        else:

            result.pitch = 0.0
            result.yaw = 0.0
            result.roll = 0.0
            result.direction = "FORWARD"

        # Distraction
        result.is_distracted = self.distraction_detector.update(
            result.direction
        )

        # Draw Eye Points
        frame = draw_eye_points(frame, left_eye_pixels)
        frame = draw_eye_points(frame, right_eye_pixels)
        frame = draw_eye_points(frame, mouth_pixels)

        # Draw Face Mesh
        frame = self.draw_landmarks(
            frame,
            results,
        )

        result.frame = frame
        print(
        f"Blink={result.blink_count}, "
        f"Yawn={result.yawn_count}, "
        f"Drowsy={result.is_drowsy}, "
        f"Direction={result.direction}, "
        f"Fatigue={result.fatigue_score}"
    )

        return True, result


    def draw_landmarks(self, frame, results):

        return self.face_detector.draw_landmarks(frame, results)
    
    def get_head_direction(self, pitch, yaw):

        YAW_THRESHOLD = 25
        PITCH_THRESHOLD = 20

        if yaw <= -YAW_THRESHOLD:
            return "LEFT"

        elif yaw >= YAW_THRESHOLD:
            return "RIGHT"

        elif pitch <= -PITCH_THRESHOLD:
            return "UP"

        elif pitch >= PITCH_THRESHOLD:
            return "DOWN"

        return "FORWARD"

    def _extract_landmarks(self, face_landmarks, frame):

        h, w, _ = frame.shape

        left_eye = get_eye_landmarks(face_landmarks, LEFT_EYE)
        right_eye = get_eye_landmarks(face_landmarks, RIGHT_EYE)
        mouth = get_mouth_landmarks(face_landmarks)

        left_eye_pixels = landmarks_to_pixels(left_eye, w, h)
        right_eye_pixels = landmarks_to_pixels(right_eye, w, h)
        mouth_pixels = landmarks_to_pixels(mouth, w, h)

        return (
            left_eye_pixels,
            right_eye_pixels,
            mouth_pixels,
        )
    def _calculate_metrics(
            self,
            left_eye_pixels,
            right_eye_pixels,
            mouth_pixels,
    ):

        left_ear = calculate_ear(left_eye_pixels)
        right_ear = calculate_ear(right_eye_pixels)

        ear = (left_ear + right_ear) / 2
        mar = calculate_mar(mouth_pixels)

        return ear, mar