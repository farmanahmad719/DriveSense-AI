import customtkinter as ctk
from theme import *


class AlertCard(ctk.CTkFrame):

    def __init__(self,parent):

        super().__init__(
            parent,
            fg_color=CARD,
            corner_radius=18,
            height=220
        )

        self.grid_propagate(False)

        title = ctk.CTkLabel(
            self,
            text="🚨 Alerts",
            font=("Segoe UI",18,"bold")
        )

        title.pack(anchor="w",padx=15,pady=(15,10))

        textbox = ctk.CTkTextbox(
            self,
            fg_color="#222B3A"
        )

        textbox.pack(fill="both",expand=True,padx=15,pady=(0,15))

        textbox.insert("end","10:22  Driver Awake\n")
        textbox.insert("end","10:23  Blink Detected\n")
        textbox.insert("end","10:25  Yawn Detected\n")