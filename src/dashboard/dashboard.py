import customtkinter as ctk
from theme import *

from src.components.sidebar import Sidebar
from src.components.navbar import Navbar
from src.components.rows.top_row import TopRow
from src.components.rows.middle_row import MiddleRow
from src.components.rows.graph_row import GraphRow
from src.components.rows.bottom_row import BottomRow


class Dashboard(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("DriveSense AI")

        self.geometry("1600x900")

        self.minsize(1400, 800)

        self.configure(fg_color=BACKGROUND)

        # ---------- GRID ----------

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)

        self.grid_rowconfigure(0, weight=1)

        # ---------- SIDEBAR ----------

        self.sidebar = Sidebar(self)

        self.sidebar.grid(
            row=0,
            column=0,
            sticky="ns"
        )

        # ---------- MAIN ----------

        self.main = ctk.CTkFrame(
            self,
            fg_color=BACKGROUND,
            corner_radius=0
        )

        self.main.grid(
            row=0,
            column=1,
            sticky="nsew"
        )

        self.main.grid_rowconfigure(0, weight=0)   # Navbar
        self.main.grid_rowconfigure(1, weight=0)   # Top Row
        self.main.grid_rowconfigure(2, weight=0)   # Middle Row
        self.main.grid_rowconfigure(3, weight=1)   # Remaining space
        self.main.grid_rowconfigure(4, weight=0)
        
        self.main.grid_columnconfigure(0, weight=1)

        self.navbar = Navbar(self.main)
        
        self.navbar.grid(
            row=0,
            column=0,
            sticky="ew",
            padx=20,
            pady=20
        )

        self.top = TopRow(self.main)

        self.top.grid(
            row=1,
            column=0,
            sticky="ew",
            padx=20,
            pady=10
        )

        self.middle = MiddleRow(self.main)

        self.middle.grid(
             row=2,
             column=0,
             sticky="ew",
             padx=20,
             pady=(0,10)
        )

        self.graph = GraphRow(self.main)

        self.graph.grid(
            row=3,
            column=0,
            sticky="nsew",
            padx=20,
            pady=10
        )

        self.bottom = BottomRow(self.main)

        self.bottom.grid(
            row=4,
            column=0,
            sticky="ew",
            padx=20,
            pady=10
        )