# class available for use across the game project
import os
import sys
import pygame

from pathlib import Path

from src.config.global_config import SCREEN_WIDTH, TITLE_FONT, TITLE_HEIGHT, MENU_COLOR, FEATURE_COLOR, \
    INSTRUCTIONS_FONT


# class available for use across the game project
class Draw:
    def __init__(self, screen):
        self.screen = screen

    def draw_title(self, title):
        # render creates a surface (graphical object) for text to be displayed
        title_font = TITLE_FONT.render(title, False, FEATURE_COLOR)  # antialias (TRUE smooth text)
        # draws rendered text onto screen (SCREEN)
        self.screen.blit(title_font, (SCREEN_WIDTH // 2 - title_font.get_width() // 2, TITLE_HEIGHT))

    def draw_text(self, text, font, color, y_pos):
        for line in text.splitlines():
            text = font.render(line, True, color)
            self.screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, y_pos))
            y_pos += text.get_height()  # Moves position of next text to the line below

    # draws menu options for welcome and game over screens
    def draw_menu_options(self, menu_options="[M] Main menu   [P] Play   [Q] Quit"):
        self.draw_text(menu_options, INSTRUCTIONS_FONT, MENU_COLOR, 660)


class AssetRoot:
    # gets project root directory
    @staticmethod
    def get_project_root():
        return Path(sys.path[0])

    def load_image(self, images_sub_folder, filename):
        project_root = self.get_project_root()  # Get the project root directory
        image_path = os.path.join(project_root, "assets", "images", images_sub_folder,
                                  filename)  # Construct full path to image
        return pygame.image.load(image_path).convert_alpha()


if __name__ == "__main__":
    pass


class AssetRoot:
    # gets project root directory
    @staticmethod
    def get_project_root():
        return Path(sys.path[0])

    def load_image(self, images_sub_folder, filename):
        project_root = self.get_project_root()  # Get the project root directory
        image_path = os.path.join(project_root, "assets", "images", images_sub_folder,
                                  filename)  # Construct full path to image
        return pygame.image.load(image_path).convert_alpha()


if __name__ == "__main__":
    pass
