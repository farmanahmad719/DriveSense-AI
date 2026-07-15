import customtkinter as ctk
from theme import *


class HelpPage(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(
            parent,
            fg_color="transparent"
        )

        self.grid_columnconfigure(0, weight=1)

        # ==========================================
        # About
        # ==========================================

        about = ctk.CTkFrame(
            self,
            fg_color=CARD,
            corner_radius=18
        )

        about.pack(
            fill="x",
            padx=10,
            pady=10
        )

        ctk.CTkLabel(
            about,
            text="ℹ About DriveSense AI",
            font=("Segoe UI",18,"bold")
        ).pack(
            anchor="w",
            padx=20,
            pady=(15,15)
        )

        ctk.CTkLabel(
            about,
            justify="left",
            wraplength=900,
            text=(
                "DriveSense AI is an intelligent Driver Monitoring System "
                "that detects driver fatigue, drowsiness, distraction, "
                "eye closure and yawning in real time using Computer Vision "
                "and Artificial Intelligence."
            )
        ).pack(
            anchor="w",
            padx=20,
            pady=(0,20)
        )

        # ==========================================
        # Features
        # ==========================================

        features = ctk.CTkFrame(
            self,
            fg_color=CARD,
            corner_radius=18
        )

        features.pack(
            fill="x",
            padx=10,
            pady=10
        )

        ctk.CTkLabel(
            features,
            text="🚀 Features",
            font=("Segoe UI",18,"bold")
        ).pack(
            anchor="w",
            padx=20,
            pady=(15,15)
        )

        feature_list = [
            "Real-time Face Detection",
            "Blink Detection",
            "Yawn Detection",
            "Head Pose Estimation",
            "Driver Distraction Detection",
            "Fatigue Score Calculation",
            "Live Dashboard",
            "Automatic Report Generation"
        ]

        for item in feature_list:

            ctk.CTkLabel(
                features,
                text=f"• {item}"
            ).pack(
                anchor="w",
                padx=25,
                pady=3
            )

        # ==========================================
        # Keyboard Shortcuts
        # ==========================================

        shortcuts = ctk.CTkFrame(
            self,
            fg_color=CARD,
            corner_radius=18
        )

        shortcuts.pack(
            fill="x",
            padx=10,
            pady=10
        )

        ctk.CTkLabel(
            shortcuts,
            text="⌨ Keyboard Shortcuts",
            font=("Segoe UI",18,"bold")
        ).pack(
            anchor="w",
            padx=20,
            pady=(15,15)
        )

        data = [
            ("Q", "Quit Application"),
            ("Generate Report", "Creates latest driving report"),
            ("Test Alarm", "Tests warning siren")
        ]

        for key, action in data:

            row = ctk.CTkFrame(
                shortcuts,
                fg_color="transparent"
            )

            row.pack(
                fill="x",
                padx=20,
                pady=5
            )

            ctk.CTkLabel(
                row,
                text=key,
                font=("Segoe UI",13,"bold")
            ).pack(side="left")

            ctk.CTkLabel(
                row,
                text=action
            ).pack(side="right")

        # ==========================================
        # Team
        # ==========================================

        team = ctk.CTkFrame(
            self,
            fg_color=CARD,
            corner_radius=18
        )

        team.pack(
            fill="x",
            padx=10,
            pady=10
        )

        ctk.CTkLabel(
            team,
            text="👨‍💻 Development Team",
            font=("Segoe UI",18,"bold")
        ).pack(
            anchor="w",
            padx=20,
            pady=(15,15)
        )

        ctk.CTkLabel(
            team,
            justify="left",
            text=(
                "DriveSense AI\n"
                "2026"
            )
        ).pack(
            anchor="w",
            padx=20,
            pady=(0,20)
        )