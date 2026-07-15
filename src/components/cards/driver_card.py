import customtkinter as ctk
from theme import *


class DriverCard(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(
            parent,
            fg_color=CARD,
            corner_radius=18,
            height=180
        )

        self.pack_propagate(False)

        ctk.CTkLabel(
            self,
            text="👤 Driver",
            font=("Segoe UI", 14, "bold")
        ).pack(pady=(15, 30))

        self.status_label = ctk.CTkLabel(
            self,
            text="AWAKE",
            text_color=ACCENT,
            font=("Segoe UI", 28, "bold")
        )

        self.status_label.pack()

        self.current_status = "AWAKE"
        self.blink_on = True

        self.after(3000, lambda: self.set_status("DROWSY"))
        self.after(8000, lambda: self.set_status("AWAKE"))
        self.after(13000, lambda: self.set_status("DISTRACTED"))

    def set_status(self, status):

        self.current_status = status

        if status == "AWAKE":

            self.status_label.configure(
                text="AWAKE",
                text_color=ACCENT
            )

        elif status == "DROWSY":

            self.status_label.configure(
                text="DROWSY",
                text_color=RED
            )

            self.blink_status()

        elif status == "DISTRACTED":

            self.status_label.configure(
                text="DISTRACTED",
                text_color=RED
            )

            self.blink_status()

    def blink_status(self):

        if self.current_status == "AWAKE":
            return

        if self.blink_on:
            self.status_label.configure(text_color=RED)
        else:
            self.status_label.configure(text_color=CARD)

        self.blink_on = not self.blink_on

        self.after(500, self.blink_status)