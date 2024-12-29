import pygame

from src.core.global_config import WINDOW_WIDTH, WINDOW_HEIGHT


class GameOver:
    def __init__(self, screen, scene, health, score, timer, quit_game):
        self.screen = screen
        self.scene = scene
        self.color = "red" # initialise once for game
        self.score = score
        self.health = health
        self.timer = timer
        self.quit_game = quit_game


    # split into different methods -------------------------------------------------
    def draw_game_over_screen(self):
        print("Game Over")
        self.scene.draw_scene()
        self.health.current_health = 0
        self.health.draw()
        self.score.draw()


        font = pygame.font.SysFont('verdana', 40)
        game_over_font = pygame.font.SysFont('verdana', 80)

        # draws final score, game over, play again and quit on screen
        game_over = game_over_font.render('Game Over', True, self.color)
        play_again_button = font.render('P - Play again', True, self.color)
        quit_button = font.render('Q - Quit', True, self.color)

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
                        self.score.total_score = self.score.score
                        self.health.current_health = self.health.max_health
                        self.timer.start_ticks = pygame.time.get_ticks()
                        return True
                    elif event.key == pygame.K_q:
                        self.quit_game()

if __name__ == '__main__':
    pass