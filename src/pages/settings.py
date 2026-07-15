import customtkinter as ctk
from theme import *


class SettingsPage(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(
            parent,
            fg_color="transparent"
        )

        self.grid_columnconfigure((0, 1), weight=1)

        # ================= Camera =================

        camera = ctk.CTkFrame(
            self,
            fg_color=CARD,
            corner_radius=18
        )

        camera.grid(
            row=0,
            column=0,
            padx=10,
            pady=10,
            sticky="nsew"
        )

        ctk.CTkLabel(
            camera,
            text="📷 Camera Settings",
            font=("Segoe UI",16,"bold")
        ).pack(anchor="w", padx=20, pady=(15,20))

        ctk.CTkLabel(camera,text="Camera ID").pack(anchor="w",padx=20)

        ctk.CTkEntry(camera).pack(fill="x",padx=20,pady=(5,15))

        ctk.CTkLabel(camera,text="FPS").pack(anchor="w",padx=20)

        ctk.CTkEntry(camera).pack(fill="x",padx=20,pady=(5,20))

        # ================= Detection =================

        detection = ctk.CTkFrame(
            self,
            fg_color=CARD,
            corner_radius=18
        )

        detection.grid(
            row=0,
            column=1,
            padx=10,
            pady=10,
            sticky="nsew"
        )

        ctk.CTkLabel(
            detection,
            text="🎯 Detection Thresholds",
            font=("Segoe UI",16,"bold")
        ).pack(anchor="w", padx=20, pady=(15,20))

        settings = [
            "EAR Threshold",
            "MAR Threshold",
            "Head Pose"
        ]

        for item in settings:

            ctk.CTkLabel(
                detection,
                text=item
            ).pack(anchor="w",padx=20)

            ctk.CTkEntry(
                detection
            ).pack(fill="x",padx=20,pady=(5,15))

        # ================= Buttons =================

        buttons = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        buttons.grid(
            row=1,
            column=0,
            columnspan=2,
            pady=20
        )

        ctk.CTkButton(
            buttons,
            text="💾 Save Settings",
            width=180,
            hover_color=BLUE
        ).pack(side="left",padx=10)

        ctk.CTkButton(
            buttons,
            text="↺ Restore Defaults",
            width=180,
            hover_color=BLUE
        ).pack(side="left",padx=10)