import customtkinter as ctk

from theme import *

from src.components.cards.camera_card import CameraCard
from src.components.cards.driver_status_card import DriverStatusCard


class LiveMonitoringPage(ctk.CTkFrame):

    def __init__(self, parent, dashboard):

        super().__init__(
            parent,
            fg_color="transparent"
        )

        self.dashboard = dashboard

        # ==================================================
        # LAYOUT
        # ==================================================

        self.grid_columnconfigure(
            0,
            weight=3
        )

        self.grid_columnconfigure(
            1,
            weight=1
        )

        self.grid_rowconfigure(
            0,
            weight=0
        )

        self.grid_rowconfigure(
            1,
            weight=1
        )

        # ==================================================
        # CONTROLS
        # ==================================================

        controls = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        controls.grid(
            row=0,
            column=0,
            columnspan=2,
            sticky="ew",
            pady=(0, 10)
        )

        # ---------------- LIVE CAMERA ----------------

        ctk.CTkButton(
            controls,
            text="🎥 Live Camera",
            command=self.dashboard.start_live_camera
        ).pack(
            side="left",
            padx=(0, 10)
        )

        # ---------------- RECORDED VIDEO ----------------

        ctk.CTkButton(
            controls,
            text="📁 Select Recorded Video",
            command=self.dashboard.select_recorded_video
        ).pack(
            side="left"
        )

        # ==================================================
        # CAMERA
        # ==================================================

        self.camera = CameraCard(
            self,
            large=True
        )

        self.camera.grid(
            row=1,
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
            row=1,
            column=1,
            sticky="nsew",
            padx=(10, 0),
            pady=10
        )

    # ==================================================
    # UPDATE DETECTION RESULT
    # ==================================================

    def update_detection_result(self, result):

        self.camera.update_frame(
            result.frame
        )

        self.driver.update_data(
            result
        )