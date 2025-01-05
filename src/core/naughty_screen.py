import pygame
from src.config.global_config import FEATURE_COLOR, FEATURE_FONT
from src.core.scene import Scene
from src.utils.utils import Draw


class NaughtyScreen:
    # text for when health has been depleted and player is put on naughty list
    @staticmethod
    def naughty_text():
        naughty_text = ("\nYou've run out of health!\n\n"
                        "Santa and his friends have been hurt.\n\n"
                        "You are now on Santa's\n"
                        "NAUGHTY LIST!")
        return naughty_text

    def naughty_screen(self):
        print("Health depleted...player now on naughty list!")
        Scene().draw_scene()

        naughty_text = self.naughty_text()
        Draw().draw_text(naughty_text, FEATURE_FONT, FEATURE_COLOR, 250)
        pygame.display.update()
        pygame.time.delay(5000)


if __name__ == '__main__':
    pass
