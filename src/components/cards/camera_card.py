import customtkinter as ctk
from theme import *


class CameraCard(ctk.CTkFrame):

    def __init__(self,parent):

        super().__init__(

            parent,

            fg_color=CARD,

            corner_radius=20,

            height=260

        )

        self.grid_propagate(False)

        title = ctk.CTkLabel(

            self,

            text="📷 Live Camera Feed",

            font=("Segoe UI",20,"bold")

        )

        title.pack(anchor="w",padx=20,pady=(15,10))

        frame = ctk.CTkFrame(

            self,

            fg_color="#202938",

            corner_radius=15

        )

        frame.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=(0,15)
        )

        label = ctk.CTkLabel(

            frame,

            text="Camera Preview\n(Coming Soon)",

            font=("Segoe UI",18)

        )

        label.place(relx=0.5,rely=0.5,anchor="center")