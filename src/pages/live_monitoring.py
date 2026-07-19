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

        # ==================================================
        # LAYOUT
        # ==================================================

        self.grid_columnconfigure(0, weight=3)
        self.grid_columnconfigure(1, weight=1)

        self.grid_rowconfigure(0, weight=1)



        # ==================================================
        # CAMERA
        # ==================================================

        self.camera = CameraCard(
            self,
            large=True
        )

        self.camera.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=(0, 15),
            pady=10
        )

        # ==================================================
        # DRIVER STATUS
        # ==================================================

        self.driver = DriverStatusCard(
            self
        )

        self.driver.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=(10, 0),
            pady=10
        )
    def update_detection_result(self, result):

        self.camera.update_frame(
            result.frame
        )

        self.driver.update_data(
            result
        )
    
   