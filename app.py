from src.camera.camera import CameraManager
from src.detection.face_detector import FaceDetector
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

        cv2.imshow("DriveSense AI", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    camera.release_camera()


if __name__ == "__main__":
    main()