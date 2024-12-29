import pygame
import sys

from src.core.global_config import FPS, WINDOW_WIDTH, WINDOW_HEIGHT
from src.core.scene import Scene
from src.entitites.entity import * # Entity, Item
from src.core.health import Health
from src.core.score import Score
from src.core.timer import Timer
from src.core.game_over import GameOver


class GameLoop:
    # initialises game window and sprite properties
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    def __init__(self):
        pygame.init()  # Initialise pygame
        pygame.display.set_caption("Double Trouble: Snowball Santa")
        self.clock = pygame.time.Clock()  # Manages frame rate
        self.running = True
        self.scene = Scene(self.screen)  # Scene instance
        self.health = Health(self.screen)  # Health instance
        self.score = Score(self.screen)  # Score instance
        self.timer = Timer(self.screen)  # Timer instance
        self.game_over = GameOver(self.screen, self.scene, self.health, self.score, self.timer,
                                  self.quit_game)  # Game Over instance

    def run(self):
        green_santa, red_santa, reindeer1, elf, bunny1, snow_thief, bunny3, bunny2, snowball = Entity.initialise_entities()
        entities = [green_santa, red_santa, reindeer1, elf, bunny1, snow_thief, bunny3, bunny2, snowball]

        # main game loop - runs until quit
        self.running = True
        while self.running:
            self.scene.draw_scene()
            self.score.draw()
            self.health.draw()

            if not self.timer.countdown_timer():
                self.game_over.draw_game_over_screen()

            for entity in entities:
                entity.update()
                entity.draw()
                entity.update_frame()

                if not isinstance(entity, Item):  # checks entity is not an instance or child of item class
                    self.running = snowball.handle_collision(entity, self.health, self.score)
                    if not self.running:
                        self.game_over.draw_game_over_screen()

            pygame.display.update()  # flip refreshes entire display surface / update - partial updates for performance
            self.clock.tick(FPS)  # Limit to 60 frames per second

        self.game_over.draw_game_over_screen()

    @staticmethod
    def quit_game():
        pygame.quit()
        sys.exit()


if __name__ == '__main__':
    game = GameLoop()
    game.run()
