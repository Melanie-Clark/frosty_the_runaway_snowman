import pygame
from src.config.global_config import WINDOW_WIDTH, WINDOW_HEIGHT


# Game window set-up and background
class Scene:
    def __init__(self, screen):
        self.screen = screen

    def draw_background(self):
        self.screen.fill((135, 206, 235))  # Blue sky
        # Snow layer (x pos, y pos, width, height):
        pygame.draw.rect(self.screen, (255, 255, 255), (0, 150, WINDOW_WIDTH, WINDOW_HEIGHT))

    def draw_trees(self):
        for x in range(25, WINDOW_WIDTH - 25, WINDOW_WIDTH // 10):
            # vertices: [x-y (starting point),.....]
            pygame.draw.polygon(self.screen, (34, 139, 34),
                                [(x, 200), (x + 25, 100),
                                 (x + 50, 200)])  # green tree triangle (3 points filled with colour)
            # Tree brown trunk (x pos, y pos, width, height):
            pygame.draw.rect(self.screen, (139, 69, 19), (x + 20, 200, 10, 20))

    def draw_mountains(self):
        for x in range(50, WINDOW_WIDTH - 50, 500):
            pygame.draw.polygon(self.screen, (200, 200, 200), [(x + 150, 175), (x + 350, 50), (x + 550, 175)])
            pygame.draw.polygon(self.screen, (220, 220, 220), [(x, 200), (x + 200, 50), (x + 450, 200)])

    def draw_scene(self):
        self.draw_background()
        self.draw_mountains()
        self.draw_trees()


if __name__ == '__main__':
    pass
