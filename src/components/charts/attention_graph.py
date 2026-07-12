import customtkinter as ctk

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class AttentionGraph(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(
            parent,
            fg_color="#1B2433",
            corner_radius=20
        )

        self.figure = Figure(
            figsize=(6, 2.2),   # only the initial size
            dpi=100
        )

        self.ax = self.figure.add_subplot(111)

        self.figure.patch.set_facecolor("#1B2433")
        self.ax.set_facecolor("#1B2433")

        self.ax.tick_params(colors="white")

        self.ax.spines["bottom"].set_color("white")
        self.ax.spines["left"].set_color("white")

        self.ax.spines["top"].set_visible(False)
        self.ax.spines["right"].set_visible(False)

        self.x = list(range(10))

        self.y = [74,73,76,78,81,83,82,84,85,86]

        self.line, = self.ax.plot(
            self.x,
            self.y,
            linewidth=3
        )

        self.ax.set_ylim(0,100)

        self.canvas = FigureCanvasTkAgg(
            self.figure,
            self
        )

        self.canvas.draw()

        self.canvas.get_tk_widget().pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        