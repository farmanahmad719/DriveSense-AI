import customtkinter as ctk

from src.components.widgets.circular_gauge import CircularGauge

app = ctk.CTk()

app.geometry("400x400")

g = CircularGauge(app)

g.pack(expand=True)

g.set_value(73)

app.mainloop()