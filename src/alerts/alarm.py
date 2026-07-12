import pygame


class AlarmManager:

    def __init__(self, sound_file="assets/alarm.wav"):

        pygame.mixer.init()

        self.sound = pygame.mixer.Sound(sound_file)
        self.is_playing = False

        print("AlarmManager initialized.")

    def play_alarm(self):

        if not self.is_playing:
            self.sound.play(-1)
            self.is_playing = True

    def stop_alarm(self):

        if self.is_playing:
            self.sound.stop()
            self.is_playing = False