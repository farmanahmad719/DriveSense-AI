from src.camera.camera import CameraManager
from src.detection.face_detector import FaceDetector
from src.utils.eye_utils import (
    LEFT_EYE,
    RIGHT_EYE,
    get_eye_landmarks,
    landmarks_to_pixels,
    draw_eye_points,
    calculate_ear,
)
import cv2
import time

def main():
    """
    Main entry point for the DriveSense AI application.
    """

    camera = CameraManager()

    camera.open_camera()
    detector = FaceDetector()
    
    previous_time = time.time()

    while True:

        ret, frame = camera.read_frame()
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

          frame = draw_eye_points(frame, left_eye_pixels)
          frame = draw_eye_points(frame, right_eye_pixels)
          frame = detector.draw_landmarks(frame, results)
       
        current_time = time.time()
        fps = 1 / (current_time - previous_time)
        previous_time = current_time

        if not ret:
            print(" Failed to read frame.")
            break
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
        cv2.imshow("DriveSense AI", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    camera.release_camera()


if __name__ == "__main__":
    main()  