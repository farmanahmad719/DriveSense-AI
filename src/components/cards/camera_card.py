import customtkinter as ctk
from theme import *


class CameraCard(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(
            parent,
            fg_color=CARD,
            corner_radius=20,
            width=400,
            height=480
        )

        #self.grid_propagate(False)
        self.pack_propagate(False)

        # =========================
        # Header
        # =========================

        header = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        header.pack(
            fill="x",
            padx=20,
            pady=(15,10)
        )

        title = ctk.CTkLabel(
            header,
            text="🎥 Live Camera Feed",
            font=("Segoe UI",18,"bold")
        )

        title.pack(side="left")

        live = ctk.CTkLabel(
            header,
            text="● LIVE",
            text_color="#00E676",
            font=("Segoe UI",13,"bold")
        )

        live.pack(side="right")

        # =========================
        # Camera Area
        # =========================

        self.camera_frame = ctk.CTkFrame(
            self,
            fg_color="#202938",
            corner_radius=15,
            width=370,
            height=280
        )

        self.camera_frame.pack(
            padx=15,
            pady=(0,15)
        )

        self.camera_frame.pack_propagate(False)

        self.camera_label = ctk.CTkLabel(
            self.camera_frame,
            text="Camera Preview\n(Waiting for Backend)",
            font=("Segoe UI",18)
        )

        self.camera_label.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )

        # =========================
        # Status Section
        # =========================

        status = ctk.CTkFrame(
            self,
            fg_color="#202938",
            corner_radius=15
        )

        status.pack(
            fill="x",
            padx=15,
            pady=(0,15)
        )

        info = [
            ("🟢 Status", "Connected"),
            ("⚡ FPS", "30"),
            ("📐 Resolution", "640 × 480")
        ]

        for title, value in info:

            row = ctk.CTkFrame(
                status,
                fg_color="transparent"
            )

            row.pack(
                fill="x",
                padx=15,
                pady=8
            )

            ctk.CTkLabel(
                row,
                text=title,
                font=("Segoe UI",13)
            ).pack(side="left")

            ctk.CTkLabel(
                row,
                text=value,
                font=("Segoe UI",13,"bold")
            ).pack(side="right")