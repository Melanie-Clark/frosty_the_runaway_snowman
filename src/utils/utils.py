import pygame

from src.config.global_config import WINDOW_WIDTH, WINDOW_HEIGHT, SCREEN, TITLE_FONT, FEATURE_COLOR, TITLE_HEIGHT


# used across files such as welcome_screen and score to load and draw the main character Frosty
class Frosty:
    @staticmethod
    def load_frosty(scale):
        target_image = pygame.image.load("../assets/images/game_play_imgs/frosty.png").convert_alpha()
        target_image = pygame.transform.scale(target_image, ((50 * scale), (65 * scale)))
        return target_image

    # draws character left and right side of welcome text
    def draw_frosty(self, x_border):
        target_image = self.load_frosty(4)
        SCREEN.blit(target_image,
                    (x_border - target_image.get_width() // 2, WINDOW_HEIGHT // 2))  # draws left-side image
        SCREEN.blit(target_image, (WINDOW_WIDTH - x_border - target_image.get_width() // 2,
                                   WINDOW_HEIGHT // 2))  # draws right-side image


# class available for use across the game project
class Draw:
    @staticmethod
    def draw_title(title):
        # render creates a surface (graphical object) for text to be displayed
        title_font = TITLE_FONT.render(title, False, FEATURE_COLOR)  # antialias (TRUE smooth text)
        # draws rendered text onto screen (SCREEN)
        SCREEN.blit(title_font, (WINDOW_WIDTH // 2 - title_font.get_width() // 2, TITLE_HEIGHT))

    @staticmethod
    def draw_text(text, font, color, y_pos):
        for line in text.splitlines():
            text = font.render(line, False, color)
            SCREEN.blit(text, (WINDOW_WIDTH // 2 - text.get_width() // 2, y_pos))
            y_pos += text.get_height()  # Moves position of next text to the line below
