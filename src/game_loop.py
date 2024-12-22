import pygame
from global_config import *
from scene import Scene
import sprite
from sprite_sheet import SpriteSheet


class GameLoop:
    # initialises game window and sprite properties
    DISPLAY = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

    def __init__(self):
        pygame.init()  # Initialise pygame

        pygame.display.set_caption("Snowpult")
        self.clock = pygame.time.Clock()  # Manages frame rate
        self.running = True
        self.scene = Scene(self.DISPLAY)  # Scene instance

    def run(self):
        bunny_sprite = SpriteSheet("../assets/images/bunny_sprite_sheet.png")
        snowball_sprite = SpriteSheet("../assets/images/snowball_sprite_sheet.png")
        snowman_sprite = SpriteSheet("../assets/images/snowman_sprite_sheet.png")
        snowmen_sprite = SpriteSheet("../assets/images/img.png")

        # cooldown - how quickly animation runs (milliseconds)
        snowball = sprite.Item(snowball_sprite, 250, 0, DISPLAY_HEIGHT - 72, 500, 350, 0.25, 0, 3, 10, "left", 270, 5,
                               5, 60, 65)
        # snowmen = sprite.Animal(snowmen_sprite, 150, DISPLAY_WIDTH, DISPLAY_HEIGHT // 4, 97, 126, 2, 1, 5, 0)
        snowman = sprite.Animal(snowman_sprite, 150, 0, DISPLAY_HEIGHT // 3, 16, 16, 6, 0, 6, 4, "right", 0, 0, 0, 100,
                                95)
        bunny = sprite.Animal(bunny_sprite, 150, DISPLAY_WIDTH, DISPLAY_HEIGHT // 2, 55, 74, 2, 2, 4, 4, "left", 0, 8,
                              55, 100, 95)

        entities = [snowball, bunny, snowman]

        # main game loop - runs until quit
        while self.running:
            self.draw()

            for entity in entities:
                if not entity.update():
                    entities.remove(entity)
                else:
                    entity.draw()
                    entity.update_frame()
                    if not isinstance(entity,
                                      sprite.Item):  # checks if entity is not an instance or child of item class
                        snowball.collision(entity)

            pygame.display.update()  # flip refreshes entire display surface / update - partial updates for performance
            self.clock.tick(FPS)  # Limit to 60 frames per second

    def draw(self):
        self.scene.draw_background()
        self.scene.draw_trees()
        self.scene.draw_mountains()


if __name__ == '__main__':
    game = GameLoop()
    game.run()
