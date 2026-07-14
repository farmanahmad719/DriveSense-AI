import customtkinter as ctk
from theme import *


class CameraCard(ctk.CTkFrame):

    def __init__(self, parent, large=False):

        super().__init__(
            parent,
            fg_color=CARD,
            corner_radius=20,
            width=400,
            height=350
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

        live_frame = ctk.CTkFrame(
            header,
            fg_color="transparent"
        )

        live_frame.pack(side="right")

        self.live_dot = ctk.CTkLabel(
            live_frame,
            text="●",
            text_color=ACCENT,
            font=("Segoe UI", 14, "bold")
        )

        self.live_dot.pack(side="left", padx=(0, 4))

        ctk.CTkLabel(
            live_frame,
            text="LIVE",
            font=("Segoe UI", 13, "bold")
         ).pack(side="left")

        self.live_visible = True
        self.blink_live()

        # =========================
        # Camera Area
        # =========================

        if large:
            camera_height = 470
            camera_width = 650
        else:
            camera_height = 280
            camera_width = 370

        self.camera_frame = ctk.CTkFrame(
            self,
            fg_color="#202938",
            corner_radius=15,
            width=camera_width,
            height=camera_height
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

            value_label = ctk.CTkLabel(
                row,
                text=value,
                font=("Segoe UI",13,"bold")
            )

            value_label.pack(side="right")

            if title == "🟢 Status":
                self.status_label = value_label

        self.after(5000, lambda: self.set_connection(False))
        self.after(10000, lambda: self.set_connection(True))

    def blink_live(self):

        if self.live_visible:
            self.live_dot.configure(text_color=ACCENT)
        else:
            self.live_dot.configure(text_color=CARD)

        self.live_visible = not self.live_visible

        self.after(500, self.blink_live)


    def set_connection(self, connected):

        if connected:

            self.status_label.configure(
                text="Connected",
                text_color=ACCENT
            )

        else:

            self.status_label.configure(
                text="Disconnected",
                text_color=RED
            )