import pygame

from src.core.score.high_score import HighScore
from src.config.global_config import FPS
from src.core.scene import Scene
from src.core.sound import Sound
from src.core.welcome_screen import WelcomeScreen
from src.core.health import Health
from src.core.score.score import Score
from src.core.timer import Timer
from src.core.game_over import GameOver
from src.entities.factory import EntityFactory
from src.entities.player import Player


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
        self.high_score = HighScore()  # High score instance

    # initialises entities for use in game loop
    @staticmethod
    def initialise_entities():
        entities, frosty, snowball = EntityFactory().initialise_entities()
        all_entities = [snowball, frosty] + entities
        return frosty, snowball, all_entities

    def game_loop(self):
        self.timer.reset()  # Resets the timer each time game is started
        target, player, all_entities = self.initialise_entities()

        # main game loop - runs until quit
        while self.running:
            self.scene.draw_scene()
            self.score.draw()
            self.health.draw()

            result, seconds = self.timer.countdown_timer()
            if not result:
                self.game_over.load_game_over(target, player)

            for entity in all_entities:
                entity.update()
                entity.check_sprite_position()
                entity.draw()
                entity.update_frame()

                if not isinstance(entity, Player):  # checks entity is not an instance or child of snowball class
                    self.running = player.check_collision(entity, self.health, self.score, seconds)
                    if not self.running:
                        self.game_over.load_game_over(target, player)

            pygame.display.update()  # flip refreshes entire display surface / update - partial updates for performance
            self.clock.tick(FPS)  # Limit to 60 frames per second

    def run(self):
        self.high_score.check_score_filepath()  # checks if high score file exists. If not, calls create function
        Sound().music()  # starts background music
        self.welcome_screen.draw_welcome_screen(self)  # welcome screen


if __name__ == '__main__':
    game = GameLoop()
    game.run()
