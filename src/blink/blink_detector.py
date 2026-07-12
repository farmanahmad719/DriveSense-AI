class BlinkDetector:

    def __init__(
        self,
        ear_threshold=0.20,
        consecutive_frames=3,
    ):

        self.ear_threshold = ear_threshold
        self.consecutive_frames = consecutive_frames

        self.frame_counter = 0
        self.total_blinks = 0

        print("BlinkDetector initialized.")

    def update(self, ear):

        if ear < self.ear_threshold:

            self.frame_counter += 1

        else:

            if self.frame_counter >= self.consecutive_frames:

                self.total_blinks += 1

                self.frame_counter = 0

                return True

            self.frame_counter = 0

        return False