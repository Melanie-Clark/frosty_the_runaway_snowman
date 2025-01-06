import pygame
from src.config.global_config import INSTRUCTIONS_COLOR, INSTRUCTIONS_FONT
from src.events.event_handler import Movement
from src.utils.utils import Frosty, Draw


class WelcomeScreen:
    def __init__(self, scene):
        self.scene = scene
        self.target = Frosty()
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

    # draws everything required for welcome screen
    def draw_welcome_screen(self, game):
        self.scene.draw_scene()
        self.draw.draw_title(self.title)
        self.target.draw_frosty(200)
        self.draw.draw_text(self.welcome_text, INSTRUCTIONS_FONT, INSTRUCTIONS_COLOR, 230)
        self.draw.draw_menu_options()
        pygame.display.update()
        self.welcome_screen_event_handler(game)

    # Event handling for starting game
    @staticmethod
    def welcome_screen_event_handler(game):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Movement.quit_game()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        game.game_loop()
                    elif event.key == pygame.K_q:
                        Movement.quit_game()


if __name__ == '__main__':
    pass
