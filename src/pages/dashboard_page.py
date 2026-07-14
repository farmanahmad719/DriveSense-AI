import customtkinter as ctk

from src.components.layout.content_area import ContentArea
from src.components.rows.bottom_row import BottomRow


class DashboardPage(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(
            parent,
            fg_color="transparent"
        )

        self.grid_columnconfigure(0, weight=1)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=0)

        # ================= CONTENT =================

        self.content = ContentArea(self)

        self.content.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        # ================= BOTTOM =================

        self.bottom = BottomRow(self)

        self.bottom.grid(
            row=1,
            column=0,
            sticky="ew",
            pady=(10,0)
        )