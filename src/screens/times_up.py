import os
import pygame
from src.config.global_config import FEATURE_COLOR, GAME_TEXT_FONT, SCREEN_HEIGHT
from src.screens.base_screen import BaseScreen


# screen for when time has run out (0 seconds)
class TimesUpScreen(BaseScreen):
    def __init__(self, screen, game_state_manager, scene, draw):
        super().__init__(screen, game_state_manager)
        self.scene = scene
        self.draw = draw

    def draw_times_up_screen(self):
        # if play in browser, bypasses Times Up screen due to delay issue
        if "PYGBAG" in os.environ:
            self.game_state_manager.set_state("game_over")
        else:
            text = "Times Up!"
            print(text)
            self.scene.draw_main_scene()
            self.draw.draw_text(text, GAME_TEXT_FONT, FEATURE_COLOR, SCREEN_HEIGHT // 2)
            pygame.display.update()
            pygame.time.delay(1000)

    def run(self):
        self.draw_times_up_screen()
        self.game_state_manager.set_state("game_over")


if __name__ == "__main__":
    pass
