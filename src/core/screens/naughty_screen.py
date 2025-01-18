import pygame
from src.config.global_config import FEATURE_COLOR, GAME_TEXT_FONT


class NaughtyScreen:
    def __init__(self, screen, game_state, scene, draw):
        self.screen = screen
        self.game_state_manager = game_state
        self.scene = scene
        self.draw = draw

    # text for when health has been depleted and player is put on naughty list
    @staticmethod
    def naughty_text():
        title = "Naughty Naughty!"
        naughty_text = (
            "Santa and his friends are hurt.\n\n"
            "They can't deliver any presents.\n"
            "Children are crying!\n\n"
            "You've been put on the\n"
            "NAUGHTY LIST!\n\n"
        )
        menu_options = "Press [RETURN] to continue"

        return title, naughty_text, menu_options

    def draw_naughty_screen(self):
        print("Health depleted...player is now on the naughty list!")
        self.scene.draw_main_scene()
        title, naughty_text, menu_options = self.naughty_text()
        self.draw.draw_title(title)
        self.draw.draw_text(naughty_text, GAME_TEXT_FONT, FEATURE_COLOR, 230)
        self.draw.draw_menu_options(menu_options)
        pygame.display.update()

    def run(self):
        self.draw_naughty_screen()


if __name__ == "__main__":
    pass
