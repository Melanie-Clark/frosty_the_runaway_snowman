from src.config.global_config import FEATURE_COLOR, FEATURE_FONT, SCREEN
from src.utils.utils import Frosty


# keep track of players score
class Score:
    def __init__(self, score=0):
        self.score = score
        self.incremental_score = score

    def increment_score(self):
        self.incremental_score += 1
        print("Score:", self.incremental_score)

    # draws score to screen
    def draw(self):
        score_text = FEATURE_FONT.render(f"Score: {self.incremental_score}", False, FEATURE_COLOR)
        target_image = Frosty.load_frosty(1)
        SCREEN.blit(target_image, (700, 5))
        SCREEN.blit(score_text, (500, 5))

    # calculates total score based on snowball hits and health remaining
    def total_score(self, health):
        total_score = self.incremental_score + health.current_health
        print("Total score:", total_score)
        return total_score
