import customtkinter as ctk

from theme import *


class SettingsPage(ctk.CTkFrame):

    def __init__(
        self,
        parent,
        settings_manager
    ):

        super().__init__(
            parent,
            fg_color="transparent"
        )

        self.settings_manager = settings_manager

        # =========================================
        # MAIN GRID
        # =========================================

        self.grid_columnconfigure(
            (0, 1),
            weight=1
        )

        self.grid_rowconfigure(
            0,
            weight=1
        )

        self.grid_rowconfigure(
            1,
            weight=0
        )

        # =========================================
        # CAMERA SETTINGS
        # =========================================

        camera = ctk.CTkFrame(
            self,
            fg_color=CARD,
            corner_radius=18
        )

        camera.grid(
            row=0,
            column=0,
            padx=10,
            pady=10,
            sticky="nsew"
        )

        ctk.CTkLabel(
            camera,
            text="📷 Camera Settings",
            font=("Segoe UI", 16, "bold")
        ).pack(
            anchor="w",
            padx=20,
            pady=(15, 20)
        )

        ctk.CTkLabel(
            camera,
            text="Camera ID"
        ).pack(
            anchor="w",
            padx=20
        )

        self.camera_entry = ctk.CTkEntry(
            camera
        )

        self.camera_entry.pack(
            fill="x",
            padx=20,
            pady=(5, 15)
        )

        self.camera_entry.insert(
            0,
            str(
                self.settings_manager.get(
                    "camera_id"
                )
            )
        )
        ctk.CTkLabel(
            camera,
            text="FPS"
        ).pack(
            anchor="w",
            padx=20
        )

        self.fps_entry = ctk.CTkEntry(
            camera
        )

        self.fps_entry.pack(
            fill="x",
            padx=20,
            pady=(5, 20)
        )

        self.fps_entry.insert(
            0,
            "30"
        )

        # =========================================
        # DETECTION SETTINGS
        # =========================================

        detection = ctk.CTkFrame(
            self,
            fg_color=CARD,
            corner_radius=18
        )

        detection.grid(
            row=0,
            column=1,
            padx=10,
            pady=10,
            sticky="nsew"
        )

        ctk.CTkLabel(
            detection,
            text="🎯 Detection Thresholds",
            font=("Segoe UI", 16, "bold")
        ).pack(
            anchor="w",
            padx=20,
            pady=(15, 20)
        )

        settings = [
            "EAR Threshold",
            "MAR Threshold",
            "Head Pose"
        ]

        self.threshold_entries = {}

        for item in settings:

            ctk.CTkLabel(
                detection,
                text=item
            ).pack(
                anchor="w",
                padx=20
            )

            entry = ctk.CTkEntry(
                detection
            )

            entry.pack(
                fill="x",
                padx=20,
                pady=(5, 15)
            )

            self.threshold_entries[item] = entry
            

        # =========================================
        # ALERT SETTINGS
        # =========================================

        alert_settings = ctk.CTkFrame(
            self,
            fg_color=CARD,
            corner_radius=18
        )

        alert_settings.grid(
            row=1,
            column=0,
            columnspan=2,
            padx=10,
            pady=10,
            sticky="ew"
        )

        ctk.CTkLabel(
            alert_settings,
            text="🚨 Alert Settings",
            font=("Segoe UI", 16, "bold")
        ).grid(
            row=0,
            column=0,
            columnspan=2,
            sticky="w",
            padx=20,
            pady=(15, 20)
        )

        # =========================================
        # ALARM SWITCH
        # =========================================

        self.alarm_switch = ctk.CTkSwitch(
            alert_settings,
            text="🔊 Enable Alarm",
            command=self.toggle_alarm
        )

        self.alarm_switch.grid(
            row=1,
            column=0,
            padx=20,
            pady=10,
            sticky="w"
        )

        if self.settings_manager.get(
            "alarm_enabled"
        ):

            self.alarm_switch.select()

        else:

            self.alarm_switch.deselect()

        # =========================================
        # SCREENSHOT SWITCH
        # =========================================

        self.screenshot_switch = ctk.CTkSwitch(
            alert_settings,
            text="📸 Capture Alert Screenshots",
            command=self.toggle_screenshot
        )

        self.screenshot_switch.grid(
            row=2,
            column=0,
            padx=20,
            pady=(10, 20),
            sticky="w"
        )

        if self.settings_manager.get(
            "screenshot_enabled"
        ):

            self.screenshot_switch.select()

        else:

            self.screenshot_switch.deselect()

        # =========================================
        # VOLUME
        # =========================================

        ctk.CTkLabel(
            alert_settings,
            text="🔉 Alarm Volume"
        ).grid(
            row=1,
            column=1,
            padx=20,
            pady=(10, 0),
            sticky="w"
        )

        self.volume_slider = ctk.CTkSlider(
            alert_settings,
            from_=0,
            to=1,
            command=self.change_volume
        )

        self.volume_slider.grid(
            row=2,
            column=1,
            padx=20,
            pady=(0, 20),
            sticky="ew"
        )

        alert_settings.grid_columnconfigure(
            1,
            weight=1
        )

        self.volume_slider.set(
            self.settings_manager.get(
                "alarm_volume"
            )
        )

        # =========================================
        # ACTION BUTTONS
        # =========================================

        buttons = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        buttons.grid(
            row=3,
            column=0,
            columnspan=2,
            pady=20
        )

        ctk.CTkButton(
            buttons,
            text="💾 Save Settings",
            width=180,
            hover_color=BLUE,
            command=self.save_settings
        ).pack(
            side="left",
            padx=10
        )

        ctk.CTkButton(
            buttons,
            text="↺ Restore Defaults",
            width=180,
            hover_color=BLUE,
            command=self.restore_defaults
        ).pack(
            side="left",
            padx=10
        )

    # =========================================
    # ALARM
    # =========================================

    def toggle_alarm(self):

        enabled = (
            self.alarm_switch.get() == 1
        )

        self.settings_manager.set(
            "alarm_enabled",
            enabled
        )

    # =========================================
    # VOLUME
    # =========================================

    def change_volume(
        self,
        value
    ):

        self.settings_manager.set(
            "alarm_volume",
            float(value)
        )

    # =========================================
    # SCREENSHOTS
    # =========================================

    def toggle_screenshot(self):

        enabled = (
            self.screenshot_switch.get() == 1
        )

        self.settings_manager.set(
            "screenshot_enabled",
            enabled
        )

    # =========================================
    # SAVE
    # =========================================

    def save_settings(self):

        try:

            camera_id = int(
                self.camera_entry.get()
            )

            self.settings_manager.set(
                "camera_id",
                camera_id
            )

            print(
                "Camera settings saved."
            )

        except ValueError:

            print(
                "Camera ID must be a number."
            )
    # =========================================
    # RESTORE DEFAULTS
    # =========================================

    def restore_defaults(self):

        self.settings_manager.set(
            "alarm_enabled",
            True
        )

        self.settings_manager.set(
            "alarm_volume",
            0.7
        )

        self.settings_manager.set(
            "screenshot_enabled",
            True
        )

        self.alarm_switch.select()

        self.screenshot_switch.select()

        self.volume_slider.set(
            0.7
        )

        print(
            "Settings restored."
        )