import pygame
from src.config.global_config import FEATURE_COLOR, SCREEN_HEIGHT, INSTRUCTIONS_FONT
from src.screens.base_screen import BaseScreen


class Reload(BaseScreen):
    def __init__(self, screen, game_state_manager, scene, draw):
        super().__init__(screen, game_state_manager)
        self.scene = scene
        self.draw = draw
        self.title = "Frosty: The Runaway Snowman!"

    def draw_text(self):
        text = ("Manually close the browser to quit\n"
                "or Press RETURN to go back to the main menu")
        self.draw.draw_text(text, INSTRUCTIONS_FONT, FEATURE_COLOR, SCREEN_HEIGHT // 2)

    # draws everything required for menu screen
    def draw_screen(self):
        self.scene.draw_main_scene()
        self.scene.draw_frosty(200)
        self.draw.draw_title(self.title)
        self.draw_text()
        pygame.display.update()

    def run(self):
        self.draw_screen()


if __name__ == "__main__":
    pass
