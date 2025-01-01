import pygame
from src.core.global_config import FONT_NAME, COLOR


class Score:
    def __init__(self, screen, score=0):
        self.screen = screen
        self.score = score
        self.incremental_score = score
        self.size = 40
        self.font = pygame.font.SysFont(FONT_NAME, self.size)

        self.target_image = pygame.image.load("../assets/images/runaway_snowman.png").convert_alpha()
        self.target_image = pygame.transform.scale(self.target_image, (50, 65))

    def increment_score(self):
        self.incremental_score += 1
        print("Score:", self.incremental_score)

    def draw(self):
        score_text = self.font.render(f"Score: {self.incremental_score}", True, COLOR)
        self.screen.blit(self.target_image, (700, 5))
        self.screen.blit(score_text, (500, 5))

    def total_score(self, health):
        total_score = self.incremental_score + health.current_health
        print("Total score:", total_score)
        return total_score
