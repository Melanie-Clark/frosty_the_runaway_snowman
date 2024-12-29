import pygame
import sys
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
        pygame.display.set_caption("Snowball Frenzy: Fake Santa")
        self.clock = pygame.time.Clock()  # Manages frame rate
        self.running = True
        self.scene = Scene(self.screen)  # Scene instance
        self.health = Health(self.screen)  # Health instance
        self.score = Score(self.screen)  # Score instance
        self.color = "red"

    def run(self):
        green_santa, red_santa, reindeer1, elf, bunny1, snow_thief, bunny3, bunny2, snowball = Entity.initialise_entities()
        entities = [green_santa, red_santa, reindeer1, elf
            , bunny1, snow_thief, bunny3, bunny2, snowball]

        game_state = "game"

        # main game loop - runs until quit
        while self.running:
            if game_state == "game":
                self.draw_scene()
                self.score.draw()
                self.health.draw()

                for entity in entities:
                    entity.update()
                    entity.draw()
                    entity.update_frame()

                    if not isinstance(entity, Item):  # checks entity is not an instance or child of item class
                        game_state = snowball.handle_collision(entity, self.health, self.score)
                        if game_state == "game_over":
                            self.draw_game_over_screen()

            pygame.display.update()  # flip refreshes entire display surface / update - partial updates for performance
            self.clock.tick(FPS)  # Limit to 60 frames per second

    def draw_scene(self):
        self.scene.draw_background()
        self.scene.draw_mountains()
        self.scene.draw_trees()

    def draw_game_over_screen(self):
        print("Game Over")
        self.draw_scene()

        font = pygame.font.SysFont('verdana', 40)
        game_over_font = pygame.font.SysFont('verdana', 80)

        game_over = game_over_font.render('Game Over', True, self.color)
        play_again_button = font.render('P - Play again', True, self.color)
        quit_button = font.render('Q - Quit', True, self.color)

        # draws final score, game over, play again and quit on screen
        self.score.draw()
        self.screen.blit(game_over,
                         (WINDOW_WIDTH // 2 - game_over.get_width() // 2, WINDOW_HEIGHT // 2 - game_over.get_height()))
        self.screen.blit(play_again_button, (
            WINDOW_WIDTH // 2 - play_again_button.get_width() // 2,
            WINDOW_HEIGHT // 1.9 + play_again_button.get_height()))
        self.screen.blit(quit_button,
                         (WINDOW_WIDTH // 2 - quit_button.get_width() // 2,
                          WINDOW_HEIGHT // 2 + quit_button.get_height() // 2))

        pygame.display.update()

        # Event handling for quit or play again
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit_game()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        self.score.total_score = 0
                        self.health.current_health = 5
                        return "game"
                    elif event.key == pygame.K_q:
                        self.quit_game()

    @staticmethod
    def quit_game():
        pygame.quit()
        sys.exit()


if __name__ == '__main__':
    game = GameLoop()
    game.run()
