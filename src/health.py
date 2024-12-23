import pygame


class Health:
    def __init__(self, display):
        self.display = display

    def draw(self):
        heart_health = pygame.image.load("../assets/images/heart_health.png").convert_alpha()
        heart_health = pygame.transform.scale(heart_health, (50, 50))
        x, y = (10, 10)
        for num in range(1, 6):
            self.display.blit(heart_health, ((num * 15) + x, y))
