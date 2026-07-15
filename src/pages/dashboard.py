import customtkinter as ctk
from theme import *

from src.components.sidebar import Sidebar
from src.components.navbar import Navbar

from src.pages.dashboard_page import DashboardPage
from src.pages.live_monitoring import LiveMonitoringPage
from src.pages.analytics import AnalyticsPage
from src.pages.alerts import AlertsPage
from src.pages.reports import ReportsPage
from src.pages.settings import SettingsPage
from src.pages.help import HelpPage


class Dashboard(ctk.CTk):

    def __init__(self):

        super().__init__()

        self.title("DriveSense AI")

        self.geometry("1600x900")

        self.minsize(1400, 800)

        self.configure(fg_color=BACKGROUND)

        # ================= GRID =================

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)

        self.grid_rowconfigure(0, weight=1)

        # ================= SIDEBAR =================

        self.sidebar = Sidebar(
            self,
            self.show_page
        )

        self.sidebar.grid(
            row=0,
            column=0,
            sticky="ns"
        )

        # ================= MAIN AREA =================

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

        self.main.grid_rowconfigure(0, weight=0)
        self.main.grid_rowconfigure(1, weight=1)

        self.main.grid_columnconfigure(0, weight=1)

        # ================= NAVBAR =================

        self.navbar = Navbar(self.main)

        self.navbar.grid(
            row=0,
            column=0,
            sticky="ew",
            padx=20,
            pady=20
        )

        # ================= PAGE CONTAINER =================

        self.page_container = ctk.CTkFrame(
            self.main,
            fg_color="transparent"
        )

        self.page_container.grid(
            row=1,
            column=0,
            sticky="nsew",
            padx=20,
            pady=(0,20)
        )

        self.page_container.grid_rowconfigure(0, weight=1)
        self.page_container.grid_columnconfigure(0, weight=1)

        # ================= LOAD DASHBOARD PAGE =================

        self.current_page = None
        self.show_page("Dashboard")

    def show_page(self, page):

        if self.current_page is not None:
            self.current_page.destroy()

        if page == "Dashboard":

            self.current_page = DashboardPage(
                self.page_container
            )

        elif page == "Live Monitoring":

            self.current_page = LiveMonitoringPage(
                self.page_container
            )

        elif page == "Analytics":
            
            self.current_page = AnalyticsPage(
                self.page_container
            )

        elif page == "Alerts":

            self.current_page = AlertsPage(
                self.page_container
            ) 

        elif page == "Reports":

            self.current_page = ReportsPage(
                self.page_container
            )

        elif page == "Settings":

            self.current_page = SettingsPage(
                self.page_container
            )

        elif page == "Help":

            self.current_page = HelpPage(
                self.page_container
            )

        else:

            self.current_page = ctk.CTkLabel(
                self.page_container,
                text=f"{page}\n\nComing Soon",
                font=("Segoe UI", 28, "bold")
            )

        self.current_page.grid(
            row=0,
            column=0,
            sticky="nsew"
        )