import pygame


class SpriteSheet:
    def __init__(self, sprite_sheet):
        self.sprite_sheet = pygame.image.load(sprite_sheet).convert_alpha()

    def get_sprite(self, frame, y, width, height, scale):
        image = pygame.Surface((width, height)).convert()
        # Draw sprite by frame
        image.blit(self.sprite_sheet, (0, 0), ((frame * width), y, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        # set sprite transparent background
        image.set_colorkey((0, 0, 0))
        return image

    def sprite_animation(self, steps, width, height, scale, row_index):
        animation_list = []
        animations_steps = steps  # i.e. how many images are idle
        y = height * row_index  # sets y-axis to start of row number

        for x in range(animations_steps):
            animation_list.append(self.get_sprite(x, y, width, height, scale))
        return animation_list


if __name__ == '__main__':
    pass
