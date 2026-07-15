import customtkinter as ctk
from theme import *


class MetricCard(ctk.CTkFrame):

    def __init__(self,parent,title,value,color):

        super().__init__(

            parent,

            fg_color=CARD,

            corner_radius=20,

            width=180,

            height=260

        )

        self.grid_propagate(False)

        title_label = ctk.CTkLabel(

            self,

            text=title,

            font=("Segoe UI",16)

        )

        title_label.pack(
            pady=(25,15)
        )

        circle = ctk.CTkProgressBar(

            self,

            progress_color=color,

            width=120,

            height=12

        )

        circle.set(0.7)

        circle.pack()

        value_label = ctk.CTkLabel(

            self,

            text=value,

            font=("Segoe UI",28,"bold")

        )

        value_label.pack(
            pady=25
        )