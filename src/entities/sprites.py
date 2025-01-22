import pygame
import os

from src.config.utils import AssetRoot


class AnimatedSprite:
    def __init__(self, sprite_sheet, flipped=False):
        self.sprite_sheet = pygame.image.load(sprite_sheet).convert_alpha()
        self.flipped = flipped

    @staticmethod
    def get_sprite_sheet_path(filename):
        project_root = AssetRoot().get_project_root()  # Gets project root directory
        sprite_sheet_path = os.path.join(project_root, "assets", "sprite_sheets",
                                         filename)  # Constructs full path to sprite_sheet
        return sprite_sheet_path
    # loads and scales single sprite
    def get_sprite(self, frame, y, width, height, scale, rotation):
        sprite = self.sprite_sheet.subsurface(
            ((frame * width), y, width, height)).convert_alpha()  # extracts sprite by frame
        sprite = pygame.transform.scale(sprite, (width * scale, height * scale))
        sprite = pygame.transform.rotate(sprite, rotation)
        sprite = pygame.transform.flip(sprite, self.flipped, False)
        return sprite

    def sprite_animation(self, steps, width, height, scale, row_index, rotation=0):
        animation_list = []
        y = height * row_index  # sets y-axis to row number

        for frame in range(steps):  # steps = number of frames
            animation_list.append(self.get_sprite(frame, y, width, height, scale, rotation))
        return animation_list


if __name__ == '__main__':
    pass
