from datetime import datetime
import csv
import os


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

    def save_to_csv(self):

        os.makedirs("logs", exist_ok=True)

        filename = datetime.now().strftime(
            "logs/session_%Y-%m-%d_%H-%M-%S.csv"
        )

        with open(filename, "w", newline="") as file:

            writer = csv.writer(file)

            writer.writerow(
                [
                    "Time",
                    "Event",
                    "Details",
                ]
            )

            for log in self.logs:

                writer.writerow(
                    [
                        log["time"],
                        log["event"],
                        log["details"],
                    ]
                )

        print(f"\nSession saved to: {filename}")