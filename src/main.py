import pygame
from global_config import DISPLAY_WIDTH, DISPLAY_HEIGHT, FPS
from scene import Scene
from entity import * # should be inidividual classes - circular imports Entity, Item, Obstacle, Target  # check if all methods
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
        self.health = Health(self.DISPLAY)  # Health instance

    def run(self):
        snowman3, reindeer1, bunny4, bunny1, snowman2, bunny3, snowman1, bunny2, snowball = Entity.initialise_entities()
        entities = [snowman3, reindeer1, bunny4, bunny1, snowman2, bunny3, snowman1, bunny2, snowball]

        # main game loop - runs until quit
        while self.running:
            self.draw()

            for entity in entities:
                entity.update()
                entity.draw()
                entity.update_frame()
                if not isinstance(entity,
                                  Item):  # checks if entity is not an instance or child of item class
                    if not snowball.handle_collision(entity, self.health): # passes health instance
                        self.running = False

            self.health.draw()

            pygame.display.update()  # flip refreshes entire display surface / update - partial updates for performance
            self.clock.tick(FPS)  # Limit to 60 frames per second

    def draw(self):
        self.scene.draw_background()
        self.scene.draw_mountains()
        self.scene.draw_trees()


if __name__ == '__main__':
    game = GameLoop()
    game.run()
