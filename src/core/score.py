import pygame
from src.core.global_config import FONT_NAME, COLOR


class Score:
    def __init__(self, screen, score=0):
        self.screen = screen
        self.score = score
        self.total_score = score
        self.size = 40
        self.font = pygame.font.SysFont(FONT_NAME, self.size)

        self.target_image = pygame.image.load("../assets/images/runaway_snowman.png").convert_alpha()
        self.target_image = pygame.transform.scale(self.target_image, (50, 65))

    def increment_score(self):
        self.total_score += 1
        print("Total Score:", self.total_score)

    def draw(self):
        score_text = self.font.render(f"Score: {self.total_score}", True, COLOR)
        self.screen.blit(self.target_image, (700, 5))
        self.screen.blit(score_text, (500, 5))
