from datetime import datetime
import os


class ReportGenerator:

    def __init__(self):

        self.start_time = datetime.now()

    def generate_report(
        self,
        total_blinks,
        total_yawns,
        fatigue_score,
        drowsiness_events,
        distraction_events,
        average_ear,
        average_mar,
    ):

        end_time = datetime.now()

        duration = end_time - self.start_time

        os.makedirs("reports", exist_ok=True)

        filename = end_time.strftime(
            "reports/report_%Y-%m-%d_%H-%M-%S.txt"
        )

        if fatigue_score < 30:
            driver_status = "SAFE"

        elif fatigue_score < 60:
            driver_status = "WARNING"

        else:
            driver_status = "HIGH RISK"

        with open(filename, "w") as file:

            file.write("=" * 50 + "\n")
            file.write("        DriveSense AI Driver Report\n")
            file.write("=" * 50 + "\n\n")

            file.write(f"Date               : {end_time.strftime('%d-%m-%Y')}\n")
            file.write(f"Time               : {end_time.strftime('%H:%M:%S')}\n")
            file.write(f"Session Duration   : {duration}\n\n")

            file.write("-" * 50 + "\n")
            file.write("Blink Statistics\n")
            file.write("-" * 50 + "\n")
            file.write(f"Total Blinks       : {total_blinks}\n\n")

            file.write("-" * 50 + "\n")
            file.write("Yawn Statistics\n")
            file.write("-" * 50 + "\n")
            file.write(f"Total Yawns        : {total_yawns}\n\n")

            file.write("-" * 50 + "\n")
            file.write("Driver Behaviour\n")
            file.write("-" * 50 + "\n")

            file.write(f"Drowsiness Events  : {drowsiness_events}\n")
            file.write(f"Distraction Events : {distraction_events}\n")
            file.write(f"Fatigue Score      : {fatigue_score}\n")
            file.write(f"Average EAR        : {average_ear:.3f}\n")
            file.write(f"Average MAR        : {average_mar:.3f}\n\n")

            file.write("-" * 50 + "\n")
            file.write("Overall Result\n")
            file.write("-" * 50 + "\n")
            file.write(f"Driver Condition   : {driver_status}\n")

        print(f"\nReport saved to: {filename}")