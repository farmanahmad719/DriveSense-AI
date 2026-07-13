import config


class DrowsinessDetector:

    def __init__(self):

        self.ear_threshold = config.EAR_THRESHOLD
        self.consecutive_frames = config.DROWSINESS_FRAMES

        self.closed_eye_frames = 0
        self.is_drowsy = False

    def update(self, ear):

        if ear < self.ear_threshold:
            self.closed_eye_frames += 1
        else:
            self.closed_eye_frames = 0
            self.is_drowsy = False

        if self.closed_eye_frames >= self.consecutive_frames:
            self.is_drowsy = True

        return self.is_drowsy