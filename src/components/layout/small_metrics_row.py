import customtkinter as ctk


class SmallMetricsRow(ctk.CTkFrame):

    def __init__(self,parent):

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


        metrics=[
            ("😴 Yawn","03"),
            ("🎯 Head Pose","Forward"),
            ("⚡ FPS","30"),
            ("📷 Camera","Online")
        ]


        for i,(title,value) in enumerate(metrics):

            card=ctk.CTkFrame(
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
                font=("Segoe UI",14,"bold")
            ).pack(pady=(12,5))


            ctk.CTkLabel(
                card,
                text=value,
                font=("Segoe UI",20)
            ).pack(pady=5)