import customtkinter as ctk

from theme import *


class DetectionCard(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(
            parent,
            fg_color=CARD,
            corner_radius=18,
            height=180
        )

        self.pack_propagate(False)

        # ---------------- Title ----------------

        ctk.CTkLabel(
            self,
            text="🤖 AI Detection",
            font=("Segoe UI", 14, "bold")
        ).pack(
            pady=7
        )

        # ---------------- Detection Labels ----------------

        self.face_label = self.create_detection_label(
            "Face"
        )

        self.eyes_label = self.create_detection_label(
            "Eyes"
        )

        self.phone_label = self.create_detection_label(
            "Phone"
        )

        self.head_label = self.create_detection_label(
            "Head"
        )

    # =======================================

    def create_detection_label(self, name):

        label = ctk.CTkLabel(
            self,
            text=f"❌ {name}",
            anchor="w"
        )

        label.pack(
            anchor="w",
            padx=18,
            pady=3
        )

        return label

    # =======================================

    def update_data(self, result):

        print(
            "DetectionCard:",
            "face_detected =", result.face_detected,
            "is_drowsy =", result.is_drowsy,
            "direction =", result.direction
        )

        # ---------------- Face ----------------

        if result.face_detected:

            self.face_label.configure(
                text="✅ Face"
            )

        else:

            self.face_label.configure(
                text="❌ Face"
            )

        # ---------------- Eyes ----------------

        if result.is_drowsy:

            self.eyes_label.configure(
                text="❌ Eyes"
            )

        else:

            self.eyes_label.configure(
                text="✅ Eyes"
            )

        # ---------------- Phone ----------------

        self.phone_label.configure(
            text="❌ Phone"
        )

        # ---------------- Head ----------------

        if result.direction == "FORWARD":

            self.head_label.configure(
                text="✅ Head"
            )

        else:

            self.head_label.configure(
                text="⚠️ Head"
            )       