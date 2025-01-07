import pygame
from src.config.global_config import FEATURE_COLOR, FEATURE_FONT
from src.core.scene import Scene
from src.events.event_handler import Events
from src.utils.utils import Draw


class NaughtyScreen:
    def __init__(self):
        self.scene = Scene()
        self.draw = Draw()
        self.game_state = "Naughty"

    # text for when health has been depleted and player is put on naughty list
    @staticmethod
    def naughty_text():
        naughty_text = ("\nYou've run out of health!\n\n"
                        "Santa and his friends have been hurt.\n\n"
                        "You are now on Santa's\n"
                        "NAUGHTY LIST!\n\n"
                        )
        menu_options = "Press C to Continue"

        return naughty_text, menu_options

    def naughty_screen(self, game_over, game):
        print("Health depleted...player is now on the naughty list!")
        self.scene.draw_main_scene()
        naughty_text, menu_options = self.naughty_text()
        self.draw.draw_text(naughty_text, FEATURE_FONT, FEATURE_COLOR, 230)
        self.draw.draw_menu_options(menu_options)
        pygame.display.update()
        Events.event_handler(self.game_state, game_over, game)


if __name__ == '__main__':
    pass
