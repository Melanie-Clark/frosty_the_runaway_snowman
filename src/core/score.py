from src.config.global_config import FEATURE_COLOR, FEATURE_FONT
from src.utils.utils import Frosty


class Score:
    def __init__(self, screen, score=0):
        self.screen = screen
        self.score = score
        self.incremental_score = score

    def increment_score(self):
        self.incremental_score += 1
        print("Score:", self.incremental_score)

    def draw(self):
        score_text = FEATURE_FONT.render(f"Score: {self.incremental_score}", False, FEATURE_COLOR)
        target_image = Frosty.load_frosty(1)
        self.screen.blit(target_image, (700, 5))
        self.screen.blit(score_text, (500, 5))

    def total_score(self, health):
        total_score = self.incremental_score + health.current_health
        print("Total score:", total_score)
        return total_score
