import sys
import pygame

from src.core.game_play import GameLoop
from src.core.instructions import InstructionScreen
from src.core.menu import MenuScreen
from src.core.naughty_screen import NaughtyScreen
from src.core.score.high_score import HighScore
from src.config.global_config import FPS, GAME_SCREEN, INSTRUCTION_SCREEN, MENU_SCREEN, GAME_OVER_SCREEN, QUIT, \
    NAUGHTY_SCREEN, TIMES_UP_SCREEN
from src.core.scene import Scene
from src.core.sound import Sound
from src.core.health import Health
from src.core.score.score import Score
from src.core.timer import Timer
from src.core.game_over import GameOver
from src.core.times_up import TimesUpScreen
from src.entities.factory import EntityFactory
from src.events.event_handler import Events


class Game:
    # initialises game window and sprite properties
    def __init__(self):
        self.game_over = None
        pygame.init()  # Initialise pygame
        pygame.display.set_caption("Frosty: The Runaway Snowman!")
        self.clock = pygame.time.Clock()  # Manages frame rate
        self.running = True
        self.timer_running = False
        self.game_state = MENU_SCREEN

        self.timer = Timer()  # Timer instance
        self.scene = Scene()  # Scene instance
        self.health = Health()  # Health instance
        self.high_score = HighScore()  # High score instance
        self.score = Score(self.high_score)  # Score instance
        self.instruction_screen = InstructionScreen()  # Instruction screen instance
        self.menu_screen = MenuScreen(self.scene)  # Menu instance
        self.naughty_screen = NaughtyScreen()
        self.times_up_screen = TimesUpScreen()
        self.target, self.player, self.all_entities, self.target_and_obstacles = EntityFactory().initialise_entities()
        self.game_loop = GameLoop(self.game_state, self.health, self.score, self.scene, self.timer,
                                  self.target_and_obstacles, self.player, self.all_entities)

    def run(self):
        self.high_score.check_score_filepath()  # checks if high score file exists. If not, calls create function
        Sound.music()  # starts background music

        while self.running:
            if self.game_state == QUIT:
                pygame.quit()
                sys.exit()

            self.game_state = Events.event_handler(self.game_state, self.player, self.game_over, self)

            if self.game_state == MENU_SCREEN:
                self.menu_screen.draw_menu_screen()
            elif self.game_state == INSTRUCTION_SCREEN:
                self.instruction_screen.draw_instruction_screen()

            elif self.game_state == GAME_SCREEN:
                if not self.timer_running:
                    # Resets timer when entering the play screen
                    self.timer.reset()
                    self.timer_running = True
                self.game_state = self.game_loop.game_loop(self.timer_running)

            elif self.game_state == TIMES_UP_SCREEN:
                self.times_up_screen.draw_times_up_screen()
                self.game_state = GAME_OVER_SCREEN
            elif self.game_state == NAUGHTY_SCREEN:
                self.naughty_screen.draw_naughty_screen()
            elif self.game_state == GAME_OVER_SCREEN:
                self.game_over = GameOver(self.scene, self.high_score, self.health, self.score,
                                          self.timer)  # Game Over instance
                self.game_over.draw_game_over_screen()

            pygame.display.update()  # flip refreshes entire display surface / update - partial updates for performance
            self.clock.tick(FPS)  # Limit to 60 frames per second


if __name__ == "__main__":
    game = Game()
    game.run()
