import pygame

from src.core.global_config import SCREEN, FPS
from src.core.scene import Scene
from src.core.welcome_screen import WelcomeScreen
from src.entitites.entity import Entity, Item
from src.core.health import Health
from src.core.score import Score
from src.core.timer import Timer
from src.core.game_over import GameOver



class GameLoop:
    # initialises game window and sprite properties
    def __init__(self):
        pygame.init()  # Initialise pygame
        pygame.display.set_caption("Frosty: The runaway snowman!")
        self.clock = pygame.time.Clock()  # Manages frame rate
        self.running = True
        self.scene = Scene(SCREEN)  # Scene instance
        self.health = Health(SCREEN)  # Health instance
        self.score = Score(SCREEN)  # Score instance
        self.timer = Timer(SCREEN)  # Timer instance
        self.welcome_screen = WelcomeScreen(SCREEN, self.scene)  # Welcome screen instance
        self.game_over = GameOver(SCREEN, self.scene, self.health, self.score, self.timer)  # Game Over instance

    def run(self):
        entities, runaway_snowman, snowball = Entity.initialise_entities()
        all_entities = entities + [runaway_snowman, snowball]

        # main game loop - runs until quit
        self.running = True
        while self.running:
            self.welcome_screen.draw_welcome_screen()
            self.scene.draw_scene()
            self.score.draw()
            self.health.draw()

            if not self.timer.countdown_timer():
                self.game_over.draw_game_over_screen(runaway_snowman)

            for entity in all_entities:
                entity.update()
                entity.check_sprite_position()
                entity.draw()
                entity.update_frame()

                if not isinstance(entity, Item):  # checks entity is not an instance or child of item class
                    self.running = snowball.handle_collision(entity, self.health, self.score)
                    if not self.running:
                        self.game_over.draw_game_over_screen(runaway_snowman)

            pygame.display.update()  # flip refreshes entire display surface / update - partial updates for performance
            self.clock.tick(FPS)  # Limit to 60 frames per second

        self.game_over.draw_game_over_screen(runaway_snowman)


if __name__ == '__main__':
    game = GameLoop()
    game.run()
