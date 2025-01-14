import pygame

from src.config.global_config import SCREEN, PLAY_SCREEN, NAUGHTY_SCREEN
from src.core.naughty_screen import NaughtyScreen


class Health:
    def __init__(self, max_health=5):
        self.max_health = max_health
        self.current_health = max_health
        self.naughty_screen = NaughtyScreen()

    # draws number of health hearts remaining on game screen in top-left corner
    def draw(self):
        heart_health = pygame.image.load("../assets/images/game_play_imgs/heart_health.png").convert_alpha()
        heart_health = pygame.transform.scale(heart_health, (50, 50))
        x, y = (10, 10)
        for num in range(1, self.current_health + 1):
            SCREEN.blit(heart_health, ((num * 15) + x, y))

    # health reduces by one when an obstacle has been hit
    def take_damage(self, damage=1):
        self.current_health -= damage
        print('Remaining health:', self.current_health)
        if self.current_health == 0:
            return NAUGHTY_SCREEN
        return PLAY_SCREEN


if __name__ == "__main__":
    pass
