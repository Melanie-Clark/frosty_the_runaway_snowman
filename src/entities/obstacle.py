import random

from src.config.global_config import SCREEN_WIDTH
from src.entities.entity import Entity


class Obstacle(Entity):
    def __init__(self, screen, sprite_sheet, direction, cooldown, x, min_y_range, max_y_range, sprite_width,
                 sprite_height, sprite_scale, row_index, steps, min_speed, max_speed, collision_x_offset,
                 collision_y_offset, collision_width, collision_height):
        super().__init__(screen, sprite_sheet, direction, cooldown, x, None, sprite_width, sprite_height,
                         sprite_scale, row_index, steps, min_speed, max_speed, collision_x_offset, collision_y_offset,
                         collision_width, collision_height)
        self.min_y_range = min_y_range
        self.max_y_range = max_y_range
        self.y = self._get_random_y()

    # protected helper method for use in this class only
    def _get_random_y(self):
        return random.randint(self.min_y_range, self.max_y_range)

    def check_sprite_position(self):
        # Resets if entity moves off-screen
        if self.x > SCREEN_WIDTH or self.x < -self.sprite_width * 2:
            self.y = self._get_random_y()
            self.direction = random.choice(["left", "right"])
            self.speed = self.get_random_speed()

            if self.x > SCREEN_WIDTH:
                self.x = -self.sprite_width * 2  # Resets to left edge
            elif self.x < -self.sprite_width * 2:
                self.x = SCREEN_WIDTH


class FlyingObstacle(Entity):
    def __init__(self, screen, sprite_sheet, direction, cooldown, x, y, sprite_width, sprite_height, sprite_scale,
                 row_index, steps, min_speed, max_speed, collision_x_offset, collision_y_offset, collision_width,
                 collision_height):
        super().__init__(screen, sprite_sheet, direction, cooldown, x, y, sprite_width, sprite_height, sprite_scale,
                         row_index, steps, min_speed, max_speed, collision_x_offset, collision_y_offset,
                         collision_width, collision_height)

    def check_sprite_position(self):
        # Resets if obstacle moves off-screen
        if self.x < -(self.sprite_width * 2):
            self.x = SCREEN_WIDTH + (self.sprite_width * 3)  # Resets to right side of screen


if __name__ == "__main__":
    pass
