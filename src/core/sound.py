import pygame


class Sound:
    @staticmethod
    def sound_effect(sound_effect):
        ouch_sfx = pygame.mixer.Sound(sound_effect)
        ouch_sfx.play()
