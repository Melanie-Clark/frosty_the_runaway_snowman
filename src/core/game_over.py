import pygame
from src.core.global_config import WINDOW_WIDTH, WINDOW_HEIGHT, FONT_NAME, COLOR
from src.events.event_handler import Movement


class GameOver:
    def __init__(self, screen, scene, health, score, timer):
        self.screen = screen
        self.scene = scene
        self.score = score
        self.health = health
        self.timer = timer
        self.font = pygame.font.SysFont(FONT_NAME, 40)
        self.game_over_font = pygame.font.SysFont(FONT_NAME, 80)

    def draw_game_over_screen(self, runaway_snowman):
        print("Game Over")
        self.scene.draw_scene()
        self.health.current_health = 0
        self.health.draw()
        self.score.draw()

        game_over, play_again_button, quit_button = self.game_over_text()

        # draws final score, game over, play again and quit onto screen
        self.screen.blit(game_over,
                         (WINDOW_WIDTH // 2 - game_over.get_width() // 2, WINDOW_HEIGHT // 2 - game_over.get_height()))
        self.screen.blit(play_again_button, (
            WINDOW_WIDTH // 2 - play_again_button.get_width() // 2,
            WINDOW_HEIGHT // 1.9 + play_again_button.get_height()))
        self.screen.blit(quit_button,
                         (WINDOW_WIDTH // 2 - quit_button.get_width() // 2,
                          WINDOW_HEIGHT // 2 + quit_button.get_height() // 2))

        pygame.display.update()
        self.game_over_event_handler(runaway_snowman)

    # text for the game over screen
    def game_over_text(self):
        game_over = self.game_over_font.render('Game Over', True, COLOR)
        play_again_button = self.font.render('P - Play again', True, COLOR)
        quit_button = self.font.render('Q - Quit', True, COLOR)
        return game_over, play_again_button, quit_button

    # Event handling for quit or play again
    def game_over_event_handler(self, runaway_snowman):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Movement.quit_game()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        self.score.total_score = self.score.score
                        self.health.current_health = self.health.max_health
                        self.timer.start_ticks = pygame.time.get_ticks()
                        runaway_snowman.speed = 2
                        return True
                    elif event.key == pygame.K_q:
                        Movement.quit_game()


if __name__ == '__main__':
    pass
