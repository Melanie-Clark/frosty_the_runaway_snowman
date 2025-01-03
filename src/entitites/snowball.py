import random
import pygame
from pygame.examples.sprite_texture import sprite
from src.config.global_config import WINDOW_WIDTH, WINDOW_HEIGHT
from src.entitites.entity import Target, Entity
from src.entitites.sprites import AnimatedSprite


class Snowball(Entity):
    def __init__(self, sprite_sheet, direction="left", cooldown=250, x=WINDOW_WIDTH // 2, y=WINDOW_HEIGHT - 55,
                 sprite_width=500, sprite_height=350, sprite_scale=0.22, row_index=0, steps=3,
                 min_speed=10, max_speed=10, collision_x_offset=5, collision_y_offset=3, collision_width=55,
                 collision_height=55,
                 rotation=270):
        super().__init__(sprite_sheet, direction, cooldown, x, y, sprite_width, sprite_height, sprite_scale, row_index,
                         steps, min_speed, max_speed, collision_x_offset, collision_y_offset, collision_width,
                         collision_height)
        self.sprite_width = sprite
        self.animation_list = self.sprite_sheet.sprite_animation(steps, sprite_width, sprite_height, sprite_scale,
                                                                 row_index, rotation)

    @staticmethod
    def initialise_entities():
        # Loads spritesheet
        snowball_sprite = AnimatedSprite("../assets/sprite_sheets/snowball_sprite_sheet.png")
        snowball = Snowball(snowball_sprite)
        return snowball

    def update(self):
        self.x, self.y, self.x_speed, self.y_speed, self.space_pressed = self.movement.event_handler(self.x, self.y,
                                                                                                     self.x_speed,
                                                                                                     self.y_speed,
                                                                                                     self.space_pressed)

    def check_sprite_position(self):
        # Resets snowball when if it goes off-screen
        if self.y < 0 - self.collision_height:
            self.y = self.initial_y  # Resets to initial position on y-axis
            self.y_speed = 0
            self.space_pressed = False

        # Keeps the sprite within screen bounds
        self.x = max(0, min(WINDOW_WIDTH - self.collision_width, self.x))

    def collision_boundaries(self, entity):
        self_rect = pygame.Rect(self.x + self.collision_x_offset, self.y + self.collision_y_offset,
                                self.collision_width, self.collision_height)
        entity_rect = pygame.Rect(entity.x + entity.collision_x_offset, entity.y + entity.collision_y_offset,
                                  entity.collision_width, entity.collision_height // 2)
        return self_rect, entity_rect

    def handle_collision(self, entity, health, score):  # receives health instance, so can be called during collision
        self_rect, entity_rect = self.collision_boundaries(entity)
        # colliderect() - pygame method to check if two rects collide
        if self_rect.colliderect(
                entity_rect) and self.collision_state == False:  # extra parameter False required to prevent a collision everytime the rects collide in one hit
            # resets item after collision on y-axis
            self.y = WINDOW_HEIGHT - self.collision_height  # resets snowball on y-axis
            self.y_speed = 0  # resets snowball speed
            self.collision_state = True
            self.space_pressed = False
            if isinstance(entity, Target):
                # Sound.sound_effect("../assets/sounds/ouch.mp3")
                score.increment_score()

                # resets frosty to disappear and re-enter from left or right side, increases speed
                entity.x = random.choice((0, WINDOW_WIDTH))
                entity.y = random.randint(200, 400)  # entity.min_y_range, entity.max_y_range
                entity.speed += 0.70

            else:
                return health.take_damage()
        # If no collision, reset collision state
        elif not self_rect.colliderect(entity_rect):
            self.collision_state = False
        return True


if __name__ == '__main__':
    pass
