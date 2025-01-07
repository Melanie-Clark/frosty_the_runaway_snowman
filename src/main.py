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
from src.events.event_handler import Events


class GameLoop:
    # initialises game window and sprite properties
    def __init__(self):
        pygame.init()  # Initialise pygame
        pygame.display.set_caption("Frosty: The runaway snowman!")
        self.clock = pygame.time.Clock()  # Manages frame rate
        self.running = True
        self.game_state = "Welcome"

        self.timer = Timer()  # Timer instance
        self.scene = Scene()  # Scene instance
        self.health = Health()  # Health instance
        self.score = Score()  # Score instance
        self.high_score = HighScore()  # High score instance
        self.welcome_screen = WelcomeScreen(self.scene)  # Welcome screen instance
        self.game_over = GameOver(self.scene, self.health, self.score, self.timer)  # Game Over instance
        self.target, self.player, self.all_entities, self.target_and_obstacles = EntityFactory().initialise_entities()

    @staticmethod
    def update_entities(all_entities):
        for entity in all_entities:
            entity.update()
            entity.check_sprite_position()
            entity.draw()
            entity.update_frame()

    def check_collision(self, target_and_obstacles, player, seconds):
        # checks collision for any obstacle or target
        for entity in target_and_obstacles:
            player.check_collision(entity, self.health, self.score, seconds, self.game_over, self)

    def game_loop(self):
        self.timer.reset()  # Resets the timer each time game is started

        # main game loop - runs until quit
        while self.running:
            self.scene.draw_main_scene()
            self.score.draw()
            self.health.draw()

            self.game_state = "Play"
            Events.event_handler(self.game_state, self.player, self)

            # returns result as True (in play), False (out of play - out of time)
            result, seconds = self.timer.countdown_timer()
            if not result:
                self.game_over.load_game_over(self)

            self.check_collision(self.target_and_obstacles, self.player, seconds)
            self.update_entities(self.all_entities)

            pygame.display.update()  # flip refreshes entire display surface / update - partial updates for performance
            self.clock.tick(FPS)  # Limit to 60 frames per second

    def run(self):
        self.high_score.check_score_filepath()  # checks if high score file exists. If not, calls create function
        Sound.music()  # starts background music

        while self.running:
            if self.game_state == "Welcome":
                self.welcome_screen.draw_welcome_screen(self)
            elif self.game_state == "Play":
                self.game_loop()


if __name__ == '__main__':
    game = GameLoop()
    game.run()
