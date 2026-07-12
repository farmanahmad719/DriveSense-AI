import time


class DistractionDetector:

    def __init__(self, threshold=2.0):

        self.threshold = threshold
        self.start_time = None
        self.is_distracted = False

    def update(self, direction):

        allowed_directions = ["LEFT", "RIGHT"]

        if direction == "FORWARD":

            self.start_time = None
            self.is_distracted = False

        elif direction in allowed_directions:

            if self.start_time is None:
                self.start_time = time.time()

            elapsed = time.time() - self.start_time

            if elapsed >= 3.0:
                self.is_distracted = True

        elif direction in ["DOWN", "UP"]:

            if self.start_time is None:
                self.start_time = time.time()

            elapsed = time.time() - self.start_time

            if elapsed >= 1.5:
                self.is_distracted = True

        return self.is_distracted