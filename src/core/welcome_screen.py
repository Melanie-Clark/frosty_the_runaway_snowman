import pygame
from src.config.global_config import INSTRUCTIONS_COLOR, INSTRUCTIONS_FONT
from src.events.event_handler import Events
from src.utils.utils import Draw


class WelcomeScreen:
    def __init__(self, scene):
        self.scene = scene
        self.draw = Draw()
        self.title = "Frosty: The runaway snowman!"
        self.welcome_text = ("The aim of the game is to throw snowballs at Frosty the runaway snowman.\n\n"
                             "Score as many hits as you can before the time runs out.\n\n"
                             "But be careful...\n"
                             "...each time you hit Frosty, he gets faster!\n\n"
                             "Watch out!\n"
                             "Santa and his friends reduces heart health.\n\n"
                             "Use the LEFT/RIGHT arrow keys to move the snowball\n"
                             "at the bottom of the screen.\n\n"
                             "Press SPACEBAR to throw the snowball.\n\n")
        self.game_state = "Welcome"

    # draws everything required for welcome screen
    def draw_welcome_screen(self, game):
        self.scene.draw_main_scene()
        self.draw.draw_title(self.title)
        self.scene.draw_frosty(200)
        self.draw.draw_text(self.welcome_text, INSTRUCTIONS_FONT, INSTRUCTIONS_COLOR, 230)
        self.draw.draw_menu_options()
        pygame.display.update()
        Events.event_handler(self.game_state, game, None)


if __name__ == '__main__':
    pass
