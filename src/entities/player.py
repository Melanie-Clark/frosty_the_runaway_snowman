import pygame
from src.config.global_config import WINDOW_WIDTH, WINDOW_HEIGHT
from src.core.sound import Sound
from src.entities.entity import Entity
from src.entities.target import Target
from src.events.event_handler import Movement


class Player(Entity):
    def __init__(self, sprite_sheet, direction="left", cooldown=250, x=WINDOW_WIDTH // 2, y=WINDOW_HEIGHT - 55,
                 sprite_width=500, sprite_height=350, sprite_scale=0.22, row_index=0, steps=3,
                 min_speed=10, max_speed=10, collision_x_offset=5, collision_y_offset=3, collision_width=55,
                 collision_height=55, rotation=270):
        super().__init__(sprite_sheet, direction, cooldown, x, y, sprite_width, sprite_height, sprite_scale, row_index,
                         steps, min_speed, max_speed, collision_x_offset, collision_y_offset, collision_width,
                         collision_height)
        self.animation_list = self.sprite_sheet.sprite_animation(steps, sprite_width, sprite_height, sprite_scale,
                                                                 row_index, rotation)
        self.sound = Sound()

    # updates player position and speed based on user input
    def update(self):
        self.x, self.y, self.x_speed, self.y_speed, self.space_pressed = Movement.event_handler(self.x, self.y,
                                                                                                self.x_speed,
                                                                                                self.y_speed,
                                                                                                self.space_pressed)

    # Checks snowball boundaries, and resets where applicable
    def check_sprite_position(self):
        # Resets snowball when if it goes off-screen
        if self.y < 0 - self.collision_height:
            self.reset_player()

        # Keeps the sprite within screen bounds
        self.x = max(0, min(WINDOW_WIDTH - self.collision_width, self.x))

    # resets snowball to its initial y-pos and speed
    def reset_player(self):
        self.y = self.initial_y  # Resets to initial position on y-axis
        self.y_speed = 0
        self.space_pressed = False

    # returns collision boundaries for snowball and other entity
    def collision_boundaries(self, entity):
        self_rect = pygame.Rect(
            self.x + self.collision_x_offset,
            self.y + self.collision_y_offset,
            self.collision_width,
            self.collision_height)
        entity_rect = pygame.Rect(
            entity.x + entity.collision_x_offset,
            entity.y + entity.collision_y_offset,
            entity.collision_width,
            entity.collision_height // 2)
        return self_rect, entity_rect

    # receives health instance, so can be called during collision
    def check_collision(self, entity, health, score, seconds):
        self_rect, entity_rect = self.collision_boundaries(entity)
        # colliderect() - pygame method to check if two rects collide
        # extra parameter False required to prevent a collision every time the rects collide in one hit
        if self_rect.colliderect(entity_rect) and self.collision_state == False:
            self.reset_player()
            self.collision_state = True
            self.collision_action(entity, health, score, seconds)
        # If no collision, reset collision state
        elif not self_rect.colliderect(entity_rect):
            self.collision_state = False
        return True

    def collision_action(self, entity, health, score, seconds):
        if isinstance(entity, Target):
            self.sound.sound_effect("../assets/sounds/ouch.mp3")
            score.increment_score(seconds)
            entity.reset_target(entity)
        else:
            self.sound.sound_effect("../assets/sounds/snowball_hit.mp3")
            return health.take_damage()


if __name__ == '__main__':
    pass
