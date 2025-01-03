import csv
import os


class HighScore:
    def __init__(self):
        self.directory = "../src/core/score"
        self.filename = "high_scores.csv"
        self.file_path = os.path.join(self.directory, self.filename)  # Construct the full path to the specific file
        self.field_names = ["High Score", "Level"]

    # Check if the file already exists in the directory
    def check_score_filepath(self):
        if not os.path.exists(self.file_path):
            self.create_high_score_file()

    # creates a new file to store high scores
    def create_high_score_file(self):
        with open(self.file_path, "w+") as csv_file:
            spreadsheet = csv.DictWriter(csv_file, fieldnames=self.field_names)
            spreadsheet.writeheader()
            spreadsheet.writerows([{"High Score": 0, "Level": 1}])

    # checks if it's a new high score
    def check_high_score(self, score):
        with open(self.file_path, "r") as csv_file:
            spreadsheet = csv.DictReader(csv_file)
            first_row = next(spreadsheet)

            if score > int(first_row["High Score"]):
                high_score = score
                print(f"NEW Player High Score: {high_score}")
                self.update_high_score(high_score)

    # updates the high score file with new high score
    def update_high_score(self, high_score):
        with open(self.file_path, "w+") as csv_file:
            spreadsheet = csv.DictWriter(csv_file, fieldnames=self.field_names)
            spreadsheet.writeheader()
            spreadsheet.writerows([{"High Score": high_score, "Level": 1}])


if __name__ == "__main__":
    pass
