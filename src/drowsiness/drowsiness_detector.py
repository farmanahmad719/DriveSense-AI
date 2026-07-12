class DrowsinessDetector:

    def __init__(
        self,
        ear_threshold=0.20,
        drowsy_frames=45,
    ):

        self.ear_threshold = ear_threshold
        self.drowsy_frames = drowsy_frames

        self.closed_eye_frames = 0
        self.is_drowsy = False

        print("DrowsinessDetector initialized.")

    def update(self, ear):

        if ear < self.ear_threshold:

            self.closed_eye_frames += 1

            if self.closed_eye_frames >= self.drowsy_frames:

                self.is_drowsy = True

        else:

            self.closed_eye_frames = 0
            self.is_drowsy = False

        return self.is_drowsy