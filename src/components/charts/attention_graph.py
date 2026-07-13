import customtkinter as ctk
from theme import *

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
            figsize=(4, 2.5),   # only the initial size
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

        self.x = list(range(0, 20, 2))

        self.datasets = {
            "Attention": [74, 73, 76, 78, 81, 83, 82, 84, 85, 86],

             "Blink Rate": [18, 17, 16, 18, 20, 19, 21, 18, 17, 16],

              "Drowsiness": [12, 13, 14, 18, 22, 20, 16, 15, 11, 9],

             "EAR": [0.31, 0.30, 0.32, 0.29, 0.28, 0.30, 0.31, 0.32, 0.31, 0.30]

        }

        self.current_metric = "Attention"

        self.line, = self.ax.plot(
            self.x,
            self.datasets[self.current_metric],
            linewidth=2
        )

        self.ax.set_ylim(0,100)

        self.canvas = FigureCanvasTkAgg(
            self.figure,
            self
        )

        self.figure.tight_layout(rect=[0, 0.15, 1, 0.92])
        
        #self.canvas.draw()

        self.canvas.get_tk_widget().pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        self.show_metric("Attention")

    def show_metric(self, metric):

        self.current_metric = metric

        colors = {
            "Attention": ACCENT,
            "Blink Rate": BLUE,
            "Drowsiness": ORANGE,
            "EAR": PURPLE
        }        

        self.line.set_ydata(self.datasets[metric])
        self.line.set_color(colors[metric])

        if metric == "EAR":
            self.ax.set_ylim(0.15, 0.40)
            self.ax.set_ylabel("EAR")

        elif metric=="Attention":
            self.ax.set_ylim(0,100)
            self.ax.set_ylabel("Attention(%)")

        elif metric == "Blink Rate":
             self.ax.set_ylim(0, 30)
             self.ax.set_ylabel("Blinks/min")

        else:
            self.ax.set_ylim(0, 100)
            self.ax.set_ylabel(metric)

        self.ax.set_title(f"{metric} Trend")
        self.ax.set_xlabel("Time (sec)")

        self.ax.title.set_color("white")
        self.ax.yaxis.label.set_color("white")
        self.ax.xaxis.label.set_color("white")

        
        self.canvas.draw_idle()

        