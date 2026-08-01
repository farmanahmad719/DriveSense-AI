import customtkinter as ctk


class SmallMetricsRow(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(
            parent,
            fg_color="transparent",
            height=80
        )

        for i in range(4):
            self.grid_columnconfigure(
                i,
                weight=1
            )

        metrics = [
            ("😴 Yawn", "03"),
            ("🎯 Head Pose", "Forward"),
            ("⚡ FPS", "30"),
            ("📷 Camera", "Online")
        ]

        self.value_labels = []

        for i, (title, value) in enumerate(metrics):

            card = ctk.CTkFrame(
                self,
                corner_radius=18,
                fg_color="#1B2433"
            )

            card.grid(
                row=0,
                column=i,
                sticky="nsew",
                padx=8
            )

            ctk.CTkLabel(
                card,
                text=title,
                font=("Segoe UI", 14, "bold")
            ).pack(
                pady=(9, 1)
            )

            value_label = ctk.CTkLabel(
                card,
                text=value,
                font=("Segoe UI", 20)
            )

            value_label.pack(
                pady=(0, 9)
            )

            self.value_labels.append(value_label)

    def update_values(
        self,
        yawn_count,
        head_pose,
        fps,
        camera_status
    ):

        self.value_labels[0].configure(
            text=str(yawn_count)
        )

        self.value_labels[1].configure(
            text=head_pose
        )

        self.value_labels[2].configure(
            text=str(fps)
        )

        self.value_labels[3].configure(
            text=camera_status
        )