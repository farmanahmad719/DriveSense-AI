import customtkinter as ctk
from theme import *
import time
from tkinter import filedialog
from src.components.sidebar import Sidebar
from src.components.navbar import Navbar
from src.engine.detection_engine import DetectionEngine

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
        # ================= BACKEND =================

        self.engine = DetectionEngine()

        self.engine.start(0)

        self.current_result = None
        self.session_history = []
        self.last_history_time = 0

        self.after(30, self.update_detection)
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
        self.analytics_page = None
        self.current_page = None
        self.show_page("Dashboard")

    def show_page(self, page):

    # Hide current page
        if self.current_page is not None:

            self.current_page.grid_forget()

        # ================= DASHBOARD =================

        if page == "Dashboard":

            if not hasattr(self, "dashboard_page"):

                self.dashboard_page = DashboardPage(
                    self.page_container,
                    self
                )

            self.current_page = self.dashboard_page

        # ================= LIVE MONITORING =================

        elif page == "Live Monitoring":

            if not hasattr(self, "live_monitoring_page"):

                self.live_monitoring_page = LiveMonitoringPage(
                    self.page_container,
                    self
                )

            self.current_page = self.live_monitoring_page

        # ================= ANALYTICS =================

        elif page == "Analytics":

            self.current_page = AnalyticsPage(
                self.page_container,
                self
    )

        # ================= ALERTS =================

        elif page == "Alerts":

            if not hasattr(self, "alerts_page"):

                self.alerts_page = AlertsPage(
                    self.page_container
                )

            self.current_page = self.alerts_page

        # ================= REPORTS =================

        elif page == "Reports":

            print("📄 REPORTS PAGE SELECTED")

            self.current_page = ReportsPage(
                self.page_container,
                self
            )

        # ================= SETTINGS =================

        elif page == "Settings":

            if not hasattr(self, "settings_page"):

                self.settings_page = SettingsPage(
                    self.page_container
                )

            self.current_page = self.settings_page

        # ================= HELP =================

        elif page == "Help":

            if not hasattr(self, "help_page"):

                self.help_page = HelpPage(
                    self.page_container
                )

            self.current_page = self.help_page

        # ================= SHOW PAGE =================

        self.current_page.grid(
            row=0,
            column=0,
            sticky="nsew"
        )
    def update_detection(self):

        ret, result = self.engine.process_frame()

        if ret and result is not None:

            self.current_result = result

            # ---------------- LIVE UI ----------------

            if hasattr(
                self.current_page,
                "update_detection_result"
            ):

                self.current_page.update_detection_result(
                    result
                )

            # ---------------- SESSION HISTORY ----------------

            current_time = time.time()

            if current_time - self.last_history_time >= 1:

                self.session_history.append(
                    result
                )

                self.last_history_time = current_time

                print(
                    "History sample added:",
                    len(self.session_history)
                )

        # ---------------- ANALYTICS ----------------

        if hasattr(
            self.current_page,
            "update_data"
        ):

            self.current_page.update_data(
                self.session_history
            )

        self.after(
            30,
            self.update_detection
        )
    def select_recorded_video(self):

        video_path = filedialog.askopenfilename(
            title="Select Recorded Video",
            filetypes=[
                (
                    "Video Files",
                    "*.mp4 *.avi *.mov *.mkv"
                ),
                (
                    "All Files",
                    "*.*"
                )
            ]
        )

        if not video_path:

            return

        print(
            f"🎥 Selected video:\n{video_path}"
        )

        # Start detection using selected video

        self.engine.start(
            video_path
        )    
    def select_recorded_video(self):

        video_path = filedialog.askopenfilename(
            title="Select Recorded Video",
            filetypes=[
                (
                    "Video Files",
                    "*.mp4 *.avi *.mov *.mkv"
                ),
                (
                    "All Files",
                    "*.*"
                )
            ]
        )

        if not video_path:

            return

        print(
            f"🎥 Selected video:\n{video_path}"
        )

        self.engine.start(
            video_path
        )    
    def start_live_camera(self):

        print(
            "🎥 Switching to live camera"
        )

        self.engine.start(
            0
        )    