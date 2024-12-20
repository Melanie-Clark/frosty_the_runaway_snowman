import pygame
import sys


# Game window set-up
class GameWindow:
    def __init__(self, display_width, display_height):
        pygame.init()  # Initialise pygame
        self.DISPLAY_WIDTH = display_width
        self.DISPLAY_HEIGHT = display_height
        self.display = pygame.display.set_mode((self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT))

        pygame.display.set_caption("Snowpult")
        clock = pygame.time.Clock()  # ----------------

    def draw_background(self):
        self.display.fill((135, 206, 235))  # Blue sky
        # Snow layer (x pos, y pos, width, height):
        pygame.draw.rect(self.display, (255, 255, 255), (0, 150, self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT))

    # Main game loop. Keeps window open until quit
    def run(self):
        self.draw_background()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            pygame.display.update()
            # flip refreshes entire display surface / update - partial updates

        pygame.quit()
        sys.exit()


if __name__ == '__main__':
    snowpult = GameWindow(1200, 700)
    snowpult.run()
