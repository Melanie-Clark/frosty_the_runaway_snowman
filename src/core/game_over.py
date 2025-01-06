import pygame
from src.config.global_config import FEATURE_COLOR, FEATURE_FONT
from src.events.event_handler import Movement
from src.utils.utils import Draw


class GameOver:
    def __init__(self, scene, health, score, timer=None):
        self.scene = scene
        self.score = score
        self.health = health
        self.timer = timer
        self.draw = Draw()
        self.running = None
        self.title = "Game Over"

    # text for the game over screen
    def game_over_text(self):
        total_score, time_bonus, high_score, new_high_score = self.score.total_score(self.health)

        game_over_text = (
            f"Score: {self.score.incremental_score}\n"
            f"Health Bonus: {self.health.current_health}\n"
            f"Time Bonus: {time_bonus}\n"
            f"TOTAL SCORE: {total_score}\n\n"
            f"{new_high_score}HIGH SCORE: {high_score}"
        )

        return game_over_text

    def draw_game_over_screen(self):
        print("Game Over")
        self.scene.draw_scene()
        game_over_text = self.game_over_text()

        # draws game over, final score, stats, play again and quit_option onto screen
        self.draw.draw_title(self.title)
        self.draw.draw_text(game_over_text, FEATURE_FONT, FEATURE_COLOR, 250)
        self.draw.draw_menu_options()

        pygame.display.update()

    # Event handling for quit or play again
    def game_over_event_handler(self, target, player):
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
                        self.score.reset_time_bonus()
                        target.speed = target.initial_min_speed
                        player.reset_player()
                        return True
                    elif event.key == pygame.K_q:
                        Movement.quit_game()

    # loads the game over screen and functionality
    def load_game_over(self, target, player):
        self.running = True
        self.draw_game_over_screen()
        self.game_over_event_handler(target, player)


if __name__ == '__main__':
    pass
