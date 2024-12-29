import pygame

from src.core.global_config import WINDOW_WIDTH, WINDOW_HEIGHT, SCREEN
from src.events.sprites import SpriteSheet
from abc import ABC, abstractmethod
from src.events.event_handler import Movement


class Entity(ABC):
    def __init__(self, sprite_sheet, cooldown, x, y, sprite_width, sprite_height, sprite_scale, row_index, steps, speed,
                 direction, rotation, collision_x_offset, collision_y_offset, collision_width, collision_height,
                 x_speed=0, y_speed=0):
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
        self.last_update = pygame.time.get_ticks()  # time of last frame update
        self.frame = 0
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.animation_list = self.sprite_sheet.sprite_animation(steps, sprite_width, sprite_height, sprite_scale,
                                                                 row_index, rotation)
        self.collision_state = False

        # collision box sizes
        self.collision_x_offset = collision_x_offset
        self.collision_y_offset = collision_y_offset
        self.collision_width = collision_width
        self.collision_height = collision_height

        self.space_pressed = False

    @staticmethod
    def initialise_entities():
        # Loads spritesheets
        snowball_sprite = SpriteSheet("../assets/sprite_sheets/snowball_sprite_sheet.png")
        bunny_sprite_left = SpriteSheet("../assets/sprite_sheets/bunny_sprite_sheet.png")
        bunny_sprite_right = SpriteSheet("../assets/sprite_sheets/bunny_sprite_sheet.png", True)
        elf_sprite_right = SpriteSheet("../assets/sprite_sheets/elf_sprite_sheet.png", True)
        snow_thief_sprite = SpriteSheet("../assets/sprite_sheets/snow_thief_sprite_sheet.png", True)
        reindeer_sprite_left = SpriteSheet("../assets/sprite_sheets/reindeer_sprite_sheet.png")
        red_santa_sprite = SpriteSheet("../assets/sprite_sheets/red_santa_sprite_sheet.png")
        green_santa_sprite = SpriteSheet("../assets/sprite_sheets/green_santa_sprite_sheet.png")
        cheeky_thief_sprite = SpriteSheet("../assets/sprite_sheets/cheeky_sprite_sprite_sheet.png")

        # cooldown - how quickly animation runs (milliseconds) ------------------------RE-ORDER ----- use random for speed, x, y coords--
        snowball = Item(snowball_sprite, 250, 0, WINDOW_HEIGHT - 55, 500, 350, 0.22, 0, 3, 10, "left", 270, 5,
                        3, 55, 55)

        # bunny_group = []
        # for i in range(3):
        #     bunny_group.append(Obstacle(bunny_sprite, 150, random.randint(0, WINDOW_WIDTH), random.randint(220, WINDOW_HEIGHT - 100), 55, 74, 2, 2, 4,
        #                   random.randint(1, 4), random.choice(["left", "right"]), 0, 10,
        #                   55, 92, 90))

        bunny1 = Obstacle(cheeky_thief_sprite, 150, WINDOW_WIDTH // 1.2, WINDOW_HEIGHT // 1.5, 93.5, 140, 0.75, 1, 5,
                          5, "right", 0, 5,
                          5, 65, 85)
        # bunny1 = Obstacle(bunny_sprite_left, 150, WINDOW_WIDTH // 1.2, WINDOW_HEIGHT // 1.5, 55, 74, 2, 2, 4,
        #                   3, "left", 0, 10,
        #                   55, 92, 90)
        bunny2 = Obstacle(bunny_sprite_right, 150, WINDOW_WIDTH // 3.2, WINDOW_HEIGHT // 1.6, 55, 74, 2, 2, 4,
                          3.5, "right", 0, 10,
                          55, 92, 90)
        bunny3 = Obstacle(bunny_sprite_left, 150, WINDOW_WIDTH // 2.3, WINDOW_HEIGHT // 2.3, 55, 74, 2, 2, 4,
                          4, "left", 0, 10,
                          55, 92, 90)

        elf = Obstacle(elf_sprite_right, 100, WINDOW_WIDTH // 3, WINDOW_HEIGHT // 3.9, 32, 64, 2, 2, 6, 4,
                       "right", 0, 8,
                       26, 46, 102)

        reindeer1 = Obstacle(reindeer_sprite_left, 200, WINDOW_WIDTH // 1.2, -20, 128, 128, 1, 2, 2,
                             3, "left", 0, 20, 18, 100, 110)

        snow_thief = Obstacle(snow_thief_sprite, 100, 0, WINDOW_HEIGHT // 2.5, 57, 70, 1.5, 0, 6, 5, "left", 0, 4, 0,
                              75, 103)

        red_santa = Obstacle(red_santa_sprite, 100, WINDOW_WIDTH // 3.8, WINDOW_HEIGHT // 3.1, 64, 64, 1.5, 1, 4,
                             4, "right", 0, 10, 0, 65, 96)
        green_santa = Target(green_santa_sprite, 200, WINDOW_WIDTH // 2.1, WINDOW_HEIGHT // 2.1, 64, 64, 1.5, 1, 4,
                             2.53, "right", 0, 10, 0, 65, 96)

        return [green_santa, red_santa, reindeer1, elf, bunny1, bunny2, bunny3, snow_thief, snowball]

    @abstractmethod
    def update(self):
        pass

    def update_frame(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_update >= self.animation_cooldown:
            self.frame = (self.frame + 1) % len(self.animation_list)  # Loops back to the first frame
            self.last_update = current_time  # resets time

    # draw to screen
    def draw(self, screen):
        SCREEN.blit(self.animation_list[self.frame], (self.x, self.y))  # draws to screen
        # uncomment to debug collisions (puts red box around each sprite)
        # pygame.draw.rect(SCREEN, (255, 0, 0),
        #                  pygame.Rect(self.x + self.collision_x_offset, self.y + self.collision_y_offset,
        #                              self.collision_width, self.collision_height), 2)


# update methods the same in Obstacle and Target, but need to defined differently somehow - could be in instantiation, rather than separate classes?
class Obstacle(Entity):
    def update(self):
        if self.direction == "right":
            self.x += self.speed  # Move to the right
        elif self.direction == "left":
            self.x -= self.speed  # Move to the left

        # Resets if entity moves off-screen
        if self.x > WINDOW_WIDTH:
            self.x = -self.sprite_width  # Resets to left edge
        elif self.x < -self.sprite_width:
            self.x = WINDOW_WIDTH


class Target(Entity):
    def update(self):
        if self.direction == "right":
            self.x += self.speed  # Move to the right
        elif self.direction == "left":
            self.x -= self.speed  # Move to the left

        # Resets if entity moves off-screen
        if self.x > WINDOW_WIDTH:
            self.x = -self.sprite_width  # Resets to left edge
        elif self.x < -self.sprite_width:
            self.x = WINDOW_WIDTH


class Item(Entity):

    def update(self):
        self.x, self.y, self.x_speed, self.y_speed, self.space_pressed = Movement.event_handler(self.x, self.y,
                                                                                                self.x_speed,
                                                                                                self.y_speed,
                                                                                                self.space_pressed)
        # Resets snowball when if it goes off-screen
        if self.y < 0 - self.collision_height:
            self.y = self.initial_y  # Resets to initial position on y-axis
            self.y_speed = 0
            self.space_pressed = False

        # # Keeps the sprite within screen bounds
        self.x = max(0, min(WINDOW_WIDTH - self.collision_width, self.x))

    def collision_boundaries(self, entity):
        self_rect = pygame.Rect(self.x + self.collision_x_offset, self.y + self.collision_y_offset,
                                self.collision_width, self.collision_height)
        entity_rect = pygame.Rect(entity.x + entity.collision_x_offset, entity.y + entity.collision_y_offset,
                                  entity.collision_width, entity.collision_height // 2)
        return self_rect, entity_rect

    def handle_collision(self, entity, health, score):  # receives health instance, so can be called during collision
        self_rect, entity_rect = self.collision_boundaries(entity)
        # ------snowball collides halfway for targets but not for obstacles--------------------------------------
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
            else:
                return health.take_damage()
        # If no collision, reset collision state
        elif not self_rect.colliderect(entity_rect):
            self.collision_state = False
        return True


if __name__ == '__main__':
    pass
