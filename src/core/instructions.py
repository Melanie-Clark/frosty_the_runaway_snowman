import pygame
from src.config.global_config import INSTRUCTIONS_COLOR, INSTRUCTIONS_FONT
from src.core.scene import Scene
from src.utils.utils import Draw


class InstructionScreen:
    def __init__(self):
        self.scene = Scene()
        self.draw = Draw()
        self.title = "Instructions"
        self.instruction_text = ("The aim of the game is to throw snowballs at Frosty the runaway snowman.\n\n"
                                 "Score as many hits as you can before the time runs out.\n\n"
                                 "But be careful...\n"
                                 "...each time you hit Frosty, he gets faster!\n\n"
                                 "Watch out!\n"
                                 "Santa and his friends reduces heart health.\n\n"
                                 "Use the LEFT/RIGHT arrow keys to move the snowball\n"
                                 "at the bottom of the screen.\n\n"
                                 "Press SPACEBAR to throw the snowball.\n\n")

    # draws everything required for welcome screen
    def draw_instruction_screen(self):
        self.scene.draw_main_scene()
        self.draw.draw_title(self.title)
        self.scene.draw_frosty(200)
        self.draw.draw_text(self.instruction_text, INSTRUCTIONS_FONT, INSTRUCTIONS_COLOR, 230)
        self.draw.draw_menu_options()
        pygame.display.update()


if __name__ == '__main__':
    pass
