import customtkinter as ctk
from theme import *


class DriverStatusCard(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(
            parent,
            fg_color=CARD,
            corner_radius=18,
            height=420
        )

        self.pack_propagate(False)

        # ---------------- Title ----------------

        ctk.CTkLabel(
            self,
            text="👤 Driver Status",
            font=("Segoe UI", 16, "bold")
        ).pack(pady=(15, 5))

        # ---------------- Main Status ----------------

        self.status_label = ctk.CTkLabel(
            self,
            text="AWAKE",
            text_color="#00E676",
            font=("Segoe UI", 34, "bold")
        )

        self.status_label.pack(pady=(15, 15))

        self.blink = True
        self.animate_status()

        # ---------------- Divider ----------------

        ctk.CTkFrame(
            self,
            fg_color="#2A3445",
            height=2
        ).pack(fill="x", padx=20, pady=(0, 15))

        # ---------------- Live Metrics ----------------

        self.add_row("Attention", "95%")
        self.add_row("Fatigue", "12%")
        self.add_row("Eyes", "OPEN")
        self.add_row("Head", "FORWARD")
        self.add_row("Blinks", "23")
        self.add_row("Yawns", "2")

        # ---------------- Divider ----------------

        ctk.CTkFrame(
            self,
            fg_color="#2A3445",
            height=2
        ).pack(fill="x", padx=20, pady=15)

        # ---------------- Session ----------------

        bottom = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        bottom.pack(fill="x", padx=20)

        ctk.CTkLabel(
            bottom,
            text="Session",
            font=("Segoe UI", 13)
        ).pack(side="left")

        self.session_label = ctk.CTkLabel(
            bottom,
            text="00:08:31",
            font=("Segoe UI", 13, "bold")
        )

        self.session_label.pack(side="right")

    # =======================================

    def add_row(self, title, value):

        row = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        row.pack(
            fill="x",
            padx=20,
            pady=6
        )

        ctk.CTkLabel(
            row,
            text=title,
            font=("Segoe UI", 13)
        ).pack(side="left")

        value_label = ctk.CTkLabel(
            row,
            text=value,
            font=("Segoe UI", 13, "bold")
        )

        value_label.pack(side="right")

    # =======================================

    def animate_status(self):

        status = self.status_label.cget("text")

        if status in ["DROWSY", "DISTRACTED"]:

 
            if self.blink:

                self.status_label.configure(
                    text_color="#00E676"
                )

            else:

                self.status_label.configure(
                    text_color=CARD
                )

            self.blink = not self.blink

        else:

            # AWAKE stays solid green
            self.status_label.configure(
                text_color="#00E676"
            )

            self.blink = True

            
        self.after(
            500,
            self.animate_status
        )

    # =======================================

    def set_status(self, status):

        status = status.upper()

        self.status_label.configure(text=status)

        if status == "AWAKE":

            self.status_label.configure(
                text_color="#00E676"
            )

        elif status in ["DROWSY", "DISTRACTED"]:

            self.status_label.configure(
                text_color="#FF3B30"
            )

        else:

            self.status_label.configure(
                text_color="white"
            )