import csv
import os
from datetime import datetime


class FeatureCollector:

    def __init__(self, file_path="data/ml_features.csv"):

        self.file_path = file_path

        os.makedirs(
            os.path.dirname(self.file_path),
            exist_ok=True
        )

        self._create_file()

    # =======================================

    def _create_file(self):

        if not os.path.exists(self.file_path):

            with open(
                self.file_path,
                "w",
                newline=""
            ) as file:

                writer = csv.writer(file)

                writer.writerow([
                    "timestamp",
                    "ear",
                    "mar",
                    "pitch",
                    "yaw",
                    "roll",
                    "blink_count",
                    "yawn_count",
                    "phone_detected",
                    "is_drowsy",
                    "is_distracted",
                    "driver_state"
                ])

    # =======================================

    def collect(self, result):

        driver_state = self._get_driver_state(
            result
        )

        with open(
            self.file_path,
            "a",
            newline=""
        ) as file:

            writer = csv.writer(file)

            writer.writerow([

                datetime.now().isoformat(),

                result.ear,

                result.mar,

                result.pitch,

                result.yaw,

                result.roll,

                result.blink_count,

                result.yawn_count,

                int(result.phone_detected),

                int(result.is_drowsy),

                int(result.is_distracted),

                driver_state

            ])
    def _get_driver_state(self, result):

        if (
            result.phone_detected
            and result.is_drowsy
            and result.is_distracted
        ):

            return "HIGH_RISK"

        elif result.phone_detected:

            return "PHONE_USAGE"

        elif result.is_drowsy:

            return "DROWSY"

        elif result.is_distracted:

            return "DISTRACTED"

        else:

            return "SAFE"        