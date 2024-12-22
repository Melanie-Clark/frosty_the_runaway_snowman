from abc import abstractmethod
import pygame
from global_config import *
from event_handler import Movement
from game_loop import GameLoop


class Entity:
    def __init__(self, sprite_sheet, cooldown, x, y, sprite_width, sprite_height, sprite_scale, row_index, steps,
                 rotation, x_speed=0, y_speed=0):
        self.sprite_sheet = sprite_sheet
        self.animation_cooldown = cooldown
        self.x = x
        self.y = y
        self.sprite_width = sprite_width
        self.sprite_height = sprite_height
        self.sprite_scale = sprite_scale
        self.row_index = row_index
        self.animation_steps = steps
        self.last_update = pygame.time.get_ticks()  # time of execution
        self.frame = 0
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.animation_list = self.sprite_sheet.sprite_animation(self.animation_steps, self.sprite_width,
                                                                 self.sprite_height,
                                                                 self.sprite_scale, self.row_index, rotation)

    def animation(self, entity):
        return self.animation_list

    @abstractmethod
    def update(self, running):
        pass

    def update_frame(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_update >= self.animation_cooldown:
            self.frame = (self.frame + 1) % len(self.animation_list)  # Loops back to the first frame
            self.last_update = current_time  # resets time


class Animal(Entity):
    def update(self, running):
        self.x, self.y, self.x_speed, self.y_speed, running = Movement.event_handler(self.x, self.y, self.x_speed,
                                                                                     self.y_speed, running)

        # Keeps the sprite within screen bounds
        self.x = max(0, min(DISPLAY_WIDTH - (self.sprite_width * 2), self.x))
        self.y = max(0, min(DISPLAY_HEIGHT - (self.sprite_height * 2), self.y))

        self.update_frame()

        # animation
        GameLoop.DISPLAY.blit(self.animation_list[self.frame], (self.x, self.y))

        return Movement.event_handler(self.x, self.y, self.x_speed, self.y_speed, running)


class Item(Entity):

    def update(self, running):
        self.x, self.y, self.x_speed, self.y_speed, running = Movement.event_handler(self.x, self.y, self.x_speed,
                                                                                     self.y_speed, running)

        # Keeps the sprite within screen bounds
        self.x = max(0, min(DISPLAY_WIDTH - 60, self.x))
        self.y = max(0, min(DISPLAY_HEIGHT - 60, self.y))

        self.update_frame()

        # animation
        GameLoop.DISPLAY.blit(self.animation_list[self.frame], (self.x, self.y))

        return Movement.event_handler(self.x, self.y, self.x_speed, self.y_speed, running)