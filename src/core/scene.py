import pygame
import random

from src.config.global_config import WINDOW_WIDTH, WINDOW_HEIGHT, SCREEN


# Game window set-up and background
class Scene:
    def __init__(self):
        self.snowflakes = [
            {"x": random.randint(0, WINDOW_WIDTH), "y": random.randint(0, WINDOW_HEIGHT), "speed": random.randint(2, 4)}
            for _ in range(250)]  # number of snowflakes

    # draws blue sky and snow background
    @staticmethod
    def draw_background():
        SCREEN.fill((135, 206, 235))  # Blue sky
        # Snow layer (x pos, y pos, width, height):
        pygame.draw.rect(SCREEN, (255, 255, 255), (0, 150, WINDOW_WIDTH, WINDOW_HEIGHT))

    @staticmethod
    def draw_trees():
        for x in range(25, WINDOW_WIDTH - 25, WINDOW_WIDTH // 10):
            # vertices: [x-y (starting point),.....]
            pygame.draw.polygon(SCREEN, (34, 139, 34),
                                [(x, 200), (x + 25, 100),
                                 (x + 50, 200)])  # green tree triangle (3 points filled with colour)
            # Tree brown trunk (x pos, y pos, width, height):
            pygame.draw.rect(SCREEN, (139, 69, 19), (x + 20, 200, 10, 20))

    @staticmethod
    def draw_mountains():
        for x in range(50, WINDOW_WIDTH - 50, 500):
            pygame.draw.polygon(SCREEN, (200, 200, 200), [(x + 150, 175), (x + 350, 50), (x + 550, 175)])
            pygame.draw.polygon(SCREEN, (220, 220, 220), [(x, 200), (x + 200, 50), (x + 450, 200)])

    # draws snow moving down at varying speed
    def draw_snow(self):
        for flake in self.snowflakes:
            flake["y"] += flake["speed"]

            if flake["y"] > WINDOW_HEIGHT:
                flake["y"] = 0
                flake["x"] = random.randint(0, WINDOW_WIDTH)
            pygame.draw.circle(SCREEN, (255, 255, 255), (flake["x"], flake["y"]), 2.5)

    # draws complete scene
    def draw_main_scene(self):
        self.draw_background()
        self.draw_mountains()
        self.draw_trees()


    # loads target character
    @staticmethod
    def load_frosty(scale=4):
        target_image = pygame.image.load("../assets/images/game_play_imgs/frosty.png").convert_alpha()
        target_image = pygame.transform.scale(target_image, ((50 * scale), (65 * scale)))
        return target_image

    # draws character left and right side of text
    def draw_frosty(self, x_border):
        target_image = self.load_frosty()
        SCREEN.blit(target_image,
                    (x_border - target_image.get_width() // 2, WINDOW_HEIGHT // 2.5))  # draws left-side image
        SCREEN.blit(target_image, (WINDOW_WIDTH - x_border - target_image.get_width() // 2,
                                   WINDOW_HEIGHT // 1.8))  # draws right-side image


if __name__ == "__main__":
    pass
