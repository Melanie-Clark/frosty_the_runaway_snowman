import pygame
from global_config import *
from scene import Scene
import sprite
from sprite_sheet import SpriteSheet
from health import Health


class GameLoop:
    # initialises game window and sprite properties
    DISPLAY = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

    def __init__(self):
        pygame.init()  # Initialise pygame

        pygame.display.set_caption("Snowpult")
        self.clock = pygame.time.Clock()  # Manages frame rate
        self.running = True
        self.scene = Scene(self.DISPLAY)  # Scene instance
        self.health = Health(self.DISPLAY)  # Scene instance

    def run(self):
        bunny_sprite_left = SpriteSheet("../assets/images/bunny_sprite_sheet.png", False)
        bunny_sprite_right = SpriteSheet("../assets/images/bunny_sprite_sheet.png", True)
        snowball_sprite = SpriteSheet("../assets/images/snowball_sprite_sheet.png", False)
        snowman_sprite = SpriteSheet("../assets/images/snowman_sprite_sheet.png", False)

        # cooldown - how quickly animation runs (milliseconds)
        snowball = sprite.Item(snowball_sprite, 250, 0, DISPLAY_HEIGHT - 50, 500, 350, 0.22, 0, 3, 10, "left", 270, 5,
                               3, 55, 55)

        bunny1 = sprite.Animal(bunny_sprite_left, 150, DISPLAY_WIDTH // 1.2, DISPLAY_HEIGHT // 1.5, 55, 74, 2, 2, 4, 3,
                               "left", 0, 8,
                               55, 100, 95)
        bunny2 = sprite.Animal(bunny_sprite_right, 150, DISPLAY_WIDTH // 3.2, DISPLAY_HEIGHT // 1.6, 55, 74, 2, 2, 4,
                               3.5, "right", 0, 8,
                               55, 100, 95)
        snowman1 = sprite.Animal(snowman_sprite, 150, 0, DISPLAY_HEIGHT // 1.7, 16, 16, 6, 0, 6, 6, "right", 0, 0, 0,
                                 100,
                                 95)
        bunny3 = sprite.Animal(bunny_sprite_left, 150, DISPLAY_WIDTH // 2.3, DISPLAY_HEIGHT // 2.3, 55, 74, 2, 2, 4, 4,
                               "left", 0, 8,
                               55, 100, 95)
        snowman2 = sprite.Animal(snowman_sprite, 150, 0, DISPLAY_HEIGHT // 2.5, 16, 16, 6, 0, 6, 4, "left", 0, 0, 0,
                                 100,
                                 95)
        bunny4 = sprite.Animal(bunny_sprite_right, 150, DISPLAY_WIDTH // 3, DISPLAY_HEIGHT // 3.9, 55, 74, 2, 2, 4, 5,
                               "right", 0, 8,
                               55, 100, 95)
        snowman3 = sprite.Animal(snowman_sprite, 150, DISPLAY_WIDTH // 3.8, DISPLAY_HEIGHT // 4.1, 16, 16, 6, 0, 6,
                                 2.53, "right", 0, 0, 0, 100,
                                 95)

        entities = [snowman3, bunny4, bunny1, snowman2, bunny3, snowman1, bunny2, snowball]

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
        self.scene.draw_mountains()
        self.scene.draw_trees()
        self.health.draw()



if __name__ == '__main__':
    game = GameLoop()
    game.run()
