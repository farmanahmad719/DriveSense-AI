import customtkinter as ctk
from theme import *


class DetectionCard(ctk.CTkFrame):

    def __init__(self,parent):

        super().__init__(
            parent,
            fg_color=CARD,
            corner_radius=18,
            height=220
        )

        self.grid_propagate(False)

        ctk.CTkLabel(
            self,
            text="🤖 AI Detection",
            font=("Segoe UI",18,"bold")
        ).pack(pady=15)

        items = [
            "✅ Face",
            "✅ Eyes",
            "❌ Phone",
            "✅ Head"
        ]

        for item in items:

            ctk.CTkLabel(
                self,
                text=item,
                anchor="w"
            ).pack(anchor="w",padx=20,pady=5)