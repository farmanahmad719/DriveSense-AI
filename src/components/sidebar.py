import customtkinter as ctk
from theme import *


class Sidebar(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(
            parent,
            width=240,
            fg_color=SIDEBAR,
            corner_radius=0
        )

        self.grid_propagate(False)

        self.logo = ctk.CTkLabel(
            self,
            text="🚗 DriveSense AI",
            font=("Segoe UI", 22, "bold"),
            text_color="white"
        )

        self.logo.pack(
            pady=(30,40)
        )

        menus = [
            "Dashboard",
            "Live Monitoring",
            "Analytics",
            "Alerts",
            "Reports",
            "Settings",
            "Help"
        ]

        for item in menus:

            button = ctk.CTkButton(

                self,

                text=item,

                fg_color="transparent",

                hover_color="#12354F",

                anchor="w",

                height=45,

                font=("Segoe UI",15)

            )

            button.pack(
                fill="x",
                padx=15,
                pady=5
            )