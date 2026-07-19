import customtkinter as ctk

from src.components.layout.camera_panel import CameraPanel
from src.components.layout.right_panel import RightPanel


class ContentArea(ctk.CTkFrame):

    def __init__(self, parent, dashboard):

        super().__init__(
            parent,
            fg_color="transparent"
        )

        self.dashboard = dashboard

        # ================= LAYOUT =================

        self.grid_columnconfigure(
            0,
            weight=3
        )

        self.grid_columnconfigure(
            1,
            weight=7
        )

        self.grid_rowconfigure(
            0,
            weight=1
        )

        # ================= CAMERA =================

        self.camera = CameraPanel(
            self
        )

        self.camera.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=(0, 15)
        )

        # ================= RIGHT PANEL =================

        self.right = RightPanel(
            self
        )

        self.right.grid(
            row=0,
            column=1,
            sticky="nsew"
        )

    # =================================================
    # UPDATE DASHBOARD
    # =================================================

    def update_detection_result(self, result):

        # Update camera frame

        self.camera.update_frame(
            result.frame
        )

        # Camera connection status

        self.camera.camera.set_connection(
            True
        )

        # Update right-side metrics

        self.right.update_data(
            result,
            30
        )
