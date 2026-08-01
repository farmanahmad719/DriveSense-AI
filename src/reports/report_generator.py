import os

from datetime import datetime

import matplotlib.pyplot as plt

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.styles import ParagraphStyle

from reportlab.lib.enums import TA_CENTER

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    Image,
    PageBreak
)


class ReportGenerator:

    def __init__(self, reports_folder="reports"):

        self.reports_folder = reports_folder

        os.makedirs(
            self.reports_folder,
            exist_ok=True
        )

    # =========================================

    def calculate_metrics(self, history):

        if not history:

            return None

        # ---------------- TOTALS ----------------

        total_blinks = (
            history[-1].blink_count
        )

        total_yawns = (
            history[-1].yawn_count
        )

        # ---------------- FATIGUE ----------------

        fatigue_values = [

            result.fatigue_score

            for result in history
        ]

        average_fatigue = (

            sum(fatigue_values)

            / len(fatigue_values)
        )

        # ---------------- DROWSINESS EVENTS ----------------

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

        # ---------------- DISTRACTION EVENTS ----------------

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

        # ---------------- EAR ----------------

        ear_values = [

            result.ear

            for result in history
        ]

        average_ear = (

            sum(ear_values)

            / len(ear_values)
        )

        # ---------------- MAR ----------------

        mar_values = [

            result.mar

            for result in history
        ]

        average_mar = (

            sum(mar_values)

            / len(mar_values)
        )

        # ---------------- RISK ----------------

        if average_fatigue >= 60:

            risk = "HIGH"

        elif average_fatigue >= 30:

            risk = "MEDIUM"

        else:

            risk = "LOW"

        return {

            "total_blinks": total_blinks,

            "total_yawns": total_yawns,

            "average_fatigue": average_fatigue,

            "drowsiness_events":
                drowsiness_events,

            "distraction_events":
                distraction_events,

            "average_ear": average_ear,

            "average_mar": average_mar,

            "risk": risk
        }

    # =========================================

    def generate_pdf(self, history):

        metrics = self.calculate_metrics(
            history
        )

        if metrics is None:

            return None
        charts = self.create_charts(
            history
        )

        filename = (
            "session_report_"
            f"{datetime.now().strftime('%Y%m%d_%H%M%S')}"
            ".pdf"
        )
        filepath = os.path.join(

            self.reports_folder,

            filename
        )

        document = SimpleDocTemplate(

            filepath,

            pagesize=A4,

            rightMargin=40,

            leftMargin=40,

            topMargin=40,

            bottomMargin=40
        )

        styles = getSampleStyleSheet()

        title_style = ParagraphStyle(

            "ReportTitle",

            parent=styles["Title"],

            alignment=TA_CENTER,

            fontSize=22,

            spaceAfter=20
        )

        heading_style = ParagraphStyle(

            "ReportHeading",

            parent=styles["Heading2"],

            spaceBefore=15,

            spaceAfter=10
        )

        story = []

        # ---------------- TITLE ----------------

        story.append(

            Paragraph(

                "DriveSense AI",

                title_style
            )
        )

        story.append(

            Paragraph(

                "Driver Safety Session Report",

                styles["Heading2"]
            )
        )

        story.append(

            Spacer(
                1,
                15
            )
        )

        # ---------------- SESSION INFO ----------------

        story.append(

            Paragraph(

                "Session Information",

                heading_style
            )
        )

        session_data = [

            [

                "Generated",

                datetime.now().strftime(

                    "%Y-%m-%d %H:%M:%S"
                )
            ],

            [

                "Risk Level",

                metrics["risk"]
            ]
        ]

        session_table = Table(

            session_data,

            colWidths=[150, 300]
        )

        session_table.setStyle(

            TableStyle([

                (

                    "GRID",

                    (0, 0),

                    (-1, -1),

                    0.5,

                    colors.grey
                ),

                (

                    "BACKGROUND",

                    (0, 0),

                    (0, -1),

                    colors.lightgrey
                ),

                (

                    "PADDING",

                    (0, 0),

                    (-1, -1),

                    8
                )
            ])
        )

        story.append(
            session_table
        )

        # ---------------- METRICS ----------------

        story.append(

            Paragraph(

                "Session Metrics",

                heading_style
            )
        )

        metrics_data = [

            ["Metric", "Value"],

            [

                "Total Blinks",

                str(
                    metrics["total_blinks"]
                )
            ],

            [

                "Total Yawns",

                str(
                    metrics["total_yawns"]
                )
            ],

            [

                "Average Fatigue",

                f"{metrics[
                    'average_fatigue'
                ]:.1f}%"
            ],

            [

                "Drowsiness Events",

                str(
                    metrics[
                        "drowsiness_events"
                    ]
                )
            ],

            [

                "Distraction Events",

                str(
                    metrics[
                        "distraction_events"
                    ]
                )
            ],

            [

                "Average EAR",

                f"{metrics[
                    'average_ear'
                ]:.3f}"
            ],

            [

                "Average MAR",

                f"{metrics[
                    'average_mar'
                ]:.3f}"
            ]
        ]

        metrics_table = Table(

            metrics_data,

            colWidths=[250, 200]
        )

        metrics_table.setStyle(

            TableStyle([

                (

                    "GRID",

                    (0, 0),

                    (-1, -1),

                    0.5,

                    colors.grey
                ),

                (

                    "BACKGROUND",

                    (0, 0),

                    (-1, 0),

                    colors.darkblue
                ),

                (

                    "TEXTCOLOR",

                    (0, 0),

                    (-1, 0),

                    colors.white
                ),

                (

                    "PADDING",

                    (0, 0),

                    (-1, -1),

                    8
                )
            ])
        )

        story.append(

            metrics_table
        )
        # ================= CHARTS =================

        story.append(
            PageBreak()
        )

        story.append(

            Paragraph(
                "Session Analytics",
                heading_style
            )
        )

        for chart_path in charts:

            story.append(

                Image(
                    chart_path,
                    width=500,
                    height=250
                )
            )

            story.append(
                Spacer(
                    1,
                    20
                )
            )

        # ---------------- FOOTER ----------------

        story.append(

            Spacer(
                1,
                30
            )
        )

        story.append(

            Paragraph(

                "Generated by DriveSense AI",

                styles["Normal"]
            )
        )

        document.build(
            story
        )

        return filepath
    def create_charts(self, history):

        if not history:

            return []

        chart_folder = os.path.join(
            self.reports_folder,
            "temp_charts"
        )

        os.makedirs(
            chart_folder,
            exist_ok=True
        )

        x = list(
            range(
                len(history)
            )
        )

        attention = [

            max(
                0,
                min(
                    100,
                    100 - result.fatigue_score
                )
            )

            for result in history
        ]

        ear = [

            result.ear

            for result in history
        ]

        fatigue = [

            result.fatigue_score

            for result in history
        ]

        charts = []

        # ================= ATTENTION =================

        attention_path = os.path.join(
            chart_folder,
            "attention.png"
        )

        plt.figure(
            figsize=(8, 4)
        )

        plt.plot(
            x,
            attention,
            linewidth=2
        )

        plt.title(
            "Attention Trend"
        )

        plt.xlabel(
            "Time Sample"
        )

        plt.ylabel(
            "Attention (%)"
        )

        plt.ylim(
            0,
            100
        )

        plt.grid(
            True,
            alpha=0.3
        )

        plt.tight_layout()

        plt.savefig(
            attention_path,
            dpi=150
        )

        plt.close()

        charts.append(
            attention_path
        )

        # ================= EAR =================

        ear_path = os.path.join(
            chart_folder,
            "ear.png"
        )

        plt.figure(
            figsize=(8, 4)
        )

        plt.plot(
            x,
            ear,
            linewidth=2
        )

        plt.title(
            "Eye Aspect Ratio (EAR)"
        )

        plt.xlabel(
            "Time Sample"
        )

        plt.ylabel(
            "EAR"
        )

        plt.grid(
            True,
            alpha=0.3
        )

        plt.tight_layout()

        plt.savefig(
            ear_path,
            dpi=150
        )

        plt.close()

        charts.append(
            ear_path
        )

        # ================= FATIGUE =================

        fatigue_path = os.path.join(
            chart_folder,
            "fatigue.png"
        )

        plt.figure(
            figsize=(8, 4)
        )

        plt.plot(
            x,
            fatigue,
            linewidth=2
        )

        plt.title(
            "Fatigue Trend"
        )

        plt.xlabel(
            "Time Sample"
        )

        plt.ylabel(
            "Fatigue Score"
        )

        plt.ylim(
            0,
            100
        )

        plt.grid(
            True,
            alpha=0.3
        )

        plt.tight_layout()

        plt.savefig(
            fatigue_path,
            dpi=150
        )

        plt.close()

        charts.append(
            fatigue_path
        )

        return charts