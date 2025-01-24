import pygame
from src.config.global_config import SCREEN_WIDTH, FEATURE_COLOR, FEATURE_FONT


class Timer:
    def __init__(self, screen, game_state, timer_running, timer=30):
        self.screen = screen
        self.game_state_manager = game_state

        self.start_ticks = pygame.time.get_ticks()  # Starting tick
        self.max_time = timer
        self.timer = timer
        self.timer_running = timer_running
        self.seconds = None

    def countdown_timer(self):
        if self.timer_running:
            # elapsed time
            seconds = self.timer - (pygame.time.get_ticks() - self.start_ticks) // 1000
            self.draw_timer(seconds)

            if seconds <= 0:
                self.game_state_manager.set_state("times_up")
            self.set_seconds(seconds)

    # gets the remaining seconds
    def get_seconds(self):
        return self.seconds

    # gets the remaining seconds
    def set_seconds(self, seconds):
        self.seconds = seconds

    # draws time remaining to screen as it countdowns
    def draw_timer(self, seconds):
        countdown = FEATURE_FONT.render(f"Time remaining: {seconds}", False, FEATURE_COLOR)
        countdown_rect = countdown.get_rect()  # puts text into a rectangle
        countdown_rect.topright = (SCREEN_WIDTH - 10, 0)  # Positions rectangle in top-right corner
        self.screen.blit(countdown, countdown_rect)

    # gets the current timer running True/False
    def get_state(self):
        return self.timer_running

    # sets the current timer running to True/False
    def set_state(self, state):
        self.timer_running = state

    # resets timer
    def reset(self):
        self.start_ticks = pygame.time.get_ticks()


if __name__ == "__main__":
    pass
