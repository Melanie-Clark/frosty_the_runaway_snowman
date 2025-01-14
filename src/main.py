import sys
import pygame

from src.core.instructions import InstructionScreen
from src.core.menu import MenuScreen
from src.core.naughty_screen import NaughtyScreen
from src.core.score.high_score import HighScore
from src.config.global_config import FPS, PLAY_SCREEN, INSTRUCTION_SCREEN, MENU_SCREEN, GAME_OVER_SCREEN, QUIT, \
    NAUGHTY_SCREEN
from src.core.scene import Scene
from src.core.sound import Sound
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
        self.timer_running = False
        self.game_state = MENU_SCREEN

        self.timer = Timer()  # Timer instance
        self.scene = Scene()  # Scene instance
        self.health = Health()  # Health instance
        self.score = Score()  # Score instance
        self.high_score = HighScore()  # High score instance
        self.instruction_screen = InstructionScreen()  # Instruction screen instance
        self.menu_screen = MenuScreen(self.scene)  # Menu instance
        self.naughty_screen = NaughtyScreen()
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
            result = player.check_collision(entity, self.health, self.score, seconds)
            if result != PLAY_SCREEN:  # If collision changes state, return immediately
                return result
        return PLAY_SCREEN

    def game_loop(self):
        self.scene.draw_main_scene()
        self.score.draw()
        self.health.draw()

        # returns game state
        self.game_state, seconds = self.timer.countdown_timer(self.timer_running)

        if self.game_state == PLAY_SCREEN:
            self.game_state = self.check_collision(self.target_and_obstacles, self.player, seconds)
            self.update_entities(self.all_entities)

    def run(self):
        self.high_score.check_score_filepath()  # checks if high score file exists. If not, calls create function
        Sound.music()  # starts background music

        while self.running:
            if self.game_state == QUIT:
                pygame.quit()
                sys.exit()

            if self.game_state == MENU_SCREEN:
                self.menu_screen.draw_menu_screen()
            elif self.game_state == INSTRUCTION_SCREEN:
                self.instruction_screen.draw_instruction_screen()
            elif self.game_state == PLAY_SCREEN:
                # Resets the timer when entering the play screen
                if not self.timer_running:
                    self.timer.reset()
                    self.timer_running = True
                self.game_loop()
            elif self.game_state == NAUGHTY_SCREEN:
                self.naughty_screen.draw_naughty_screen()
            elif self.game_state == GAME_OVER_SCREEN:
                self.game_over.draw_game_over_screen()

            self.game_state = Events.event_handler(self.game_state, self.player, self.game_over, self)

            pygame.display.update()  # flip refreshes entire display surface / update - partial updates for performance
            self.clock.tick(FPS)  # Limit to 60 frames per second


if __name__ == "__main__":
    game = GameLoop()
    game.run()
