import pygame
from src.config.global_config import SCREEN_WIDTH, FEATURE_COLOR, FEATURE_FONT


class Timer:
    def __init__(self, screen, game_state, timer=30):
        self.screen = screen
        self.game_state_manager = game_state

        self.start_ticks = pygame.time.get_ticks()  # Starting tick
        self.max_time = timer
        self.timer = timer

    def countdown_timer(self, timer_running):
        if timer_running:
            # elapsed time
            seconds = self.timer - (pygame.time.get_ticks() - self.start_ticks) // 1000
            self.draw_timer(seconds)

            if seconds < 0:
                self.game_state_manager.set_state("times_up")
                return seconds
            else:
                self.game_state_manager.set_state("game_play")
                return seconds
        else:
            self.game_state_manager.set_state("game_play")
            return 0

    # draws time remaining to screen as it countdowns
    def draw_timer(self, seconds):
        countdown = FEATURE_FONT.render(f"Time remaining: {seconds}", False, FEATURE_COLOR)
        countdown_rect = countdown.get_rect()  # puts text into a rectangle
        countdown_rect.topright = (SCREEN_WIDTH - 10, 0)  # Positions rectangle in top-right corner
        self.screen.blit(countdown, countdown_rect)

    # resets timer ticks
    def reset(self):
        self.start_ticks = pygame.time.get_ticks()


if __name__ == "__main__":
    pass
