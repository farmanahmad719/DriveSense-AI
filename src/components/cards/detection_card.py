import customtkinter as ctk
from theme import *


class DetectionCard(ctk.CTkFrame):

    def __init__(self,parent):

        super().__init__(
            parent,
            fg_color=CARD,
            corner_radius=18,
            height=180
        )

        self.pack_propagate(False)

        ctk.CTkLabel(
            self,
            text="🤖 AI Detection",
            font=("Segoe UI",14,"bold")
        ).pack(pady=7)

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