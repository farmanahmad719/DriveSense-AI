import customtkinter as ctk

from theme import *


class SystemStatusCard(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(
            parent,
            fg_color=CARD,
            corner_radius=18
        )

        # ================= HEADER =================

        ctk.CTkLabel(
            self,
            text="🖥 System Status",
            font=("Segoe UI", 16, "bold"),
            text_color="white"
        ).pack(
            anchor="w",
            padx=20,
            pady=(15, 9)
        )

        # ================= MONITORING =================

        ctk.CTkLabel(
            self,
            text="✓ Monitoring Active",
            text_color="white",
            font=("Segoe UI", 13, "bold")
        ).pack(
            anchor="w",
            padx=20,
            pady=1
        )

        # ================= CAMERA =================

        ctk.CTkLabel(
            self,
            text="✓ Camera Online",
            text_color="white",
            font=("Segoe UI", 13, "bold")
        ).pack(
            anchor="w",
            padx=20,
            pady=(1, 3)
        )

        # ================= BACKEND =================

        ctk.CTkLabel(
            self,
            text="✓ Backend Connected",
            text_color="white",
            font=("Segoe UI", 13, "bold")
        ).pack(
            anchor="w",
            padx=20,
            pady=(3,5)
        )