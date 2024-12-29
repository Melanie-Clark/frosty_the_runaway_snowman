import pygame


class Health:

    def __init__(self, screen, max_health=5):
        self.screen = screen
        self.max_health = max_health
        self.current_health = max_health

    def draw(self):
        heart_health = pygame.image.load("../assets/images/heart_health.png").convert_alpha()
        heart_health = pygame.transform.scale(heart_health, (50, 50))
        x, y = (10, 10)
        for num in range(1, self.current_health + 1):
            self.screen.blit(heart_health, ((num * 15) + x, y))

    def take_damage(self, damage=1):
        self.current_health -= damage
        print('Remaining health:', self.current_health)
        if self.current_health == 0:
            return False
        return True


if __name__ == '__main__':
    pass
