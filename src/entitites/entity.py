import pygame
import random

from src.core.global_config import WINDOW_WIDTH, WINDOW_HEIGHT, SCREEN
from src.entitites.sprites import AnimatedSprite
from abc import ABC, abstractmethod
from src.events.event_handler import Movement


class Entity(ABC):  # inherits functionality from pygames Sprite class
    def __init__(self, sprite_sheet, direction, cooldown, x, y, sprite_width, sprite_height, sprite_scale, row_index,
                 steps, min_speed, max_speed, collision_x_offset, collision_y_offset, collision_width,
                 collision_height,
                 x_speed=0, y_speed=0):
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
        self.speed = random.randint(self.min_speed, self.max_speed)
        self.initial_min_speed = min_speed
        self.last_update = pygame.time.get_ticks()  # time of last frame update
        self.frame = 0
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.animation_list = self.sprite_sheet.sprite_animation(steps, sprite_width, sprite_height, sprite_scale,
                                                                 row_index)
        self.collision_state = False
        self.space_pressed = False

        # collision box sizes
        self.collision_x_offset = collision_x_offset
        self.collision_y_offset = collision_y_offset
        self.collision_width = collision_width
        self.collision_height = collision_height

    @staticmethod
    def initialise_entities():
        # Loads spritesheets
        snowball_sprite = AnimatedSprite("../assets/sprite_sheets/snowball_sprite_sheet.png")
        bunny_sprite = AnimatedSprite("../assets/sprite_sheets/bunny_sprite_sheet.png")
        elf_sprite = AnimatedSprite("../assets/sprite_sheets/elf_sprite_sheet.png")
        reindeer_sprite = AnimatedSprite("../assets/sprite_sheets/reindeer_sprite_sheet.png")
        red_santa_sprite = AnimatedSprite("../assets/sprite_sheets/red_santa_sprite_sheet.png")
        runaway_snowman_sprite = AnimatedSprite("../assets/sprite_sheets/runaway_sprite_sprite_sheet.png", True)

        sprite_width = {"reindeer": 128, "elf": 32, "red_santa": 64, "bunny": 55, "snowman": 93.5, "snowball": 500}
        sprite_height = {"reindeer": 128, "elf": 64, "red_santa": 64, "bunny": 74, "snowman": 140, "snowball": 350}

        random_x_position = random.randint(0, WINDOW_WIDTH)

        reindeer_group = [
            (FlyingObstacle(reindeer_sprite, "left", 200, random_x_position + (i * sprite_width["reindeer"]), -20,
                            sprite_width["reindeer"], sprite_height["reindeer"], 1, 2, 2,
                            3, 3, 20, 18, 100, 110)) for i in range(5)]

        bunny_group = [(Obstacle(bunny_sprite, random.choice(["left", "right"]), 150,
                                 random.randint(0 - sprite_width["bunny"], WINDOW_WIDTH + sprite_width["bunny"]),
                                 random.randint(400, WINDOW_HEIGHT - (sprite_height["bunny"] * 3)),
                                 sprite_width["bunny"], sprite_height["bunny"], 2, 2, 4,
                                 2, 5, 10, 55, 92, 90)) for _ in range(2)]

        runaway_snowman = Target(runaway_snowman_sprite, random.choice(["left", "right"]), 150,
                                 random_x_position, random.randint(200, WINDOW_HEIGHT // 2), sprite_width["snowman"],
                                 sprite_height["snowman"], 0.75, 1, 5, 2, 2, 5, 5, 62, 85)

        elf_group = [
            (Obstacle(elf_sprite, random.choice(["left", "right"]), 100,
                      random.randint(0 - 32, WINDOW_WIDTH + sprite_width["elf"]),
                      random.randint(180, WINDOW_HEIGHT - (sprite_height["elf"] * 3)), sprite_width["elf"],
                      sprite_height["elf"], 2, 2, 6, 3,
                      6, 8, 26, 46, 102)) for _ in range(3)]

        red_santa = Obstacle(red_santa_sprite, random.choice(["left", "right"]), 75,
                             random.randint(0 - 64, WINDOW_WIDTH + sprite_width["red_santa"]),
                             random.randint(180, WINDOW_HEIGHT - (sprite_height["red_santa"] * 3)),
                             sprite_width["red_santa"],
                             sprite_height["red_santa"], 1.75, 2,
                             4, 3, 5, 25, 5, 60, 108)

        snowball = Item(snowball_sprite, "left", 250, WINDOW_WIDTH // 2, WINDOW_HEIGHT - 55, sprite_width["snowball"],
                        sprite_height["snowball"], 0.22, 0, 3, 10, 10,
                        5, 3, 55, 55, 270)

        return [*reindeer_group, *elf_group, red_santa, *bunny_group], runaway_snowman, snowball

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


class Obstacle(Entity):
    def check_sprite_position(self):
        # Resets if entity moves off-screen
        if self.x > WINDOW_WIDTH:
            self.x = -self.sprite_width  # Resets to left edge
            self.y = random.randint(210, WINDOW_HEIGHT - (self.sprite_height * 3))
            self.direction = random.choice(["left", "right"])
            self.speed = random.randint(self.min_speed, self.max_speed)
        elif self.x < -self.sprite_width:
            self.x = WINDOW_WIDTH
            self.y = random.randint(210, WINDOW_HEIGHT - (self.sprite_height * 3))
            self.direction = random.choice(["left", "right"])
            self.speed = random.randint(self.min_speed, self.max_speed)


class FlyingObstacle(Entity):
    def check_sprite_position(self):
        # Resets if obstacle moves off-screen
        if self.x < 0 - (self.sprite_width * 2):
            self.x = WINDOW_WIDTH + (self.sprite_width * 3)  # Resets to right side of screen


class Target(Entity):
    def check_sprite_position(self):
        # Resets if entity moves off-screen
        if self.x > WINDOW_WIDTH:
            self.x = WINDOW_WIDTH  # Resets to left edge
            self.y = random.randint(200, WINDOW_HEIGHT // 2)
            # if target goes off-screen, it returns from the same side
            if self.direction == "left":
                self.direction = "right"
            else:
                self.direction = "left"
        elif self.x < -self.sprite_width:
            self.x = -self.sprite_width
            self.y = random.randint(200, WINDOW_HEIGHT // 2)
            if self.direction == "left":
                self.direction = "right"
            else:
                self.direction = "left"


class Item(Entity):
    def __init__(self, sprite_sheet, direction, cooldown, x, y, sprite_width, sprite_height, sprite_scale, row_index,
                 steps, min_speed, max_speed, collision_x_offset, collision_y_offset, collision_width, collision_height,
                 rotation):
        super().__init__(sprite_sheet, direction, cooldown, x, y, sprite_width, sprite_height, sprite_scale, row_index,
                         steps, min_speed, max_speed, collision_x_offset, collision_y_offset, collision_width,
                         collision_height)
        self.rotation = rotation
        self.animation_list = self.sprite_sheet.sprite_animation(steps, sprite_width, sprite_height, sprite_scale,
                                                                 row_index, rotation)

    def update(self):
        self.x, self.y, self.x_speed, self.y_speed, self.space_pressed = Movement.event_handler(self.x, self.y,
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
            self.y = WINDOW_HEIGHT - self.collision_height
            self.y_speed = 0
            self.collision_state = True
            self.space_pressed = False
            if isinstance(entity, Target):
                score.increment_score()
                entity.x = random.randint(0, WINDOW_WIDTH)
                entity.y = random.randint(200, WINDOW_HEIGHT // 2)
                entity.speed += 0.85
            else:
                return health.take_damage()
        # If no collision, reset collision state
        elif not self_rect.colliderect(entity_rect):
            self.collision_state = False
        return True


if __name__ == '__main__':
    pass
