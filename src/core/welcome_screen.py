import pygame
from src.config.global_config import WINDOW_WIDTH, INSTRUCTIONS_COLOR, INSTRUCTIONS_FONT, SCREEN
from src.events.event_handler import Movement
from src.utils.utils import Frosty, Title


class WelcomeScreen:
    def __init__(self, scene):
        self.scene = scene
        self.frosty = Frosty()
        self.welcome_title = Title()
        self.title = "Frosty: The runaway snowman!"
        self.welcome_text = ("The aim of the game is to throw snowballs\n"
                             "at Frosty the runaway snowman.\n\n"
                             "Score as many hits\n"
                             "as you can in 30 seconds.\n\n"
                             "But be careful...\n"
                             "...each time you hit Frosty, he gets faster!\n\n"
                             "Use the left/right arrow keys to move\n"
                             "the snowball at the bottom of the screen.\n"
                             "Press SPACEBAR to throw the snowball.\n\n"
                             "Press P to Play or Q to Quit")

    def draw_welcome_text(self, y_start_pos):
        for line in self.welcome_text.splitlines():
            welcome_text = INSTRUCTIONS_FONT.render(line, False, INSTRUCTIONS_COLOR)
            SCREEN.blit(welcome_text, (WINDOW_WIDTH // 2 - welcome_text.get_width() // 2, y_start_pos))
            y_start_pos += welcome_text.get_height()  # Moves to the next line position

    # draws everything required for welcome screen
    def draw_welcome_screen(self, game):
        self.scene.draw_scene()
        self.welcome_title.draw_title(self.title)
        self.frosty.draw_frosty(200)
        self.draw_welcome_text(230)
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
