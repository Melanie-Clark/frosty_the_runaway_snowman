import pygame
from global_config import WINDOW_WIDTH, WINDOW_HEIGHT, FPS
from scene import Scene
from entity import *  # Entity, Item, Obstacle, Target
from health import Health
from score import Score


class GameLoop:
    # initialises game window and sprite properties
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    def __init__(self):
        pygame.init()  # Initialise pygame
        pygame.display.set_caption("Snowball Fake Santa")  # --------------game name------
        self.clock = pygame.time.Clock()  # Manages frame rate
        self.running = True
        self.scene = Scene(self.screen)  # Scene instance
        self.health = Health(self.screen)  # Health instance
        self.score = Score(self.screen)  # Score instance

    def run(self):
        red_santa, snowman3, reindeer1, bunny4, bunny1, snowman2, bunny3, snowman1, bunny2, snowball = Entity.initialise_entities()
        entities = [red_santa, snowman3, reindeer1, bunny4, bunny1, snowman2, bunny3, snowman1, bunny2, snowball]

        # main game loop - runs until quit
        while self.running:
            self.draw()
            self.score.draw()

            for entity in entities:
                entity.update()

                entity.draw()
                entity.update_frame()
                if not isinstance(entity,
                                  Item):  # checks if entity is not an instance or child of item class
                    if not snowball.handle_collision(entity, self.health, self.score):  # passes health and score instance
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