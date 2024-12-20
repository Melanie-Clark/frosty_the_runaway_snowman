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

    # Main game loop. Keeps window open until quit
    @staticmethod
    def run():
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
