class FatigueScore:

    def __init__(self):
        self.score = 0

    def update(self, is_drowsy, total_yawns):

        score = 0

        if is_drowsy:
            score += 70

        score += min(total_yawns * 10, 30)

        self.score = score

        return self.score