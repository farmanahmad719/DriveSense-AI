import customtkinter as ctk


class CircularGauge(ctk.CTkCanvas):

    def __init__(self, parent, size=150, color="#00E676"):

        super().__init__(
            parent,
            width=size,
            height=size,
            bg="#111827",
            highlightthickness=0
        )

        self.size = size
        self.center = size / 2
        self.radius = size / 2 - 15

        self.color = color
        self.value = 0

        self.draw_gauge()

    def draw_gauge(self):

        self.delete("all")

        x1 = 15
        y1 = 15
        x2 = self.size - 15
        y2 = self.size - 15

        # Background ring
        self.create_arc(
            x1,
            y1,
            x2,
            y2,
            start=90,
            extent=-360,
            style="arc",
            outline="#2C3647",
            width=12
        )

        # Progress ring
        angle = (self.value / 100) * 360

        self.create_arc(
            x1,
            y1,
            x2,
            y2,
            start=90,
            extent=-angle,
            style="arc",
            outline=self.color,
            width=12
        )

        # Percentage
        self.create_text(
            self.center,
            self.center-8,
            text=f"{self.value}%",
            fill="white",
            font=("Segoe UI", 24, "bold")
        )

        # Status
        if self.value >= 80:
            status = "Excellent"
        elif self.value >= 60:
            status = "Good"
        elif self.value >= 40:
            status = "Warning"
        else:
            status = "Critical"

        self.create_text(
            self.center,
            self.center+20,
            text=status,
            fill="#9CA3AF",
            font=("Segoe UI", 12)
        )

    def set_value(self, target):
        
        step = 1 if target > self.value else -1
        
        def animate():
            
            if self.value != target:
                self.value += step
                self.draw_gauge()
                self.after(10, animate)

        animate()