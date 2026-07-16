import customtkinter as ctk

from theme import *


class SettingsPage(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(
            parent,
            fg_color="transparent"
        )

        # ================= LAYOUT =================

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=0)

        # ====================================================
        # CAMERA SETTINGS
        # ====================================================

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
            font=("Segoe UI", 18, "bold")
        ).pack(
            anchor="w",
            padx=20,
            pady=(20, 25)
        )

        # ====================================================
        # EAR
        # ====================================================

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

        buttons = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        buttons.grid(
            row=1,
            column=0,
            columnspan=2,
            pady=(10, 20)
        )

        ctk.CTkButton(
            buttons,
            text="💾 Save Settings",
            width=190,
            height=42,
            corner_radius=12,
            hover_color=BLUE,
            font=("Segoe UI", 14, "bold"),
            command=self.save_settings
        ).pack(
            side="left",
            padx=10
        )

        ctk.CTkButton(
            buttons,
            text="↺ Restore Defaults",
            width=190,
            height=42,
            corner_radius=12,
            hover_color=BLUE,
            font=("Segoe UI", 14, "bold"),
            command=self.restore_defaults
        ).pack(
            side="left",
            padx=10
        )

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
        )