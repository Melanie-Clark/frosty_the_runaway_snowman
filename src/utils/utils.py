import pygame

from src.config.global_config import WINDOW_WIDTH, WINDOW_HEIGHT, SCREEN


# used across files such as welcome_screen and score to load and draw the main character Frosty
class Frosty:
    @staticmethod
    def load_frosty(scale):
        target_image = pygame.image.load("../assets/images/frosty.png").convert_alpha()
        target_image = pygame.transform.scale(target_image, ((50 * scale), (65 * scale)))
        return target_image

    # draws character left and right side of welcome text
    def draw_frosty(self, x_border):
        target_image = self.load_frosty(4)
        SCREEN.blit(target_image,
                    (x_border - target_image.get_width() // 2, WINDOW_HEIGHT // 2))  # draws left-side image
        SCREEN.blit(target_image, (WINDOW_WIDTH - x_border - target_image.get_width() // 2,
                                   WINDOW_HEIGHT // 2))  # draws right-side image
