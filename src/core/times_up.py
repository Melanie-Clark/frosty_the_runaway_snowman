import pygame
from src.config.global_config import FEATURE_COLOR, GAME_TEXT_FONT, TIMES_UP_SCREEN, WINDOW_HEIGHT, GAME_OVER_SCREEN
from src.core.scene import Scene
from src.utils.utils import Draw


# screen for when time has run out (0 seconds)
class TimesUpScreen:
    def __init__(self):
        self.scene = Scene()
        self.draw = Draw()
        self.game_state = TIMES_UP_SCREEN

    @staticmethod
    def times_up_text():
        times_up = "Times Up!"
        return times_up

    def draw_times_up_screen(self):
        print("Times Up!")
        self.scene.draw_main_scene()
        times_up = self.times_up_text()
        self.draw.draw_text(times_up, GAME_TEXT_FONT, FEATURE_COLOR, WINDOW_HEIGHT // 2)
        pygame.display.update()
        pygame.time.delay(1000)


if __name__ == "__main__":
    pass
