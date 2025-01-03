import pygame
from src.config.global_config import WINDOW_WIDTH, WINDOW_HEIGHT, FEATURE_COLOR, INSTRUCTIONS_COLOR, FEATURE_FONT, \
    SCREEN
from src.events.event_handler import Movement
from src.utils.utils import Title


class GameOver:
    def __init__(self, scene, health, score, timer=None):
        self.scene = scene
        self.score = score
        self.health = health
        self.timer = timer
        self.game_over_title = Title()
        self.title = "Game Over"

    # text for the game over screen
    def game_over_text(self):
        incremental_score = FEATURE_FONT.render(f'Score: {self.score.incremental_score}', False, FEATURE_COLOR)
        health = FEATURE_FONT.render(f'Health: {self.health.current_health}', False, FEATURE_COLOR)

        total_score, time_bonus = self.score.total_score(self.health)
        total_score = FEATURE_FONT.render(f'TOTAL SCORE: {total_score}', False, FEATURE_COLOR)
        time_bonus = FEATURE_FONT.render(f'Time bonus: {time_bonus}', False, FEATURE_COLOR)

        options = FEATURE_FONT.render('Press P to Play or Q to Quit', False, INSTRUCTIONS_COLOR)
        return [incremental_score, health, time_bonus, total_score], options

    def draw_game_over_screen(self, frosty):
        print("Game Over")
        self.scene.draw_scene()

        game_over_text, options = self.game_over_text()

        # draws final score, game over, stats, play again and quit_option onto screen
        self.game_over_title.draw_title(self.title)

        # draws score, health remaining and total to screen
        for i, text in enumerate(game_over_text, start=-1):
            SCREEN.blit(text, (WINDOW_WIDTH // 2 - text.get_width() // 2,
                               WINDOW_HEIGHT // 2 + text.get_height() * i))

        SCREEN.blit(options, (WINDOW_WIDTH // 2 - options.get_width() // 2,
                              WINDOW_HEIGHT // 1.25 + options.get_height()))

        pygame.display.update()
        self.game_over_event_handler(frosty)

    # Event handling for quit or play again
    def game_over_event_handler(self, frosty):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Movement.quit_game()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        pygame.event.clear()  # clears event queues, so can be replayed
                        self.score.incremental_score = self.score.score
                        self.health.current_health = self.health.max_health
                        self.timer.reset()
                        frosty.speed = frosty.initial_min_speed
                        self.score.reset_time_bonus()
                        return True
                    elif event.key == pygame.K_q:
                        Movement.quit_game()


if __name__ == '__main__':
    pass
