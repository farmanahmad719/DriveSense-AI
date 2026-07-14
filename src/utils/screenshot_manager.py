import cv2
import os
from datetime import datetime


class ScreenshotManager:

    def __init__(self):

        os.makedirs("alerts", exist_ok=True)

    def save(self, frame, event):

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        filename = f"{event}_{timestamp}.png"

        path = os.path.join("alerts", filename)

        cv2.imwrite(path, frame)

        print(f"Screenshot saved: {path}")