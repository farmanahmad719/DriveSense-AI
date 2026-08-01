import pygame


class AlarmManager:

    def __init__(
        self,
        sound_file="assets/alarm.wav",
        settings_manager=None
    ):

        pygame.mixer.init()

        self.sound = pygame.mixer.Sound(
            sound_file
        )

        self.is_playing = False

        self.settings_manager = (
            settings_manager
        )

        # Apply saved volume
        self.update_volume()

        print(
            "AlarmManager initialized."
        )

    # =========================================
    # UPDATE VOLUME
    # =========================================

    def update_volume(self):

        if self.settings_manager is None:

            return

        volume = self.settings_manager.get(
            "alarm_volume"
        )

        if volume is not None:

            self.sound.set_volume(
                float(volume)
            )

    # =========================================
    # PLAY ALARM
    # =========================================

    def play_alarm(self):

        # Check whether alarm is enabled
        if self.settings_manager is not None:

            alarm_enabled = (
                self.settings_manager.get(
                    "alarm_enabled"
                )
            )

            if not alarm_enabled:

                return

            self.update_volume()

        if not self.is_playing:

            self.sound.play(
                loops=-1
            )

            self.is_playing = True

    # =========================================
    # STOP ALARM
    # =========================================

    def stop_alarm(self):

        if self.is_playing:

            self.sound.stop()

            self.is_playing = False