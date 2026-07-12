class YawnDetector:

    def __init__(
        self,
        mar_threshold=0.60,
        yawn_frames=15,
    ):

        self.mar_threshold = mar_threshold
        self.yawn_frames = yawn_frames

        self.open_mouth_frames = 0
        self.total_yawns = 0
        self.is_yawning = False

        print("YawnDetector initialized.")

    def update(self, mar):

        if mar > self.mar_threshold:

            self.open_mouth_frames += 1

            if (
                self.open_mouth_frames >= self.yawn_frames
                and not self.is_yawning
            ):
                self.total_yawns += 1
                self.is_yawning = True

        else:

            self.open_mouth_frames = 0
            self.is_yawning = False

        return self.is_yawning