import customtkinter as ctk

from src.components.cards.alert_card import AlertCard
from src.components.cards.driver_card import DriverCard
from src.components.cards.detection_card import DetectionCard
from src.components.cards.trip_card import TripCard


class BottomRow(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(parent, fg_color="transparent")

        for i in range(4):
            self.grid_columnconfigure(i, weight=1)

        AlertCard(self).grid(row=0,column=0,sticky="nsew",padx=8)

        DriverCard(self).grid(row=0,column=1,sticky="nsew",padx=8)

        DetectionCard(self).grid(row=0,column=2,sticky="nsew",padx=8)

        TripCard(self).grid(row=0,column=3,sticky="nsew",padx=8)