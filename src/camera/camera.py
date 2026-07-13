import cv2
import config


class CameraManager:

    def __init__(self):
        self.cap = None

    def open_camera(self):
        self.cap = cv2.VideoCapture(config.CAMERA_INDEX)

        if not self.cap.isOpened():
            raise RuntimeError("Could not open camera.")

    def read_frame(self):
        return self.cap.read()

    def release_camera(self):
        if self.cap is not None:
            self.cap.release()