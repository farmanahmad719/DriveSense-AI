import customtkinter as ctk

from src.components.charts.attention_graph import AttentionGraph


class AnalyticsPage(ctk.CTkFrame):

    def __init__(self, parent,dashboard):

        super().__init__(
            parent,
            fg_color="transparent"
        )
        self.dashboard = dashboard
        # ================= Grid =================

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # ================= Attention =================

        self.attention = AttentionGraph(self)
        self.attention.grid(
            row=0,
            column=0,
            padx=10,
            pady=10,
            sticky="nsew"
        )

        self.attention.show_metric("Attention")

        # ================= Blink =================

        self.blink = AttentionGraph(self)
        self.blink.grid(
            row=0,
            column=1,
            padx=10,
            pady=10,
            sticky="nsew"
        )

        self.blink.show_metric("Blink Rate")

        # ================= Drowsiness =================

        self.drowsiness = AttentionGraph(self)
        self.drowsiness.grid(
            row=1,
            column=0,
            padx=10,
            pady=10,
            sticky="nsew"
        )

        self.drowsiness.show_metric("Drowsiness")

        # ================= EAR =================

        self.ear = AttentionGraph(self)
        self.ear.grid(
            row=1,
            column=1,
            padx=10,
            pady=10,
            sticky="nsew"
        )

        self.ear.show_metric("EAR")
    def update_data(self, history):

        if not history:

            return

        # ---------------- Attention ----------------

        attention_data = []

        for result in history:

            attention = max(
                0,
                min(
                    100,
                    100 - result.fatigue_score
                )
            )

            attention_data.append(
                attention
            )

        self.attention.datasets["Attention"] = (
            attention_data[-10:]
        )

        self.attention.x = list(
            range(
                len(
                    self.attention.datasets["Attention"]
                )
            )
        )

        self.attention.line.set_xdata(
            self.attention.x
        )

        self.attention.line.set_ydata(
            self.attention.datasets["Attention"]
        )

        self.attention.ax.set_xlim(
            0,
            max(
                10,
                len(
                    self.attention.x
                )
            )
        )

        self.attention.canvas.draw_idle()    
                # ---------------- Blink Rate ----------------

        # ---------------- Blink Rate ----------------

        blink_data = []

        for index in range(
            len(history)
        ):

            if index == 0:

                blink_data.append(
                    0
                )

            else:

                previous_count = (
                    history[index - 1].blink_count
                )

                current_count = (
                    history[index].blink_count
                )

                new_blinks = (
                    current_count - previous_count
                )

                blink_rate = (
                    new_blinks * 60
                )

                blink_data.append(
                    blink_rate
                )

        self.blink.datasets["Blink Rate"] = (
            blink_data[-10:]
        )

        self.blink.x = list(
            range(
                len(
                    self.blink.datasets["Blink Rate"]
                )
            )
        )

        self.blink.line.set_xdata(
            self.blink.x
        )

        self.blink.line.set_ydata(
            self.blink.datasets["Blink Rate"]
        )

        self.blink.ax.set_xlim(
            0,
            max(
                10,
                len(
                    self.blink.x
                )
            )
        )

        self.blink.canvas.draw_idle()
                # ---------------- Drowsiness ----------------

        drowsiness_data = []

        for result in history:

            if result.is_drowsy:

                drowsiness_data.append(
                    100
                )

            else:

                drowsiness_data.append(
                    0
                )

        self.drowsiness.datasets["Drowsiness"] = (
            drowsiness_data[-10:]
        )

        self.drowsiness.x = list(
            range(
                len(
                    self.drowsiness.datasets[
                        "Drowsiness"
                    ]
                )
            )
        )

        self.drowsiness.line.set_xdata(
            self.drowsiness.x
        )

        self.drowsiness.line.set_ydata(
            self.drowsiness.datasets[
                "Drowsiness"
            ]
        )

        self.drowsiness.ax.set_xlim(
            0,
            max(
                10,
                len(
                    self.drowsiness.x
                )
            )
        )

        self.drowsiness.canvas.draw_idle()
                # ---------------- EAR ----------------

        ear_data = []

        for result in history:

            ear_data.append(
                result.ear
            )

        self.ear.datasets["EAR"] = (
            ear_data[-10:]
        )

        self.ear.x = list(
            range(
                len(
                    self.ear.datasets["EAR"]
                )
            )
        )

        self.ear.line.set_xdata(
            self.ear.x
        )

        self.ear.line.set_ydata(
            self.ear.datasets["EAR"]
        )

        self.ear.ax.set_xlim(
            0,
            max(
                10,
                len(
                    self.ear.x
                )
            )
        )

        self.ear.canvas.draw_idle()