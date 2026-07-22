import json
import os


class SettingsManager:

    DEFAULT_SETTINGS = {
        "alarm_enabled": True,
        "alarm_volume": 0.7,
        "screenshot_enabled": True,
        "camera_id": 0,

        "ear_threshold": 0.25,
        "mar_threshold": 0.70,
    }

    def __init__(self):

        self.settings_path = "data/settings.json"

        self.settings = self.DEFAULT_SETTINGS.copy()

        self.load()

    # =========================================

    def load(self):

        if not os.path.exists(self.settings_path):

            self.save()

            return

        try:

            with open(
                self.settings_path,
                "r"
            ) as file:

                saved_settings = json.load(file)

                self.settings.update(
                    saved_settings
                )

        except Exception as error:

            print(
                f"Settings load error: {error}"
            )

    # =========================================

    def save(self):

        os.makedirs(
            "data",
            exist_ok=True
        )

        with open(
            self.settings_path,
            "w"
        ) as file:

            json.dump(
                self.settings,
                file,
                indent=4
            )

    # =========================================

    def get(self, key):

        return self.settings.get(
            key
        )

    # =========================================

    def set(self, key, value):

        self.settings[key] = value

        self.save()