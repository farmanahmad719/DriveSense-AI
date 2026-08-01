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

<<<<<<< HEAD
        # ================= LAYOUT =================

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=0)

        # ====================================================
        # CAMERA SETTINGS
        # ====================================================
=======
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
>>>>>>> 151acb891a5b5ca9cf0a51ae8c9855e06d790cdd

        camera = ctk.CTkFrame(
            self,
            fg_color=CARD,
            corner_radius=18
        )

        camera.grid(
            row=0,
            column=0,
            padx=(0, 10),
            pady=10,
            sticky="nsew"
        )

        ctk.CTkLabel(
            camera,
            text="📷 Camera Settings",
<<<<<<< HEAD
            font=("Segoe UI", 18, "bold")
        ).pack(
            anchor="w",
            padx=20,
            pady=(20, 25)
        )

        # ---------------- Camera ID ----------------

        ctk.CTkLabel(
            camera,
            text="Camera Source",
            font=("Segoe UI", 13)
        ).pack(
            anchor="w",
            padx=20
        )

        self.camera_id = ctk.CTkComboBox(
            camera,
            values=["Camera 0", "Camera 1", "Camera 2"],
            height=38
        )

        self.camera_id.pack(
            fill="x",
            padx=20,
            pady=(6, 20)
        )

        self.camera_id.set("Camera 0")

        # ---------------- Resolution ----------------

        ctk.CTkLabel(
            camera,
            text="Resolution",
            font=("Segoe UI", 13)
        ).pack(
            anchor="w",
            padx=20
        )

        self.resolution = ctk.CTkComboBox(
            camera,
            values=[
                "640 × 480",
                "1280 × 720",
                "1920 × 1080"
            ],
            height=38
        )

        self.resolution.pack(
            fill="x",
            padx=20,
            pady=(6, 20)
        )

        self.resolution.set("640 × 480")

        # ---------------- FPS ----------------

        ctk.CTkLabel(
            camera,
            text="Frame Rate",
            font=("Segoe UI", 13)
        ).pack(
            anchor="w",
            padx=20
        )

        self.fps = ctk.CTkComboBox(
            camera,
            values=[
                "15 FPS",
                "24 FPS",
                "30 FPS",
                "60 FPS"
            ],
            height=38
        )

        self.fps.pack(
            fill="x",
            padx=20,
            pady=(6, 20)
        )

        self.fps.set("30 FPS")

        # ====================================================
        # DETECTION SETTINGS
        # ====================================================
=======
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
>>>>>>> 151acb891a5b5ca9cf0a51ae8c9855e06d790cdd

        detection = ctk.CTkFrame(
            self,
            fg_color=CARD,
            corner_radius=18
        )

        detection.grid(
            row=0,
            column=1,
            padx=(10, 0),
            pady=10,
            sticky="nsew"
        )

        ctk.CTkLabel(
            detection,
            text="🎯 Detection Thresholds",
<<<<<<< HEAD
            font=("Segoe UI", 18, "bold")
        ).pack(
            anchor="w",
            padx=20,
            pady=(20, 25)
=======
            font=("Segoe UI", 16, "bold")
        ).pack(
            anchor="w",
            padx=20,
            pady=(15, 20)
>>>>>>> 151acb891a5b5ca9cf0a51ae8c9855e06d790cdd
        )

        # ====================================================
        # EAR
        # ====================================================

<<<<<<< HEAD
        ctk.CTkLabel(
            detection,
            text="EAR Threshold",
            font=("Segoe UI", 13)
        ).pack(
            anchor="w",
            padx=20
        )

        self.ear_value = ctk.CTkLabel(
            detection,
            text="0.25",
            font=("Segoe UI", 13, "bold")
        )

        self.ear_value.pack(
            anchor="e",
            padx=20
        )

        self.ear_slider = ctk.CTkSlider(
            detection,
            from_=0.10,
            to=0.50,
            number_of_steps=40,
            command=self.update_ear
        )

        self.ear_slider.pack(
            fill="x",
            padx=20,
            pady=(5, 20)
        )

        self.ear_slider.set(0.25)

        # ====================================================
        # MAR
        # ====================================================

        ctk.CTkLabel(
            detection,
            text="MAR Threshold",
            font=("Segoe UI", 13)
        ).pack(
            anchor="w",
            padx=20
        )

        self.mar_value = ctk.CTkLabel(
            detection,
            text="0.60",
            font=("Segoe UI", 13, "bold")
        )

        self.mar_value.pack(
            anchor="e",
            padx=20
        )

        self.mar_slider = ctk.CTkSlider(
            detection,
            from_=0.20,
            to=1.00,
            number_of_steps=80,
            command=self.update_mar
        )

        self.mar_slider.pack(
            fill="x",
            padx=20,
            pady=(5, 20)
        )

        self.mar_slider.set(0.60)

        # ====================================================
        # HEAD POSE
        # ====================================================

        ctk.CTkLabel(
            detection,
            text="Head Pose Sensitivity",
            font=("Segoe UI", 13)
        ).pack(
            anchor="w",
            padx=20
        )

        self.head_pose_value = ctk.CTkLabel(
            detection,
            text="50",
            font=("Segoe UI", 13, "bold")
        )

        self.head_pose_value.pack(
            anchor="e",
            padx=20
        )

        self.head_pose_slider = ctk.CTkSlider(
            detection,
            from_=0,
            to=100,
            number_of_steps=100,
            command=self.update_head_pose
        )

        self.head_pose_slider.pack(
            fill="x",
            padx=20,
            pady=(5, 20)
        )

        self.head_pose_slider.set(50)

        # ====================================================
        # BUTTONS
        # ====================================================
=======
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
>>>>>>> 151acb891a5b5ca9cf0a51ae8c9855e06d790cdd

        buttons = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        buttons.grid(
            row=3,
            column=0,
            columnspan=2,
            pady=(10, 20)
        )

        ctk.CTkButton(
            buttons,
            text="💾 Save Settings",
<<<<<<< HEAD
            width=190,
            height=42,
            corner_radius=12,
            hover_color=BLUE,
            font=("Segoe UI", 14, "bold"),
=======
            width=180,
            hover_color=BLUE,
>>>>>>> 151acb891a5b5ca9cf0a51ae8c9855e06d790cdd
            command=self.save_settings
        ).pack(
            side="left",
            padx=10
        )

        ctk.CTkButton(
            buttons,
            text="↺ Restore Defaults",
<<<<<<< HEAD
            width=190,
            height=42,
            corner_radius=12,
            hover_color=BLUE,
            font=("Segoe UI", 14, "bold"),
=======
            width=180,
            hover_color=BLUE,
>>>>>>> 151acb891a5b5ca9cf0a51ae8c9855e06d790cdd
            command=self.restore_defaults
        ).pack(
            side="left",
            padx=10
        )

<<<<<<< HEAD
    # ====================================================
    # SLIDER UPDATES
    # ====================================================

    def update_ear(self, value):

        self.ear_value.configure(
            text=f"{float(value):.2f}"
        )

    def update_mar(self, value):

        self.mar_value.configure(
            text=f"{float(value):.2f}"
        )

    def update_head_pose(self, value):

        self.head_pose_value.configure(
            text=f"{int(float(value))}"
        )

    # ====================================================
    # SAVE SETTINGS
    # ====================================================

    def save_settings(self):

        print("Settings saved.")

        print(
            "Camera:",
            self.camera_id.get()
        )

        print(
            "Resolution:",
            self.resolution.get()
        )

        print(
            "FPS:",
            self.fps.get()
        )

        print(
            "EAR:",
            self.ear_slider.get()
        )

        print(
            "MAR:",
            self.mar_slider.get()
        )

        print(
            "Head Pose:",
            self.head_pose_slider.get()
        )

    # ====================================================
    # RESTORE DEFAULTS
    # ====================================================

    def restore_defaults(self):

        self.camera_id.set("Camera 0")

        self.resolution.set("640 × 480")

        self.fps.set("30 FPS")

        self.ear_slider.set(0.25)

        self.mar_slider.set(0.60)

        self.head_pose_slider.set(50)

        self.ear_value.configure(
            text="0.25"
        )

        self.mar_value.configure(
            text="0.60"
        )

        self.head_pose_value.configure(
            text="50"
=======
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
>>>>>>> 151acb891a5b5ca9cf0a51ae8c9855e06d790cdd
        )