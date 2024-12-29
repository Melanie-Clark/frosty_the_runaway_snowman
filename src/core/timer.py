import pygame

from src.core.global_config import WINDOW_WIDTH


class Timer:
    def __init__(self, screen, timer=30):
        self.screen = screen
        self.start_ticks = pygame.time.get_ticks()  # Starting tick
        self.max_time = timer
        self.timer = timer
        self.size = 40
        self.font_name = "Verdana"
        self.color = "red"  # use colour from main.py ------------------
        self.font = pygame.font.SysFont(self.font_name, self.size)

    def countdown_timer(self):
        # Calculates remaining time
        seconds = self.timer - (pygame.time.get_ticks() - self.start_ticks) // 1000
        self.draw(seconds)
        if seconds < 0:
            return False
        return True

    def draw(self, seconds):
        countdown = self.font.render(f"Time remaining: {seconds}", True, self.color)
        countdown_rect = countdown.get_rect()  # puts text into a rectangle
        countdown_rect.topright = (WINDOW_WIDTH - 10, 0)  # Positions rectangle in top-right corner
        self.screen.blit(countdown, countdown_rect)
