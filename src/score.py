import pygame


class Score:
    def __init__(self, screen):
        self.screen = screen
        self.score = 0
        self.total_score = 0
        self.size = 40
        self.font_name = "Verdana"
        self.color = "red"
        self.font = pygame.font.SysFont(self.font_name, self.size)

        self.green_santa_image = pygame.image.load("../assets/images/green_santa.png").convert_alpha()
        self.green_santa = pygame.transform.scale(self.green_santa_image, (60, 60))

    def increment_score(self):
        self.total_score += 1
        print("Total Score:", self.total_score)

    def draw(self):
        score_text = self.font.render(f"Score: {self.total_score}", True, self.color)
        self.screen.blit(self.green_santa, (700, 5))
        self.screen.blit(score_text, (500, 5))

    def game_over(self):
        print("Game Over")
        game_over_font = pygame.font.SysFont(self.font_name, 100)
        score_text = game_over_font.render(f"Total Score: {self.total_score}", True, self.color)
        self.screen.blit(score_text, (400, 350))
        # STOP SPEED or go to Game Over menu----------------------------------
