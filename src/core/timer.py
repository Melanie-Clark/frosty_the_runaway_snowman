import pygame
from src.config.global_config import WINDOW_WIDTH, FEATURE_COLOR, FEATURE_FONT, SCREEN, GAME_SCREEN, TIMES_UP_SCREEN


class Timer:
    def __init__(self, timer=30):
        self.start_ticks = pygame.time.get_ticks()  # Starting tick
        self.max_time = timer
        self.timer = timer

    def countdown_timer(self, timer_running):
        if timer_running:
            # elapsed time
            seconds = self.timer - (pygame.time.get_ticks() - self.start_ticks) // 1000
            self.draw_timer(seconds)

            if seconds < 0:
                return TIMES_UP_SCREEN, seconds
            else:
                return GAME_SCREEN, seconds
        else:
            return GAME_SCREEN, 0

    # draws time remaining to screen as it countdowns
    @staticmethod
    def draw_timer(seconds):
        countdown = FEATURE_FONT.render(f"Time remaining: {seconds}", False, FEATURE_COLOR)
        countdown_rect = countdown.get_rect()  # puts text into a rectangle
        countdown_rect.topright = (WINDOW_WIDTH - 10, 0)  # Positions rectangle in top-right corner
        SCREEN.blit(countdown, countdown_rect)

    # resets timer ticks
    def reset(self):
        self.start_ticks = pygame.time.get_ticks()


if __name__ == "__main__":
    pass
