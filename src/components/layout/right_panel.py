import customtkinter as ctk

from src.components.layout.gauge_row import GaugeRow
from src.components.layout.small_metrics_row import SmallMetricsRow
from src.components.cards.graph_card import GraphCard


class RightPanel(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(
            parent,
            fg_color="transparent"
        )

        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=1)

        self.grid_columnconfigure(0, weight=1)

        # ---------------- Gauges ----------------

        self.gauges = GaugeRow(self)

        self.gauges.grid(
            row=0,
            column=0,
            sticky="ew",
            pady=8
        )

        # ---------------- Small Metrics ----------------

        self.metrics = SmallMetricsRow(self)

        self.metrics.grid(
            row=1,
            column=0,
            sticky="ew",
            pady=8
        )

        # ---------------- Graph ----------------

        self.graph = GraphCard(self)

        self.graph.grid(
            row=2,
            column=0,
            sticky="nsew",
            pady=8
        )

    def update_data(self, result, fps):

    # ---------------- Attention ----------------

        attention = max(
            0,
            min(
                100,
                100 - result.fatigue_score
            )
        )

        self.gauges.attention_gauge.update_value(
            attention
        )

        # ---------------- Drowsiness ----------------

        self.gauges.drowsiness_gauge.update_value(
            100 if result.is_drowsy else 0
        )

        # ---------------- Blink Rate ----------------

        self.gauges.blink_gauge.update_value(
            result.blink_count
        )

        # ---------------- EAR ----------------

        self.gauges.ear_gauge.update_value(
            int(result.ear * 100)
        )

        # ---------------- Small Metrics ----------------

        self.metrics.update_values(
            result.yawn_count,
            result.direction,
            fps,
            "Online"
        )