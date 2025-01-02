import pygame
from src.config.global_config import WINDOW_WIDTH, FEATURE_COLOR, FEATURE_FONT


class Timer:
    def __init__(self, screen, timer=30):
        self.screen = screen
        self.start_ticks = pygame.time.get_ticks()  # Starting tick
        self.max_time = timer
        self.timer = timer

    def countdown_timer(self):
        # Calculates remaining time
        seconds = self.timer - (pygame.time.get_ticks() - self.start_ticks) // 1000
        self.draw(seconds)
        if seconds < 0:
            return False
        return True

    def draw(self, seconds):
        countdown = FEATURE_FONT.render(f"Time remaining: {seconds}", False, FEATURE_COLOR)
        countdown_rect = countdown.get_rect()  # puts text into a rectangle
        countdown_rect.topright = (WINDOW_WIDTH - 10, 0)  # Positions rectangle in top-right corner
        self.screen.blit(countdown, countdown_rect)
