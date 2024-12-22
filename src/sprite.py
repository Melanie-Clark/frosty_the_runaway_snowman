from abc import abstractmethod
import pygame
from global_config import *
from event_handler import Movement
from game_loop import GameLoop


class Entity:
    def __init__(self, sprite_sheet, cooldown, x, y, sprite_width, sprite_height, sprite_scale, row_index, steps, speed, direction,
                 rotation, x_speed=0, y_speed=0):
        self.sprite_sheet = sprite_sheet
        self.animation_cooldown = cooldown
        self.x = x
        self.y = y
        self.initial_y = y
        self.sprite_width = sprite_width
        self.sprite_height = sprite_height
        self.sprite_scale = sprite_scale
        self.row_index = row_index
        self.animation_steps = steps
        self.speed = speed
        self.direction = direction
        self.last_update = pygame.time.get_ticks()  # time of execution
        self.frame = 0
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.animation_list = self.sprite_sheet.sprite_animation(self.animation_steps, self.sprite_width,
                                                                 self.sprite_height,
                                                                 self.sprite_scale, self.row_index, rotation)

    @abstractmethod
    def update(self):
        pass

    def update_frame(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_update >= self.animation_cooldown:
            self.frame = (self.frame + 1) % len(self.animation_list)  # Loops back to the first frame
            self.last_update = current_time  # resets time

    # draw to screen
    def draw(self):
        GameLoop.DISPLAY.blit(self.animation_list[self.frame], (self.x, self.y))


class Animal(Entity):
    def update(self):
        # Move the animal based on direction
        if self.direction == "right":
            self.x += self.speed  # Move to the right
        elif self.direction == "left":
            self.x -= self.speed  # Move to the left

        # Reset the bunny or snowman when they go off-screen
        if self.x > DISPLAY_WIDTH:  # If the entity moves off the right edge
            self.x = -self.sprite_width  # Reset to the left edge
        elif self.x < -self.sprite_width:  # If the entity moves off the left edge
            self.x = DISPLAY_WIDTH  # Reset to the right edge


        # # Keeps the sprite within screen bounds
        # self.x = max(-self.sprite_width * 2, min(DISPLAY_WIDTH, self.x))
        return True # this isn't needed - adjust entities from game_loop ------------------------


class Item(Entity):

    def update(self):
        self.x, self.y, self.x_speed, self.y_speed = Movement.event_handler(self.x, self.y, self.x_speed,
                                                                            self.y_speed)

        # Reset the bunny or snowman when they go off-screen
        if self.y < 0:  # If the entity moves off the top of the screem
            self.y = self.initial_y  # Reset to the bottom edge
            self.y_speed = 0


        # # Keeps the sprite within screen bounds
        self.x = max(0, min(DISPLAY_WIDTH - 60, self.x))
        # self.y = max(0, min(DISPLAY_HEIGHT - 60, self.y))

        return True

if __name__ == '__main__':
    pass