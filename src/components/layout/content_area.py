import customtkinter as ctk

from src.components.layout.camera_panel import CameraPanel
from src.components.layout.right_panel import RightPanel


class ContentArea(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(
            parent,
            fg_color="transparent"
        )

        self.grid_columnconfigure(0, weight=3)   # Camera
        self.grid_columnconfigure(1, weight=7)   # Right Panel

        self.grid_rowconfigure(0, weight=1)

        self.camera = CameraPanel(self)

        self.camera.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=(0,15)
        )

        self.right = RightPanel(self)

        self.right.grid(
            row=0,
            column=1,
            sticky="nsew"
        )