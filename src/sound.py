import os
import pygame

from src.config.utils import AssetRoot


class Sound:

    @staticmethod
    def get_sound_path(filename):
        project_root = AssetRoot.get_project_root()  # Get the project root directory
        sound_path = os.path.join(project_root, "assets", "sounds", filename)  # Constructs full path to image
        return sound_path

    @staticmethod
    def sound_effect(sound_effect):
        sfx = pygame.mixer.Sound(sound_effect)
        sfx.play()

    @staticmethod
    def music():
        project_root = AssetRoot.get_project_root()  # Get the project root directory
        music_file_path = os.path.join(project_root, 'assets', 'sounds', 'snowtime_soundtrack.ogg')

        pygame.mixer.music.load(music_file_path)
        pygame.mixer.music.play(-1)  # -1 loops infinitely.


if __name__ == "__main__":
    pass
