import pygame


class Sound:
    @staticmethod
    def sound_effect(sound_effect):
        ouch_sfx = pygame.mixer.Sound(sound_effect)
        ouch_sfx.play()

    @staticmethod
    def music():
        pygame.mixer.music.load("../assets/sounds/snowtime_soundtrack.mp3")
        pygame.mixer.music.play(-1)  # -1 loops infinitely.
