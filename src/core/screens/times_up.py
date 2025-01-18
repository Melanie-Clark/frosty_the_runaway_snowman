import pygame
from src.config.global_config import FEATURE_COLOR, GAME_TEXT_FONT, SCREEN_HEIGHT


# screen for when time has run out (0 seconds)
class TimesUpScreen:
    def __init__(self, screen, game_state, scene, draw):
        self.screen = screen
        self.game_state_manager = game_state
        self.scene = scene
        self.draw = draw

    @staticmethod
    def times_up_text():
        times_up = "Times Up!"
        return times_up

    def draw_times_up_screen(self):
        print("Times Up!")
        self.scene.draw_main_scene()
        times_up = self.times_up_text()
        self.draw.draw_text(times_up, GAME_TEXT_FONT, FEATURE_COLOR, SCREEN_HEIGHT // 2)
        pygame.display.update()
        pygame.time.delay(1000)

    def run(self):
        self.draw_times_up_screen()
        self.game_state_manager.set_state("game_over")


if __name__ == "__main__":
    pass
