import pygame
from src.config.global_config import INSTRUCTIONS_COLOR, INSTRUCTIONS_FONT
from src.events.event_handler import Movement
from src.utils.utils import Frosty, Draw


class WelcomeScreen:
    def __init__(self, scene):
        self.scene = scene
        self.frosty = Frosty()
        self.draw = Draw()
        self.title = "Frosty: The runaway snowman!"
        self.welcome_text = ("The aim of the game is to throw snowballs\n"
                             "at Frosty the runaway snowman.\n\n"
                             "Score as many hits\n"
                             "as you can before the time runs out.\n\n"
                             "But be careful...\n"
                             "...each time you hit Frosty, he gets faster!\n\n"
                             "Hurting Santa or his friends will cost you\n"
                             "heart health — so aim wisely!\n\n"
                             "Use the left/right arrow keys to move\n"
                             "the snowball at the bottom of the screen.\n"
                             "Press SPACEBAR to throw the snowball.\n\n"
                             "Press P to Play or Q to Quit")

    # draws everything required for welcome screen
    def draw_welcome_screen(self, game):
        self.scene.draw_scene()
        self.draw.draw_title(self.title)
        self.frosty.draw_frosty(200)
        # self.draw_welcome_text(230)
        self.draw.draw_text(self.welcome_text, INSTRUCTIONS_FONT, INSTRUCTIONS_COLOR, 230)
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
