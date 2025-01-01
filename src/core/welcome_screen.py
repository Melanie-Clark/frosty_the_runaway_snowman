import pygame
from src.core.global_config import WINDOW_WIDTH, WINDOW_HEIGHT, FONT_NAME, COLOR, INSTRUCTIONS_COLOR
from src.events.event_handler import Movement


class WelcomeScreen:
    def __init__(self, screen, scene, font_size=30):
        self.screen = screen
        self.scene = scene
        self.font = pygame.font.SysFont(FONT_NAME, font_size) # -----------font size on game over and score ------------
        self.large_font = pygame.font.SysFont(FONT_NAME, 50) # -----------font size on game over and score ------------
# -------- play and quit - needs to be size 40 ----------------------------


    @staticmethod
    def welcome_images(scale):
        # ---------------create function, as also used in score.py-different tuple multiplication-----------
        target_image = pygame.image.load("../assets/images/runaway_snowman.png").convert_alpha()
        target_image = pygame.transform.scale(target_image, ((50 * scale), (65 * scale)))
        return target_image

    # text for the game over screen
    def welcome_text(self):
        title = self.large_font.render('Frosty: The runaway snowman!', True, COLOR)
        welcome_text = ("The aim of the game is to throw snowballs\n"
        "at Frosty the runaway snowman\n"
        "as many times as you can\n"
        " to get the highest score.\n\n"
        "But be careful...\n"
        "...each time you hit Frosty, he gets faster!\n\n"
        "Press SPACEBAR to throw the snowball.\n\n"
        "Press P to Play, or Q to Quit.")
        play = self.font.render('P - Play', True, COLOR)
        quit_option = self.font.render('Q - Quit', True, COLOR)
        return title, welcome_text, play, quit_option

    def draw_welcome_screen(self):
        self.scene.draw_scene()
        target_image = self.welcome_images(4)

        title, welcome_text, play, quit_option = self.welcome_text()

        # centres title on screen
        self.screen.blit(title, (WINDOW_WIDTH // 2 - title.get_width() // 2, 10))

        welcome_text_y = 230
        for line in welcome_text.splitlines():
            welcome_text = self.font.render(line, True, INSTRUCTIONS_COLOR)
            self.screen.blit(welcome_text, (WINDOW_WIDTH // 2 - welcome_text.get_width() // 2, welcome_text_y))
            # Moves to the next line position
            welcome_text_y += welcome_text.get_height()

        self.screen.blit(target_image, (
            WINDOW_WIDTH // 1.25, WINDOW_HEIGHT // 2))  # -------------single line used in score draw method------
        self.screen.blit(target_image, (
            WINDOW_WIDTH // 4 - target_image.get_width(), WINDOW_HEIGHT // 2))  # -------------single line used in score draw method------

        # draws play again and quit_option onto screen
        self.screen.blit(play, (
            WINDOW_WIDTH // 3 - play.get_width() // 2,
            WINDOW_HEIGHT // 1.15 + play.get_height()))
        self.screen.blit(quit_option,
                         (((WINDOW_WIDTH // 3) * 2) - quit_option.get_width() // 2,
                          WINDOW_HEIGHT // 1.15 + quit_option.get_height()))

        pygame.display.update()
        self.welcome_screen_event_handler()

    # Event handling for starting game
    def welcome_screen_event_handler(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Movement.quit_game()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        print("ADD MAIN SCREEN HERE")  # ----------------------------
                    elif event.key == pygame.K_q:
                        Movement.quit_game()


if __name__ == '__main__':
    pass
