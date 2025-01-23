import pygame
from src.config.global_config import FEATURE_COLOR, GAME_TEXT_FONT, SCREEN_WIDTH, SCREEN_HEIGHT
from src.screens.base_screen import BaseScreen


class GameOver(BaseScreen):
    def __init__(self, screen, game_state_manager, draw, scene, high_score, health, score, timer=None):
        super().__init__(screen, game_state_manager)
        self.draw = draw
        self.scene = scene
        self.high_score = high_score
        self.score = score
        self.health = health
        self.timer = timer
        self.title = "Game Over"

    # text for the game over screen
    def game_over_text(self):
        total_score, time_bonus, high_score = self.score.total_score(self.health)
        high_score_text = self.high_score.get_high_score_text()

        game_over_text = (
            f"Score:\n"
            f"Health bonus:\n"
            f"Time bonus (10 hits):\n"
            f"TOTAL:\n\n"
            f"{high_score_text}High score:"
        )

        game_over_values = (
            f"{self.score.incremental_score}\n"
            f"{self.health.current_health}\n"
            f"{time_bonus}\n"
            f"{total_score}\n\n"
            f"{high_score}"
        )

        return [game_over_text, game_over_values]

    def draw_text(self):
        x_pos = SCREEN_WIDTH // 3.3
        y_pos = SCREEN_HEIGHT // 2.88
        game_over_info = self.game_over_text()
        for info in game_over_info:
            for line in info.splitlines():
                text = GAME_TEXT_FONT.render(line, True, FEATURE_COLOR)
                self.screen.blit(text, (x_pos, y_pos))
                y_pos += text.get_height()  # Moves position of next text to line below
            x_pos = SCREEN_WIDTH // 1.5
            y_pos = SCREEN_HEIGHT // 2.88

    def draw_game_over_screen(self):
        print("Game Over")
        self.scene.draw_main_scene()
        # draws game over, final score, stats, play again and quit_option onto screen
        self.draw.draw_title(self.title)
        self.draw_text()
        self.draw.draw_menu_options()
        pygame.display.update()

    def reset_game(self, target, player):
        pygame.event.clear()  # clears event queues, so can be replayed
        self.score.incremental_score = self.score.score
        self.health.current_health = self.health.max_health
        self.timer.reset()
        self.score.reset_time_bonus()
        self.high_score.reset_high_score()
        target.speed = target.initial_min_speed
        print("Game reset")
        player.reset_player()

    def run(self):
        self.draw_game_over_screen()


if __name__ == "__main__":
    pass
