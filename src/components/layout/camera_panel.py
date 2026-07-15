import customtkinter as ctk

from src.components.cards.camera_card import CameraCard


class CameraPanel(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(
            parent,
            fg_color="transparent"
        )

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)


        self.camera = CameraCard(parent)

        self.camera.grid(
            row=0,
            column=0,
            sticky="nsew"
        )