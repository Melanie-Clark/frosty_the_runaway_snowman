import pygame


class SpriteSheet:
    def __init__(self, sprite_sheet):
        self.sprite_sheet = pygame.image.load(sprite_sheet).convert_alpha()

    def get_sprite(self, frame, width, height, scale):
        image = pygame.Surface((width, height)).convert()
        # Draw sprite by frame
        image.blit(self.sprite_sheet, (0, 0), ((frame * width), 0, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        # set sprite transparent background
        image.set_colorkey((0,0,0))
        return image


if __name__ == '__main__':
    pass
