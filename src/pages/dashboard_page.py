import customtkinter as ctk

from src.components.layout.content_area import ContentArea
from src.components.rows.bottom_row import BottomRow


class DashboardPage(ctk.CTkFrame):

    def __init__(self, parent, dashboard, alert_systems):

        super().__init__(
            parent,
            fg_color="transparent"
        )
        self.alert_system = alert_systems

        self.dashboard = dashboard

        self.grid_columnconfigure(
            0,
            weight=1
        )

        self.grid_rowconfigure(
            0,
            weight=1
        )

        self.grid_rowconfigure(
            1,
            weight=0
        )

        # ================= CONTENT =================

        self.content = ContentArea(
            self,
            dashboard
        )

        self.content.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        # ================= BOTTOM =================

        self.bottom = BottomRow(
            self,
            self.alert_system
        )

        self.bottom.grid(
            row=1,
            column=0,
            sticky="ew",
            pady=(10, 0)
        )

    # =================================================
    # RECEIVE DETECTION RESULT
    # =================================================

    def update_detection_result(self, result):

        print("🔥 DashboardPage received result")

        self.content.update_detection_result(
            result
        )
        self.bottom.update_data(result)

        # =================================================
    # CLEANUP
    # =================================================

    def stop(self):

        print("🛑 DashboardPage stopping")

        self.content.stop()