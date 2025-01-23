import pygame
from src.config.global_config import INSTRUCTIONS_FONT, MENU_COLOR, SCREEN_WIDTH, SCREEN_HEIGHT
from src.screens.base_screen import BaseScreen


class InstructionScreen(BaseScreen):
    def __init__(self, screen, game_state_manager, scene, draw):
        super().__init__(screen, game_state_manager)
        self.scene = scene
        self.draw = draw

        self.title = "Instructions"
        self.instruction_text = ("The aim of the game is to hurl as many snowballs at\n"
                                 "Frosty the runaway snowman before the time runs out.\n\n"
                                 "But be careful...each time you hit Frosty, he gets faster!\n"
                                 "But hit Frosty 10 times for an extra Time Bonus!\n\n"
                                 "Watch out...Santa and his friends reduces your health!\n\n"
                                 "Use the LEFT/RIGHT arrow keys to move the\n"
                                 "snowball at the bottom of the screen.\n\n"
                                 "Press SPACEBAR to throw the snowball.\n\n"
                                 )

    # draws everything required for welcome screen
    def draw_instruction_screen(self):
        self.scene.draw_main_scene()
        self.draw.draw_title(self.title)
        self.scene.draw_frosty(SCREEN_WIDTH // 6.4)
        self.scene.draw_snow()
        self.draw.draw_text(self.instruction_text, INSTRUCTIONS_FONT, MENU_COLOR, SCREEN_HEIGHT // 3.3)
        self.draw.draw_menu_options()
        pygame.display.update()

    def run(self):
        self.draw_instruction_screen()


if __name__ == '__main__':
    pass
