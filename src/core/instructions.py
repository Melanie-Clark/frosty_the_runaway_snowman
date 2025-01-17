import pygame
from src.config.global_config import INSTRUCTIONS_FONT, MENU_COLOR
from src.core.scene import Scene
from src.utils.utils import Draw


class InstructionScreen:
    def __init__(self):
        self.scene = Scene()
        self.draw = Draw()
        self.title = "Instructions"
        self.instruction_text = ("FROSTY HAS RUN AWAY!\n\n"
                                 "The aim of the game is to hurl as many snowballs.\n"
                                 "at Frosty before the time runs out.\n\n"
                                 "But be careful...each time you hit Frosty, he gets faster!\n"
                                 "Watch out...Santa and his friends reduces your health!\n\n"
                                 "Use the LEFT/RIGHT arrow keys to move the\n"
                                 "snowball at the bottom of the screen.\n\n"
                                 "Press SPACEBAR to throw the snowball.\n\n"
                                 )

    # draws everything required for welcome screen
    def draw_instruction_screen(self):
        self.scene.draw_main_scene()
        self.draw.draw_title(self.title)
        self.scene.draw_frosty(200)
        self.scene.draw_snow()
        self.draw.draw_text(self.instruction_text, INSTRUCTIONS_FONT, MENU_COLOR, 220)
        self.draw.draw_menu_options()
        pygame.display.update()


if __name__ == '__main__':
    pass
