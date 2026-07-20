import customtkinter as ctk
from datetime import datetime
from theme import *
import os

class ReportsPage(ctk.CTkFrame):

    def __init__(self, parent, dashboard):

        super().__init__(
            parent,
            fg_color="transparent"
        )

        self.dashboard = dashboard

        self.grid_columnconfigure(
            0,
            weight=1
        )

        self.grid_rowconfigure(
            1,
            weight=1
        )

        # ================= TITLE =================

        ctk.CTkLabel(
            self,
            text="📄 Session Report",
            font=("Segoe UI", 26, "bold")
        ).grid(
            row=0,
            column=0,
            sticky="w",
            padx=20,
            pady=(10, 20)
        )

        # ================= REPORT CARD =================

        self.report_card = ctk.CTkFrame(
            self,
            fg_color=CARD,
            corner_radius=20
        )

        self.report_card.grid(
            row=1,
            column=0,
            sticky="nsew",
            padx=20,
            pady=(0, 20)
        )

        self.report_card.grid_columnconfigure(
            0,
            weight=1
        )

        self.report_card.grid_columnconfigure(
            1,
            weight=1
        )

        self.metric_labels = {}

        self.create_metric(
            "Total Blinks",
            "0",
            0,
            0
        )

        self.create_metric(
            "Total Yawns",
            "0",
            0,
            1
        )

        self.create_metric(
            "Average Fatigue",
            "0%",
            1,
            0
        )

        self.create_metric(
            "Drowsiness Events",
            "0",
            1,
            1
        )

        self.create_metric(
            "Distraction Events",
            "0",
            2,
            0
        )

        self.create_metric(
            "Average EAR",
            "0.00",
            2,
            1
        )

        self.create_metric(
            "Average MAR",
            "0.00",
            3,
            0
        )

        self.create_metric(
            "Risk Level",
            "LOW",
            3,
            1
        )

        # ================= BUTTON =================

        # ================= BUTTONS =================

        button_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        button_frame.grid(
            row=2,
            column=0,
            pady=(0, 20)
        )

        ctk.CTkButton(
            button_frame,
            text="🔄 Refresh Report",
            command=self.update_report
        ).pack(
            side="left",
            padx=10
        )

        ctk.CTkButton(
            button_frame,
            text="📄 Generate Report",
            command=self.generate_report
        ).pack(
            side="left",
            padx=10
        )
        self.auto_update()

    # =================================================

    def create_metric(
        self,
        name,
        value,
        row,
        column
    ):

        card = ctk.CTkFrame(
            self.report_card,
            fg_color="#222B3A",
            corner_radius=15
        )

        card.grid(
            row=row,
            column=column,
            sticky="nsew",
            padx=15,
            pady=15
        )

        ctk.CTkLabel(
            card,
            text=name,
            font=("Segoe UI", 13)
        ).pack(
            pady=(15, 5)
        )

        value_label = ctk.CTkLabel(
            card,
            text=value,
            font=("Segoe UI", 24, "bold")
        )

        value_label.pack(
            pady=(0, 15)
        )

        self.metric_labels[name] = value_label

    # =================================================

    def update_report(self):

        history = self.dashboard.session_history

        if not history:

            return

        # ---------------- BLINKS ----------------

        total_blinks = (
            history[-1].blink_count
        )

        self.metric_labels[
            "Total Blinks"
        ].configure(
            text=str(total_blinks)
        )

        # ---------------- YAWNS ----------------

        total_yawns = (
            history[-1].yawn_count
        )

        self.metric_labels[
            "Total Yawns"
        ].configure(
            text=str(total_yawns)
        )

        # ---------------- FATIGUE ----------------

        fatigue_values = [

            result.fatigue_score

            for result in history
        ]

        average_fatigue = sum(
            fatigue_values
        ) / len(
            fatigue_values
        )

        self.metric_labels[
            "Average Fatigue"
        ].configure(
            text=f"{average_fatigue:.1f}%"
        )

        # ---------------- DROWSINESS ----------------

        drowsiness_events = 0

        previous_drowsy = False

        for result in history:

            if (
                result.is_drowsy
                and not previous_drowsy
            ):

                drowsiness_events += 1

            previous_drowsy = (
                result.is_drowsy
            )

        self.metric_labels[
            "Drowsiness Events"
        ].configure(
            text=str(
                drowsiness_events
            )
        )

        # ---------------- DISTRACTION ----------------

        distraction_events = 0

        previous_distracted = False

        for result in history:

            if (
                result.is_distracted
                and not previous_distracted
            ):

                distraction_events += 1

            previous_distracted = (
                result.is_distracted
            )

        self.metric_labels[
            "Distraction Events"
        ].configure(
            text=str(
                distraction_events
            )
        )

        # ---------------- EAR ----------------

        ear_values = [

            result.ear

            for result in history
        ]

        average_ear = sum(
            ear_values
        ) / len(
            ear_values
        )

        self.metric_labels[
            "Average EAR"
        ].configure(
            text=f"{average_ear:.3f}"
        )

        # ---------------- MAR ----------------

        mar_values = [

            result.mar

            for result in history
        ]

        average_mar = sum(
            mar_values
        ) / len(
            mar_values
        )

        self.metric_labels[
            "Average MAR"
        ].configure(
            text=f"{average_mar:.3f}"
        )

        # ---------------- RISK ----------------

        if average_fatigue >= 60:

            risk = "HIGH"

        elif average_fatigue >= 30:

            risk = "MEDIUM"

        else:

            risk = "LOW"

        self.metric_labels[
            "Risk Level"
        ].configure(
            text=risk
        )
    def auto_update(self):

        self.update_report()

        self.after(
            1000,
            self.auto_update
        )    
    def generate_report(self):

        history = self.dashboard.session_history

        if not history:

            print(
                "⚠️ No session data available"
            )

            return

        # ---------------- METRICS ----------------

        total_blinks = (
            history[-1].blink_count
        )

        total_yawns = (
            history[-1].yawn_count
        )

        fatigue_values = [

            result.fatigue_score

            for result in history
        ]

        average_fatigue = sum(
            fatigue_values
        ) / len(
            fatigue_values
        )

        drowsiness_events = 0

        previous_drowsy = False

        for result in history:

            if (
                result.is_drowsy
                and not previous_drowsy
            ):

                drowsiness_events += 1

            previous_drowsy = (
                result.is_drowsy
            )

        distraction_events = 0

        previous_distracted = False

        for result in history:

            if (
                result.is_distracted
                and not previous_distracted
            ):

                distraction_events += 1

            previous_distracted = (
                result.is_distracted
            )

        ear_values = [

            result.ear

            for result in history
        ]

        average_ear = sum(
            ear_values
        ) / len(
            ear_values
        )

        mar_values = [

            result.mar

            for result in history
        ]

        average_mar = sum(
            mar_values
        ) / len(
            mar_values
        )

        # ---------------- RISK ----------------

        if average_fatigue >= 60:

            risk = "HIGH"

        elif average_fatigue >= 30:

            risk = "MEDIUM"

        else:

            risk = "LOW"

        # ---------------- REPORT TEXT ----------------

            report = f"""
        ========================================
                DRIVESENSE AI SESSION REPORT
        ========================================

        Generated:
        {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

        ----------------------------------------
        SESSION SUMMARY
        ----------------------------------------

        Total Blinks:
        {total_blinks}

        Total Yawns:
        {total_yawns}

        Average Fatigue:
        {average_fatigue:.1f}%

        Drowsiness Events:
        {drowsiness_events}

        Distraction Events:
        {distraction_events}

        Average EAR:
        {average_ear:.3f}

        Average MAR:
        {average_mar:.3f}

        Risk Level:
        {risk}

        ========================================
                END OF REPORT
        ========================================
        """

            # ---------------- SAVE REPORT ----------------

            filename = (
                f"session_report_"
                f"{datetime.now().strftime('%Y%m%d_%H%M%S')}"
                f".txt"
            )

          # ---------------- SAVE REPORT ----------------

            project_root = os.getcwd()

            reports_folder = os.path.join(
                project_root,
                "reports"
            )

            os.makedirs(
                reports_folder,
                exist_ok=True
            )

            filepath = os.path.join(
                reports_folder,
                filename
            )

            with open(
                filepath,
                "w",
                encoding="utf-8"
            ) as file:

                file.write(
                    report
                )

            print(
                f"✅ Report saved at:\n{filepath}"
            )    