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
        self.large_font = pygame.font.SysFont(FONT_NAME, 80)

    def draw_game_over_screen(self, runaway_snowman):
        print("Game Over")
        self.scene.draw_scene()
        self.health.draw()
        self.score.draw()

        game_over, incremental_score, health, total_score, play_again, quit_option = self.game_over_text()

        # draws final score, game over, stats, play again and quit_option onto screen
        self.screen.blit(game_over,
                         (WINDOW_WIDTH // 2 - game_over.get_width() // 2,
                          WINDOW_HEIGHT // 2 - (game_over.get_height() * 1.25)))
        self.screen.blit(incremental_score, (
            WINDOW_WIDTH // 2 - incremental_score.get_width() // 2,
            WINDOW_HEIGHT // 2))
        self.screen.blit(health, (
            WINDOW_WIDTH // 2 - health.get_width() // 2,
            WINDOW_HEIGHT // 2 + health.get_height()))
        self.screen.blit(total_score, (
            WINDOW_WIDTH // 2 - total_score.get_width() // 2,
            WINDOW_HEIGHT // 2 + (total_score.get_height() * 2.25)))
        self.screen.blit(play_again, (
            WINDOW_WIDTH // 3 - play_again.get_width() // 2,
            WINDOW_HEIGHT // 1.25 + play_again.get_height()))
        self.screen.blit(quit_option,
                         (((WINDOW_WIDTH // 3) * 2) - quit_option.get_width() // 2,
                          WINDOW_HEIGHT // 1.25 + quit_option.get_height()))

        pygame.display.update()
        self.game_over_event_handler(runaway_snowman)

    # text for the game over screen
    def game_over_text(self):
        game_over = self.large_font.render('Game Over', True, COLOR)
        incremental_score = self.font.render(f'Score: {self.score.incremental_score}', True, COLOR)
        health = self.font.render(f'Health: {self.health.current_health}', True, COLOR)
        total_score = self.font.render(f'TOTAL SCORE: {self.score.total_score(self.health)}', True, COLOR)
        play_again = self.font.render('P - Play again', True, COLOR)
        quit_option = self.font.render('Q - Quit', True, COLOR)
        return game_over, incremental_score, health, total_score, play_again, quit_option

    # Event handling for quit or play again
    def game_over_event_handler(self, runaway_snowman):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Movement.quit_game()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        self.score.incremental_score = self.score.score
                        self.health.current_health = self.health.max_health
                        self.timer.start_ticks = pygame.time.get_ticks()
                        runaway_snowman.speed = runaway_snowman.initial_min_speed
                        return True
                    elif event.key == pygame.K_q:
                        Movement.quit_game()


if __name__ == '__main__':
    pass
