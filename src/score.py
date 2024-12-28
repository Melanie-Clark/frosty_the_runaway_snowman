import pygame


class Score:
    def __init__(self, screen, current_score=0, size=40):
        self.screen = screen
        self.score = current_score
        self.total = current_score
        self.size = size
        self.color = "red"

    def total_score(self):
        self.total += 1
        print("Total Score:", self.total)


    def draw(self):
        font = pygame.font.SysFont("verdana", self.size)
        score_text = font.render(f"Score: {self.total}", True, self.color)
        self.screen.blit(score_text, (500, 5))

    def game_over(self):
        print("Game Over")
        font = pygame.font.SysFont("verdana", 100)
        score_text = font.render(f"Total Score: {self.total}", True, self.color)
        self.screen.blit(score_text, (500, 350))
        # STOP SPEED or go to Game Over menu----------------------------------
