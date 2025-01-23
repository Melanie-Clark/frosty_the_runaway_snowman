import pygame
import csv
import os

from src.config.global_config import FEATURE_COLOR, FEATURE_FONT, SCREEN_HEIGHT, SCREEN_WIDTH
from src.screens.base_screen import BaseScreen


class HighScore(BaseScreen):
    def __init__(self, screen, game_state_manager, scene, draw):
        super().__init__(screen, game_state_manager)
        self.scene = scene
        self.draw = draw
        self.title = "Frosty: The Runaway Snowman!"
        self.directory = "src/score"
        self.filename = "high_scores.csv"
        self.file_path = os.path.join(self.directory, self.filename)  # Construct the full path to the specific file
        self.field_names = ["High Score", "Level"]
        self.high_score_text = ""

    # Check if the file already exists in the directory
    def check_score_filepath(self):
        os.makedirs(self.directory, exist_ok=True)  # Creates directory if it doesn't exist
        if not os.path.exists(self.file_path):
            self.create_high_score_file()

    # creates a new file to store high scores
    def create_high_score_file(self):
        with open(self.file_path, "w+") as csv_file:
            spreadsheet = csv.DictWriter(csv_file, fieldnames=self.field_names)
            spreadsheet.writeheader()
            spreadsheet.writerows([{"High Score": 0, "Level": 1}])

    # checks if there's a new high score
    def check_high_score(self, score):
        with open(self.file_path, "r") as csv_file:
            spreadsheet = csv.DictReader(csv_file)
            first_row = next(spreadsheet)

            if score > int(first_row["High Score"]):
                self.set_new_high_score(score)
                high_score = score
            else:
                high_score = int(first_row["High Score"])

        return high_score

    # updates the high score file with new high score
    def set_new_high_score(self, high_score):
        self.high_score_text = "NEW! "
        with open(self.file_path, "w+") as csv_file:
            spreadsheet = csv.DictWriter(csv_file, fieldnames=self.field_names)
            spreadsheet.writeheader()
            spreadsheet.writerows([{"High Score": high_score, "Level": 1}])

    def get_high_score_text(self):
        return self.high_score_text

    def get_high_score(self):
        with open(self.file_path, "r") as csv_file:
            spreadsheet = csv.DictReader(csv_file)
            first_row = next(spreadsheet)
            high_score = int(first_row["High Score"])
        return high_score

    def reset_high_score(self):
        self.high_score_text = ""

    def draw_text(self):
        high_score = self.get_high_score()
        display_text = f"High Score: {high_score}"
        self.draw.draw_text(display_text, FEATURE_FONT, FEATURE_COLOR, SCREEN_HEIGHT // 2)

    # draws everything required for menu screen
    def draw_screen(self):
        self.scene.draw_main_scene()
        self.scene.draw_frosty(SCREEN_WIDTH // 6.4)
        self.scene.draw_snow()
        self.draw.draw_title(self.title)
        self.draw_text()
        self.draw.draw_menu_options()
        pygame.display.update()

    def run(self):
        self.draw_screen()


if __name__ == "__main__":
    pass
