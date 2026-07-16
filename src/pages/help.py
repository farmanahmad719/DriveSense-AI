import customtkinter as ctk

from theme import *


class HelpPage(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(
            parent,
            fg_color="transparent"
        )

        # ====================================================
        # SCROLLABLE CONTENT
        # ====================================================

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        scroll = ctk.CTkScrollableFrame(
            self,
            fg_color="transparent"
        )

        scroll.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        scroll.grid_columnconfigure(0, weight=1)
        scroll.grid_columnconfigure(1, weight=1)

        # ====================================================
        # PAGE HEADER
        # ====================================================

        header = ctk.CTkFrame(
            scroll,
            fg_color=CARD,
            corner_radius=18
        )

        header.grid(
            row=0,
            column=0,
            columnspan=2,
            sticky="ew",
            padx=10,
            pady=(10, 15)
        )

        ctk.CTkLabel(
            header,
            text="❓ Help & Documentation",
            font=("Segoe UI", 22, "bold")
        ).pack(
            anchor="w",
            padx=20,
            pady=(18, 5)
        )

        ctk.CTkLabel(
            header,
            text="Learn more about DriveSense AI and how to use the system.",
            text_color="gray",
            font=("Segoe UI", 13)
        ).pack(
            anchor="w",
            padx=20,
            pady=(0, 18)
        )

        # ====================================================
        # ABOUT
        # ====================================================

        about = ctk.CTkFrame(
            scroll,
            fg_color=CARD,
            corner_radius=18
        )

        about.grid(
            row=1,
            column=0,
            columnspan=2,
            sticky="ew",
            padx=10,
            pady=(0, 15)
        )

        ctk.CTkLabel(
            about,
            text="ℹ About DriveSense AI",
            font=("Segoe UI", 18, "bold")
        ).pack(
            anchor="w",
            padx=20,
            pady=(18, 12)
        )

        ctk.CTkLabel(
            about,
            justify="left",
            wraplength=1200,
            text=(
                "DriveSense AI is an intelligent Driver Monitoring System "
                "designed to improve driver safety through real-time Computer "
                "Vision and Artificial Intelligence. The system monitors "
                "driver attention, fatigue, drowsiness, distraction, eye "
                "closure, yawning, and head position while driving."
            )
        ).pack(
            anchor="w",
            padx=20,
            pady=(0, 20)
        )

        # ====================================================
        # FEATURES
        # ====================================================

        features = ctk.CTkFrame(
            scroll,
            fg_color=CARD,
            corner_radius=18
        )

        features.grid(
            row=2,
            column=0,
            sticky="nsew",
            padx=(10, 7),
            pady=(0, 15)
        )

        ctk.CTkLabel(
            features,
            text="🚀 Features",
            font=("Segoe UI", 18, "bold")
        ).pack(
            anchor="w",
            padx=20,
            pady=(18, 15)
        )

        feature_list = [
            "✓ Real-time Face Detection",
            "✓ Blink Detection",
            "✓ Yawn Detection",
            "✓ Head Pose Estimation",
            "✓ Driver Distraction Detection",
            "✓ Fatigue Score Calculation",
            "✓ Live Monitoring Dashboard",
            "✓ Automatic Report Generation"
        ]

        for item in feature_list:

            ctk.CTkLabel(
                features,
                text=item,
                font=("Segoe UI", 13)
            ).pack(
                anchor="w",
                padx=25,
                pady=4
            )

        # ====================================================
        # QUICK ACTIONS
        # ====================================================

        shortcuts = ctk.CTkFrame(
            scroll,
            fg_color=CARD,
            corner_radius=18
        )

        shortcuts.grid(
            row=2,
            column=1,
            sticky="nsew",
            padx=(7, 10),
            pady=(0, 15)
        )

        ctk.CTkLabel(
            shortcuts,
            text="⚙ Quick Actions",
            font=("Segoe UI", 18, "bold")
        ).pack(
            anchor="w",
            padx=20,
            pady=(18, 15)
        )

        data = [
            ("Q", "Quit Application"),
            ("Generate Report", "Open latest driving report"),
            ("Test Alarm", "Test warning siren")
        ]

        for key, action in data:

            row = ctk.CTkFrame(
                shortcuts,
                fg_color="transparent"
            )

            row.pack(
                fill="x",
                padx=20,
                pady=7
            )

            ctk.CTkLabel(
                row,
                text=key,
                font=("Segoe UI", 13, "bold")
            ).pack(
                side="left"
            )

            ctk.CTkLabel(
                row,
                text=action,
                text_color="gray",
                font=("Segoe UI", 12)
            ).pack(
                side="right"
            )

        # ====================================================
        # DEVELOPMENT TEAM
        # ====================================================

        team = ctk.CTkFrame(
            scroll,
            fg_color=CARD,
            corner_radius=18
        )

        team.grid(
            row=3,
            column=0,
            columnspan=2,
            sticky="ew",
            padx=10,
            pady=(0, 15)
        )

        ctk.CTkLabel(
            team,
            text="👨‍💻 Development Team",
            font=("Segoe UI", 18, "bold")
        ).pack(
            anchor="w",
            padx=20,
            pady=(18, 10)
        )

        ctk.CTkLabel(
            team,
            text=(
                "Frontend: Abida Kulsoom\n"
                "Backend: Farman Ahmad\n\n"
                "DriveSense AI\n"
                "Driver Monitoring System\n"
                "2026"
            ),
            justify="left",
            text_color="gray",
            font=("Segoe UI", 13)
        ).pack(
            anchor="w",
            padx=20,
            pady=(0, 18)
        )