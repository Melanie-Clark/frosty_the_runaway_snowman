from src.config.global_config import FEATURE_COLOR, FEATURE_FONT
from src.core.scene import Scene


# keep track of players score
class Score:
    def __init__(self, screen, high_score, score=0):
        self.screen = screen
        self.score = score
        self.high_score = high_score
        self.incremental_score = score
        self.time_bonus = None

    def increment_score(self, seconds):
        self.incremental_score += 1
        if self.incremental_score == 10:
            self.time_bonus = seconds
        print("Score:", self.incremental_score, "Time bonus:", self.time_bonus)

    # draws score to screen
    def draw(self):
        score_text = FEATURE_FONT.render(f"Score: {self.incremental_score}", False, FEATURE_COLOR)
        target_image = Scene.load_frosty(1)
        self.screen.blit(target_image, (700, 5))
        self.screen.blit(score_text, (500, 5))

    # calculates total score based on snowball hits and health remaining
    def total_score(self, health):
        if self.time_bonus:
            bonus = self.time_bonus
        else:
            bonus = 0

        total_score = self.incremental_score + health.current_health + bonus
        print("Total score:", total_score)
        high_score, new_high_score = self.high_score.check_high_score(total_score)
        return total_score, bonus, high_score, new_high_score

    # resets time_bonus for play again
    def reset_time_bonus(self):
        self.time_bonus = 0
