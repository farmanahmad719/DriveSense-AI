import customtkinter as ctk

from theme import *

from src.components.cards.camera_card import CameraCard
from src.components.cards.driver_status_card import DriverStatusCard

class LiveMonitoringPage(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(
            parent,
            fg_color="transparent"
        )

        # Layout
        self.grid_columnconfigure(0, weight=5)
        self.grid_columnconfigure(1, weight=1)

        self.grid_rowconfigure(0, weight=1)

        # ================= CAMERA =================

        self.camera = CameraCard(self, large=True)

        self.camera.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=(0,15),
            pady=10
        )

        # ================= RIGHT PANEL =================

        right = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        right.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=(10,0),
            pady=10
        )
        
        right.grid_columnconfigure(0, weight=1)
        right.grid_rowconfigure(0, weight=1)
        right.grid_rowconfigure(1, weight=2)

        # ================= DRIVER INFO =================

        info = ctk.CTkFrame(
            right,
            fg_color=CARD,
            corner_radius=18,
            height=200
        )

        info.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=0,
            pady=(0,15)
        )

        info.pack_propagate(False)

        ctk.CTkLabel(
            info,
            text="👤 Driver Information",
            font=("Segoe UI",16,"bold")
        ).pack(
            anchor="w",
            padx=20,
            pady=(15,15)
        )

        details = [
            ("Name", "Farman"),
            ("Vehicle", "MH12AB1234"),
            ("Driver ID", "DR001"),
            ("Trip ID", "TRP001")
        ]

        for title, value in details:

            row = ctk.CTkFrame(
                info,
                fg_color="transparent"
            )

            row.pack(
                fill="x",
                padx=20,
                pady=5
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

        # ================= DRIVER STATUS =================

        self.driver = DriverStatusCard(right)
        
        self.driver.grid(
            row=1,
            column=0,
            sticky="nsew",
            padx=0,
            pady=(10, 0)
        )