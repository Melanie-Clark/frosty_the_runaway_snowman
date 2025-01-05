import random

from src.config.global_config import WINDOW_WIDTH
from src.entitites.entity import Entity


class Target(Entity):
    def __init__(self, sprite_sheet, direction, cooldown, x, min_y_range, max_y_range, sprite_width, sprite_height,
                 sprite_scale, row_index, steps, min_speed, max_speed, collision_x_offset, collision_y_offset,
                 collision_width, collision_height):
        super().__init__(sprite_sheet, direction, cooldown, x, None, sprite_width, sprite_height, sprite_scale,
                         row_index,
                         steps, min_speed, max_speed, collision_x_offset, collision_y_offset, collision_width,
                         collision_height)
        self.min_y_range = min_y_range
        self.max_y_range = max_y_range
        self.y = random.randint(self.min_y_range, self.max_y_range)

    def check_sprite_position(self):
        # Resets if entity moves off-screen
        if self.x > WINDOW_WIDTH or self.x < -self.sprite_width:
            if self.direction == "left":
                self.direction = "right"
            else:
                self.direction = "left"

            if self.x > WINDOW_WIDTH:
                self.x = WINDOW_WIDTH  # Resets to left edge
                self.y = random.randint(self.min_y_range, self.max_y_range)
                # if target goes off-screen, it returns from the same side
            elif self.x < -self.sprite_width:
                self.x = -self.sprite_width
                self.y = random.randint(self.min_y_range, self.max_y_range)

if __name__ == "__main__":
    pass