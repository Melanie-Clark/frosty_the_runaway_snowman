import pygame
import random

from abc import ABC, abstractmethod


# Base/Parent class for all entities
class Entity(ABC):
    def __init__(self, screen, sprite_sheet, direction, cooldown, x, y, sprite_width, sprite_height, sprite_scale,
                 row_index,
                 steps, min_speed, max_speed, collision_x_offset, collision_y_offset, collision_width,
                 collision_height, x_speed=0, y_speed=0):
        self.screen = screen
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
        self.speed = self.get_random_speed()

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

    def get_random_speed(self):
        return random.randint(self.min_speed, self.max_speed)

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
        sprite = self.animation_list[self.frame]
        if self.direction == "right":
            sprite = pygame.transform.flip(sprite, True, False)

        self.screen.blit(sprite, (self.x, self.y))
        # # uncomment to debug collisions (puts red box around each sprite):
        # pygame.draw.rect(self.screen, (255, 0, 0),
        #                  pygame.Rect(self.x + self.collision_x_offset, self.y + self.collision_y_offset,
        #                              self.collision_width, self.collision_height), 2)


if __name__ == "__main__":
    pass
