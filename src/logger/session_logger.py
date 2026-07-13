from datetime import datetime


class SessionLogger:

    def __init__(self):
        self.logs = []

    def log(self, event, details=""):

        timestamp = datetime.now().strftime("%H:%M:%S")

        self.logs.append(
            {
                "time": timestamp,
                "event": event,
                "details": details,
            }
        )

    def get_logs(self):
        return self.logs