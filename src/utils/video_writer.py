import cv2
import os
from datetime import datetime


class VideoWriterManager:

    def __init__(self):

        os.makedirs("outputs", exist_ok=True)

        filename = datetime.now().strftime("session_%Y%m%d_%H%M%S.mp4")

        self.output_path = os.path.join("outputs", filename)

        self.writer = None

    def initialize(self, width, height, fps):

        print("initialize() called")

        if fps <= 0:
            fps = 30

        fourcc = cv2.VideoWriter_fourcc(*"mp4v")

        self.writer = cv2.VideoWriter(
            self.output_path,
            fourcc,
            fps,
            (width, height),
        )

        print("Writer opened:", self.writer.isOpened())

    def write(self, frame):

        if self.writer is not None:
            self.writer.write(frame)

    def release(self):

        if self.writer is not None:
            self.writer.release()

        print(f"\nOutput video saved to:\n{self.output_path}")