import cv2
import time

from src.camera.camera import CameraManager
from src.detection.face_detector import FaceDetector
from src.blink.blink_detector import BlinkDetector
from src.drowsiness.drowsiness_detector import DrowsinessDetector
from src.alerts.alarm import AlarmManager

from src.utils.eye_utils import (
    LEFT_EYE,
    RIGHT_EYE,
    get_eye_landmarks,
    landmarks_to_pixels,
    draw_eye_points,
    calculate_ear,
)


def main():

    camera = CameraManager()
    detector = FaceDetector()
    blink_detector = BlinkDetector()
    drowsiness_detector = DrowsinessDetector()
    alarm = AlarmManager()

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

            left_eye_pixels = landmarks_to_pixels(left_eye, w, h)
            right_eye_pixels = landmarks_to_pixels(right_eye, w, h)

            left_ear = calculate_ear(left_eye_pixels)
            right_ear = calculate_ear(right_eye_pixels)

            ear = (left_ear + right_ear) / 2

            blink_detector.update(ear)

            is_drowsy = drowsiness_detector.update(ear)

            if is_drowsy:
                alarm.play_alarm()
            else:
                alarm.stop_alarm()

            frame = draw_eye_points(frame, left_eye_pixels)
            frame = draw_eye_points(frame, right_eye_pixels)
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

        cv2.imshow("DriveSense AI", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    alarm.stop_alarm()
    camera.release_camera()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()