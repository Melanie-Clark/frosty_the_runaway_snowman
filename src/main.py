import pygame

from src.config.global_config import FPS, SCREEN
from src.core.scene import Scene
from src.core.welcome_screen import WelcomeScreen
from src.entitites.entity import Entity
from src.core.health import Health
from src.core.score import Score
from src.core.timer import Timer
from src.core.game_over import GameOver
from src.entitites.snowball import Snowball


class GameLoop:
    # initialises game window and sprite properties
    def __init__(self):
        pygame.init()  # Initialise pygame
        pygame.display.set_caption("Frosty: The runaway snowman!")
        self.clock = pygame.time.Clock()  # Manages frame rate
        self.running = True
        self.timer = Timer()  # Timer instance
        self.scene = Scene()  # Scene instance
        self.health = Health()  # Health instance
        self.score = Score()  # Score instance
        self.welcome_screen = WelcomeScreen(self.scene)  # Welcome screen instance
        self.game_over = GameOver(self.scene, self.health, self.score, self.timer)  # Game Over instance

    # initialises entities for use in game loop
    @staticmethod
    def initialise_entities():
        entities, frosty = Entity.initialise_entities()
        snowball = Snowball.initialise_entities()
        all_entities = [snowball, frosty] + entities
        return frosty, snowball, all_entities

    def game_loop(self):
        self.timer.reset()  # Resets the timer each time game is started
        frosty, snowball, all_entities = self.initialise_entities()

        # main game loop - runs until quit
        while self.running:

            self.scene.draw_scene()
            self.score.draw()
            self.health.draw()

            if not self.timer.countdown_timer():
                self.load_game_over(frosty)

            for entity in all_entities:
                entity.update()
                entity.check_sprite_position()
                entity.draw()
                entity.update_frame()

                if not isinstance(entity, Snowball):  # checks entity is not an instance or child of item class
                    self.running = snowball.handle_collision(entity, self.health, self.score)
                    if not self.running:
                        self.load_game_over(frosty)

            pygame.display.update()  # flip refreshes entire display surface / update - partial updates for performance
            self.clock.tick(FPS)  # Limit to 60 frames per second

        self.load_game_over(frosty)

    # loads the game over screen and functionality
    def load_game_over(self, frosty):
        self.game_over.draw_game_over_screen(frosty)

    def run(self):
        self.welcome_screen.draw_welcome_screen(self)


if __name__ == '__main__':
    game = GameLoop()
    game.run()
