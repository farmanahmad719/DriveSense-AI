import customtkinter as ctk

from src.components.cards.small_card import SmallCard


class MiddleRow(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(
            parent,
            fg_color="transparent"
        )

        self.grid_columnconfigure((0,1,2,3,4), weight=1)

        SmallCard(self, "Yawn Count", "3", "#00E676").grid(
            row=0, column=1, padx=8, sticky="ew"
        )

        SmallCard(self, "Head Pose", "0°", "#29B6F6").grid(
            row=0, column=2, padx=8, sticky="ew"
        )

        SmallCard(self, "FPS", "30", "#00E676").grid(
            row=0, column=3, padx=8, sticky="ew"
        )

        SmallCard(self, "Camera", "Online", "#00E676").grid(
            row=0, column=4, padx=8, sticky="ew"
        )