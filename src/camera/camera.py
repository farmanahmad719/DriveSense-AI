import cv2


class CameraManager:

    def __init__(self, source=0):
        self.source = source
        self.camera = None

        print("CameraManager initialized.")

    def open_camera(self):

        self.camera = cv2.VideoCapture(self.source)

        if not self.camera.isOpened():
            raise Exception("Unable to open webcam.")

        print("Webcam opened.")

    def read_frame(self):

        if self.camera is None:
            raise Exception("Camera is not opened.")

        ret, frame = self.camera.read()

        return ret, frame

    def release_camera(self):

        if self.camera is not None:
            self.camera.release()

        cv2.destroyAllWindows()

        print("Camera released.")