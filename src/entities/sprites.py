import pygame


class AnimatedSprite:
    def __init__(self, sprite_sheet, flipped=False):
        self.sprite_sheet = pygame.image.load(sprite_sheet).convert_alpha()
        self.flipped = flipped

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
