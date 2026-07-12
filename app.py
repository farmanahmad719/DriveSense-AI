import cv2
import time

from matplotlib.pylab import roll

from src.camera.camera import CameraManager
from src.detection.face_detector import FaceDetector
from src.blink.blink_detector import BlinkDetector
from src.drowsiness.drowsiness_detector import DrowsinessDetector
from src.alerts.alarm import AlarmManager
from src.yawn.yawn_detector import YawnDetector
from src.scoring.fatigue_score import FatigueScore
from src.head_pose.head_pose_estimator import HeadPoseEstimator
from src.utils.eye_utils import (
    LEFT_EYE,
    RIGHT_EYE,
    MOUTH,
    get_eye_landmarks,
    get_mouth_landmarks,
    landmarks_to_pixels,
    draw_eye_points,
    calculate_ear,
    calculate_mar,
)

def main():

    camera = CameraManager()
    detector = FaceDetector()
    blink_detector = BlinkDetector()
    drowsiness_detector = DrowsinessDetector()
    alarm = AlarmManager()
    yawn_detector = YawnDetector()
    fatigue_score = FatigueScore()
    head_pose_estimator = HeadPoseEstimator()
    camera.open_camera()

    previous_time = time.time()

    ear = 0
    is_drowsy = False

    while True:

        ret, frame = camera.read_frame()

        if not ret:
            print("Failed to read frame.")
            break

        results = detector.detect_faces(frame)

        if results.multi_face_landmarks:

            face_landmarks = results.multi_face_landmarks[0]

            h, w, _ = frame.shape

            left_eye = get_eye_landmarks(face_landmarks, LEFT_EYE)
            right_eye = get_eye_landmarks(face_landmarks, RIGHT_EYE)
            mouth = get_mouth_landmarks(face_landmarks)

            left_eye_pixels = landmarks_to_pixels(left_eye, w, h)
            right_eye_pixels = landmarks_to_pixels(right_eye, w, h)
            mouth_pixels = landmarks_to_pixels(mouth, w, h)

            left_ear = calculate_ear(left_eye_pixels)
            right_ear = calculate_ear(right_eye_pixels)
            mar = calculate_mar(mouth_pixels)

            ear = (left_ear + right_ear) / 2
            pose = head_pose_estimator.estimate_pose(frame, face_landmarks)

            if pose is not None:
               pitch, yaw, roll = pose
            else:
                pitch, yaw, roll = 0.0, 0.0, 0.0
            direction = "FORWARD"

            if yaw < -15:
                direction = "LEFT"

            elif yaw > 15:
                direction = "RIGHT"

            elif pitch < -15:
                direction = "UP"

            elif pitch > 15:
                direction = "DOWN"

            blink_detector.update(ear)

            is_drowsy = drowsiness_detector.update(ear)

            is_yawning = yawn_detector.update(mar)
            score = fatigue_score.update(
                is_drowsy,
                yawn_detector.total_yawns
        )       

            if is_drowsy:
                alarm.play_alarm()
            else:
                alarm.stop_alarm()

            frame = draw_eye_points(frame, left_eye_pixels)
            frame = draw_eye_points(frame, right_eye_pixels)
            frame = draw_eye_points(frame, mouth_pixels)
            frame = detector.draw_landmarks(frame, results)

        else:

            alarm.stop_alarm()
            is_drowsy = False

        current_time = time.time()

        fps = 1 / (current_time - previous_time)

        previous_time = current_time

        cv2.putText(
            frame,
            f"FPS: {int(fps)}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2,
        )

        cv2.putText(
            frame,
            f"EAR: {ear:.2f}",
            (20, 80),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255, 255, 0),
            2,
        )
        cv2.putText(
            frame,
            f"MAR: {mar:.2f}",
            (20, 200),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255, 255, 0),
             2,
        )
             

        cv2.putText(
            frame,
            f"Blinks: {blink_detector.total_blinks}",
            (20, 120),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            2,
        )

        status = "DROWSY" if is_drowsy else "ALERT"

        color = (0, 0, 255) if is_drowsy else (0, 255, 0)

        cv2.putText(
            frame,
            f"Status: {status}",
            (20, 160),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            color,
            2,
        )
        cv2.putText(
            frame,
            f"Yawns: {yawn_detector.total_yawns}",
            (20, 240),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255, 0, 255),
            2,
        )
        cv2.putText(
            frame,
            f"Fatigue Score: {score}",
            (20, 280),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 165, 255),
            2,
        )
        cv2.putText(
            frame,
            f"Pitch: {pitch:.1f}",
            (20, 320),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (255, 255, 255),
            2,
        )

        cv2.putText(
            frame,
            f"Yaw: {yaw:.1f}",
            (20, 360),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (255, 255, 255),
            2,
        )

        cv2.putText(
            frame,
            f"Roll: {roll:.1f}",
            (20, 400),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (255, 255, 255),
            2,
        )
        cv2.putText(
            frame,
            f"Head: {direction}",
            (20, 440),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 255),
            2,
        )

        cv2.imshow("DriveSense AI", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    alarm.stop_alarm()
    camera.release_camera()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
    