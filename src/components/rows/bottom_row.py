import customtkinter as ctk

from src.components.cards.alert_card import AlertCard
from src.components.cards.driver_card import DriverCard
from src.components.cards.detection_card import DetectionCard
from src.components.cards.trip_card import TripCard


class BottomRow(ctk.CTkFrame):

    def __init__(self, parent, alert_systems):

        super().__init__(
            parent,
            fg_color="transparent"
        )
        self.alert_system = alert_systems
        print(
            "BottomRow AlertSystem:",
            id(self.alert_system)
        )

        for i in range(4):

            self.grid_columnconfigure(
                i,
                weight=1
            )
        
        # ---------------- Alert ----------------

        self.alert_card = AlertCard(
            self,
            self.alert_system
        )
        self.alert_card.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=8
        )

        # ---------------- Driver ----------------

        self.driver_card = DriverCard(self)

        self.driver_card.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=8
        )

        # ---------------- Detection ----------------

        self.detection_card = DetectionCard(self)

        self.detection_card.grid(
            row=0,
            column=2,
            sticky="nsew",
            padx=8
        )

        # ---------------- Trip ----------------

        self.trip_card = TripCard(self)

        self.trip_card.grid(
            row=0,
            column=3,
            sticky="nsew",
            padx=8
        )

    def update_data(self, result):

        print("🔥 DETECTION CARD UPDATE CALLED")

        print(
            "Face:",
            result.face_detected,
            "Drowsy:",
            result.is_drowsy,
            "Direction:",
            result.direction
        )

        self.driver_card.update_data(
            result
        )

        self.detection_card.update_data(
            result
        )

        self.alert_card.update_data(
            result
        )

        self.trip_card.update_data(
            result
        )

        alert_count = len(
            self.alert_card.alert_system.get_alerts()
        )

        self.trip_card.update_alert_count(
            alert_count
        )
        self.trip_card.update_duration()