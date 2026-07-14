import cv2


class CameraManager:

    def __init__(self):
        self.cap = None

    def open_camera(self, source=0):

        self.cap = cv2.VideoCapture(source)

        if not self.cap.isOpened():
            raise RuntimeError(f"Unable to open source: {source}")

        print("Input source opened.")

    def read_frame(self):
        return self.cap.read()

    def get_width(self):
        return int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))

    def get_height(self):
        return int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    def get_fps(self):

        fps = self.cap.get(cv2.CAP_PROP_FPS)

        if fps == 0:
            fps = 30

        return fps

    def release_camera(self):

        if self.cap:
            self.cap.release()