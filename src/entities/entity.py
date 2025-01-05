import pygame
import random

from src.config.global_config import SCREEN
from src.entities.sprites import AnimatedSprite
from abc import ABC, abstractmethod


class Entity(ABC):  # inherits functionality from pygames Sprite class
    def __init__(self, sprite_sheet, direction, cooldown, x, y, sprite_width, sprite_height, sprite_scale, row_index,
                 steps, min_speed, max_speed, collision_x_offset, collision_y_offset, collision_width,
                 collision_height, x_speed=0, y_speed=0):
        self.sprite_sheet = sprite_sheet
        self.direction = direction
        self.animation_cooldown = cooldown
        self.x = x
        self.y = y
        self.initial_y = y
        self.sprite_width = sprite_width
        self.sprite_height = sprite_height
        self.sprite_scale = sprite_scale
        self.row_index = row_index
        self.animation_steps = steps
        self.min_speed = min_speed
        self.max_speed = max_speed
        self.initial_min_speed = min_speed
        self.speed = random.randint(self.min_speed, self.max_speed)

        # collision box sizes
        self.collision_x_offset = collision_x_offset
        self.collision_y_offset = collision_y_offset
        self.collision_width = collision_width
        self.collision_height = collision_height

        self.x_speed = x_speed
        self.y_speed = y_speed

        self.last_update = pygame.time.get_ticks()  # time of last frame update
        self.frame = 0
        self.animation_list = self.sprite_sheet.sprite_animation(steps, sprite_width, sprite_height, sprite_scale,
                                                                 row_index)
        self.collision_state = False
        self.space_pressed = False

    # Loads spritesheets
    @staticmethod
    def initialise_spritesheets():
        bunny_sprite = AnimatedSprite("../assets/sprite_sheets/bunny_sprite_sheet.png")
        elf_sprite = AnimatedSprite("../assets/sprite_sheets/elf_sprite_sheet.png")
        reindeer_sprite = AnimatedSprite("../assets/sprite_sheets/reindeer_sprite_sheet.png")
        red_santa_sprite = AnimatedSprite("../assets/sprite_sheets/red_santa_sprite_sheet.png")
        frosty_sprite = AnimatedSprite("../assets/sprite_sheets/frosty_sprite_sheet.png", True)
        return bunny_sprite, elf_sprite, reindeer_sprite, red_santa_sprite, frosty_sprite

    @abstractmethod
    def check_sprite_position(self):
        pass

    def update(self):
        if self.direction == "right":
            self.x += self.speed  # Move to the right
        elif self.direction == "left":
            self.x -= self.speed  # Move to the left

    def update_frame(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_update >= self.animation_cooldown:
            self.frame = (self.frame + 1) % len(self.animation_list)  # Loops back to the first frame
            self.last_update = current_time  # resets time

    # draw to screen
    def draw(self):
        if self.direction == "right":
            flipped_sprite = pygame.transform.flip(self.animation_list[self.frame], True, False)
        else:
            flipped_sprite = self.animation_list[self.frame]

        SCREEN.blit(flipped_sprite, (self.x, self.y))
        # uncomment to debug collisions (puts red box around each sprite)
        # pygame.draw.rect(SCREEN, (255, 0, 0),
        #                  pygame.Rect(self.x + self.collision_x_offset, self.y + self.collision_y_offset,
        #                              self.collision_width, self.collision_height), 2)


if __name__ == "__main__":
    pass
