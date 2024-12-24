from abc import abstractmethod
import pygame
from global_config import *
from event_handler import Movement
from game_loop import GameLoop
from sprite_sheet import SpriteSheet


# ----------CONSIDER STANDARDISING GAMELOOP.DISPLAY (circular display) VS SELF.DISPLAY - scene/health

class Entity:
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
        self.last_update = pygame.time.get_ticks()  # time of execution
        self.frame = 0
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.animation_list = self.sprite_sheet.sprite_animation(self.animation_steps, self.sprite_width,
                                                                 self.sprite_height,
                                                                 self.sprite_scale, self.row_index, rotation)
        self.score = 0
        self.collision_state = False

        # collision box sizes
        self.collision_x_offset = collision_x_offset
        self.collision_y_offset = collision_y_offset
        self.collision_width = collision_width
        self.collision_height = collision_height
        # self.health = Health(GameLoop.DISPLAY)  # Health instance
        # self.health = health

    @staticmethod
    def initialise_entities():
        bunny_sprite_left = SpriteSheet("../assets/images/bunny_sprite_sheet.png", False)
        bunny_sprite_right = SpriteSheet("../assets/images/bunny_sprite_sheet.png", True)
        snowball_sprite = SpriteSheet("../assets/images/snowball_sprite_sheet.png", False)
        snowman_sprite = SpriteSheet("../assets/images/snowman_sprite_sheet.png", False)

        # cooldown - how quickly animation runs (milliseconds) ------------------------RE-ORDER
        snowball = Item(snowball_sprite, 250, 0, DISPLAY_HEIGHT - 50, 500, 350, 0.22, 0, 3, 10, "left", 270, 5,
                        3, 55, 55)

        bunny1 = Obstacle(bunny_sprite_left, 150, DISPLAY_WIDTH // 1.2, DISPLAY_HEIGHT // 1.5, 55, 74, 2, 2, 4,
                          3, "left", 0, 8,
                          55, 100, 95)
        bunny2 = Obstacle(bunny_sprite_right, 150, DISPLAY_WIDTH // 3.2, DISPLAY_HEIGHT // 1.6, 55, 74, 2, 2, 4,
                          3.5, "right", 0, 8,
                          55, 100, 95)
        snowman1 = Target(snowman_sprite, 150, 0, DISPLAY_HEIGHT // 1.7, 16, 16, 6, 0, 6, 6, "right", 0, 0, 0,
                          100, 95)
        bunny3 = Obstacle(bunny_sprite_left, 150, DISPLAY_WIDTH // 2.3, DISPLAY_HEIGHT // 2.3, 55, 74, 2, 2, 4,
                          4, "left", 0, 8,
                          55, 100, 95)
        snowman2 = Target(snowman_sprite, 150, 0, DISPLAY_HEIGHT // 2.5, 16, 16, 6, 0, 6, 4, "left", 0, 0, 0,
                          100, 95)
        bunny4 = Obstacle(bunny_sprite_right, 150, DISPLAY_WIDTH // 3, DISPLAY_HEIGHT // 3.9, 55, 74, 2, 2, 4, 5,
                          "right", 0, 8,
                          55, 100, 95)
        snowman3 = Target(snowman_sprite, 150, DISPLAY_WIDTH // 3.8, DISPLAY_HEIGHT // 4.1, 16, 16, 6, 0, 6,
                          2.53, "right", 0, 0, 0, 100, 95)

        return snowman3, bunny4, bunny1, snowman2, bunny3, snowman1, bunny2, snowball

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
        # used for debugging - puts red box around each sprite
        # pygame.draw.rect(GameLoop.DISPLAY, (255, 0, 0),
        #                  pygame.Rect(self.x + self.collision_x_offset, self.y + self.collision_y_offset, self.collision_width, self.collision_height), 2)


class Obstacle(Entity):
    def update(self):
        if self.direction == "right":
            self.x += self.speed  # Move to the right
        elif self.direction == "left":
            self.x -= self.speed  # Move to the left

        # Resets when entity moves off-screen
        if self.x > DISPLAY_WIDTH:  # If the entity moves off the right edge
            self.x = -self.sprite_width  # Reset to the left edge
        elif self.x < -self.sprite_width:  # If the entity moves off the left edge
            self.x = DISPLAY_WIDTH  # Reset to the right edge


class Target(Entity):
    def update(self):
        if self.direction == "right":
            self.x += self.speed  # Move to the right
        elif self.direction == "left":
            self.x -= self.speed  # Move to the left

        # Resets when entity moves off-screen
        if self.x > DISPLAY_WIDTH:  # If the entity moves off the right edge
            self.x = -self.sprite_width  # Reset to the left edge
        elif self.x < -self.sprite_width:  # If the entity moves off the left edge
            self.x = DISPLAY_WIDTH  # Reset to the right edge


class Item(Entity):

    def update(self):
        self.x, self.y, self.x_speed, self.y_speed = Movement.event_handler(self.x, self.y, self.x_speed,
                                                                            self.y_speed)

        # Resets snowball when it goes off-screen
        if self.y < 0:  # If the snowball moves off the top of the screen
            self.y = self.initial_y  # Reset to the bottom edge
            self.y_speed = 0

        # # Keeps the sprite within screen bounds
        self.x = max(0, min(DISPLAY_WIDTH - 50, self.x))  # 50 needs to be hard-coded -------------------------------

    def collision(self, entity, health): # receives health instance, so can be called during collision
        self_rect = pygame.Rect(self.x + self.collision_x_offset, self.y + self.collision_y_offset,
                                self.collision_width, self.collision_height)
        entity_rect = pygame.Rect(entity.x + self.collision_x_offset, entity.y + self.collision_y_offset,
                                  entity.collision_width, entity.collision_height)
        if self_rect.colliderect(entity_rect) and self.collision_state == False:
            self.y = DISPLAY_HEIGHT - 50  # 50 needs to be hard-coded ---------------------------------------------
            self.y_speed = 0
            self.collision_state = True
            if isinstance(entity, Target):
                self.score += 1
                print('Total Score:', self.score)
            else:
                print('collision', health)
                return health.take_damage()
        # If no collision, reset the collision state
        elif not self_rect.colliderect(entity_rect):
            self.collision_state = False
        return True


if __name__ == '__main__':
    pass
