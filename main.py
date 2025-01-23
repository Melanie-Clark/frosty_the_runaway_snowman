import pygame
import asyncio  # required for pygbag conversion to downloadable file

from src.screens.game_over import GameOver
from src.screens.game_play import GameLoop
from src.screens.instructions import InstructionScreen
from src.screens.menu import MenuScreen
from src.screens.naughty_screen import NaughtyScreen
from src.screens.high_score import HighScore
from src.config.global_config import FPS, SCREEN_WIDTH, SCREEN_HEIGHT
from src.scene import Scene
from src.screens.reload import Reload
from src.sound import Sound
from src.health import Health
from src.score.score import Score
from src.timer import Timer
from src.screens.times_up import TimesUpScreen
from src.entities.factory import EntityFactory
from src.config.event_handler import EventHandler
from src.config.game_state_manager import GameStateManager
from src.config.utils import Draw


class Game:
    # initialises game window and sprite properties
    def __init__(self):
        pygame.init()  # Initialise pygame
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Frosty: The Runaway Snowman!")
        self.clock = pygame.time.Clock()  # Manages frame rate
        self.running = True

        self.game_state_manager = GameStateManager("main_menu")

        self.scene = Scene(self.screen)
        self.draw = Draw(self.screen)
        self.health = Health(self.screen, self.game_state_manager)
        self.timer = Timer(self.screen, self.game_state_manager, False)

        self.high_score = HighScore(self.screen, self.game_state_manager, self.scene, self.draw)
        self.score = Score(self.screen, self.high_score, self.timer.seconds)

        self.target, self.player, self.all_entities, self.target_and_obstacles = EntityFactory(
            self.screen).initialise_entities()

        self.menu_screen = MenuScreen(self.screen, self.game_state_manager, self.scene, self.draw)
        self.instruction_screen = InstructionScreen(self.screen, self.game_state_manager, self.scene, self.draw)
        self.game_play = GameLoop(self.screen, self.game_state_manager, self.health, self.score,
                                  self.scene, self.timer, self.target_and_obstacles, self.player, self.all_entities)
        self.naughty_screen = NaughtyScreen(self.screen, self.game_state_manager, self.scene, self.draw)
        self.times_up_screen = TimesUpScreen(self.screen, self.game_state_manager, self.scene, self.draw)
        self.game_over = GameOver(self.screen, self.game_state_manager, self.draw, self.scene, self.high_score,
                                  self.health, self.score, self.timer)
        self.reload = Reload(self.screen, self.game_state_manager, self.scene, self.draw)

        self.states = {
            "main_menu": self.menu_screen,
            "instructions": self.instruction_screen,
            "high_score": self.high_score,
            "game_play": self.game_play,
            "naughty_screen": self.naughty_screen,
            "times_up": self.times_up_screen,
            "game_over": self.game_over,
            "reload": self.reload
        }

        self.event_handler = EventHandler(self.game_state_manager, self, self.player, self.game_over, self.timer)

    # async required for pygbag conversion to downloadable file - defines an asynchronous coroutine
    async def main(self):
        self.high_score.check_score_filepath()  # checks if high score file exists. If not, calls create function
        Sound.music()  # starts background music

        while self.running:
            # calls the central event handler for any state
            self.event_handler.handle_events()

            # returns current state and runs that state
            self.states[self.game_state_manager.get_state()].run()

            pygame.display.update()  # flip refreshes entire display surface / update - partial updates for performance
            self.clock.tick(FPS)  # Limit to 60 frames per second

            # required for pygbag conversion to downloadable file - pauses execution until the awaited coroutine or task is completed.
            await asyncio.sleep(0)


if __name__ == "__main__":
    game = Game()
    asyncio.run(game.main())  # required for pygbag conversion to downloadable file
