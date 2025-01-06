import random

from src.config.global_config import WINDOW_WIDTH
from src.entities.entity import Entity


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
        self.y = self._get_random_y()

    # protected helper method for use in this class only
    def _get_random_y(self):
        return random.randint(self.min_y_range, self.max_y_range)

    def check_sprite_position(self):
        # Resets if target moves off-screen
        if self.x > WINDOW_WIDTH or self.x < -self.sprite_width:
            if self.direction == "left":
                self.direction = "right"
            else:
                self.direction = "left"

            if self.x > WINDOW_WIDTH:
                self.x = WINDOW_WIDTH  # Resets to left edge
                # if target goes off-screen, it returns from the same side
            elif self.x < -self.sprite_width:
                self.x = -self.sprite_width
            self.y = self._get_random_y()

    @staticmethod
    def reset_target(entity):
        # resets target to disappear and re-enter from left or right side, increases speed
        entity.x = random.choice((0, WINDOW_WIDTH))
        entity.y = random.randint(entity.min_y_range, entity.max_y_range)
        entity.speed += 0.65


if __name__ == "__main__":
    pass
