import pygame
import sys
from sprite_sheet import Character

# Game window set-up
class GameWindow:
    def __init__(self, display_width, display_height):
        pygame.init()  # Initialise pygame
        self.DISPLAY_WIDTH = display_width
        self.DISPLAY_HEIGHT = display_height
        self.display = pygame.display.set_mode((self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT))

        pygame.display.set_caption("Snowpult")
        self.clock = pygame.time.Clock()  # Manages frame rate

    def draw_background(self):
        self.display.fill((135, 206, 235))  # Blue sky
        # Snow layer (x pos, y pos, width, height):
        pygame.draw.rect(self.display, (255, 255, 255), (0, 150, self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT))

    def draw_trees(self):
        for x in range(25, self.DISPLAY_WIDTH - 25, self.DISPLAY_WIDTH // 10):
            # vertices: [x-y (starting point),.....
            pygame.draw.polygon(self.display, (34, 139, 34),
                                [(x, 400), (x + 25, 300),
                                 (x + 50, 400)])  # green tree triangle - 3 points filled with colour
            # Tree brown trunk (x pos, y pos, width, height):
            pygame.draw.rect(self.display, (139, 69, 19), (x + 20, 400, 10, 20))

    def draw_mountains(self):
        for x in range(50, self.DISPLAY_WIDTH - 50, 500):
            pygame.draw.polygon(self.display, (200, 200, 200), [(x + 150, 175), (x + 350, 50), (x + 550, 175)])
            pygame.draw.polygon(self.display, (220, 220, 220), [(x, 200), (x + 200, 50), (x + 450, 200)])

    # Main game loop. Keeps window open until quit
    def run(self):
        self.draw_background()
        self.draw_trees()
        self.draw_mountains()

        bunny_sprite = "../assets/images/bunny_sprite_sheet.png"
        bunny = Character(bunny_sprite)
        # show frame image
        frame_0 = bunny.get_sprite(0, 55, 74, 2)
        frame_1 = bunny.get_sprite(1, 55, 74, 2)

        self.display.blit(frame_0, (0, 0))
        self.display.blit(frame_1, (110, 0)) # scale * width


        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            pygame.display.update()  # flip refreshes entire display surface / update - partial updates for performance
            self.clock.tick(60)  # Limit to 60 frames per second

        pygame.quit()
        sys.exit()


if __name__ == '__main__':
    snowpult = GameWindow(1200, 700)
    snowpult.run()
