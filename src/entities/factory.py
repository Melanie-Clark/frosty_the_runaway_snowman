import random

from src.config.global_config import SCREEN_WIDTH
from src.entities.obstacle import Obstacle, FlyingObstacle
from src.entities.player import Player
from src.entities.sprites import AnimatedSprite
from src.entities.target import Target


class EntityFactory:
    # Loads spritesheets
    def __init__(self, screen):
        self.screen = screen
        self.player = None

    @staticmethod
    def initialise_spritesheets():
        bunny_sprite = AnimatedSprite("assets/sprite_sheets/bunny_sprite_sheet.png")
        elf_sprite = AnimatedSprite("assets/sprite_sheets/elf_sprite_sheet.png")
        reindeer_sprite = AnimatedSprite("assets/sprite_sheets/reindeer_sprite_sheet.png")
        red_santa_sprite = AnimatedSprite("assets/sprite_sheets/red_santa_sprite_sheet.png")
        frosty_sprite = AnimatedSprite("assets/sprite_sheets/frosty_sprite_sheet.png", True)
        snowball_sprite = AnimatedSprite("assets/sprite_sheets/snowball_sprite_sheet.png")
        return bunny_sprite, elf_sprite, reindeer_sprite, red_santa_sprite, frosty_sprite, snowball_sprite

    # initialises all entities
    def initialise_entities(self):
        bunny_sprite, elf_sprite, reindeer_sprite, red_santa_sprite, frosty_sprite, snowball_sprite = self.initialise_spritesheets()
        self.player = Player(self.screen, snowball_sprite)

        sprite_width = {"reindeer": 128, "elf": 32, "red_santa": 64, "bunny": 55, "snowman": 93.5}
        sprite_height = {"reindeer": 128, "elf": 64, "red_santa": 64, "bunny": 74, "snowman": 140}

        random_x_position = random.randint(0, SCREEN_WIDTH)

        bunny = Obstacle(self.screen, bunny_sprite, random.choice(["left", "right"]), 150,
                         random.randint(0 - sprite_width["bunny"], SCREEN_WIDTH + sprite_width["bunny"]),
                         400, 500,
                         sprite_width["bunny"], sprite_height["bunny"],
                         2, 2, 4, 2, 5,
                         10, 55, 92, 90)

        elf_group = [(Obstacle(self.screen, elf_sprite, random.choice(["left", "right"]), 100,
                               random.randint(0 - sprite_width["elf"], SCREEN_WIDTH + sprite_width["elf"]),
                               200, 475,
                               sprite_width["elf"], sprite_height["elf"],
                               2, 2, 6, 3, 6,
                               8, 26, 46, 102))
                     for _ in range(3)]

        red_santa = Obstacle(self.screen, red_santa_sprite, random.choice(["left", "right"]), 75,
                             random.randint(0 - sprite_width["red_santa"], SCREEN_WIDTH + sprite_width["red_santa"]),
                             100, 425,
                             sprite_width["red_santa"], sprite_height["red_santa"],
                             1.75, 2, 4, 3, 5,
                             30, 5, 55, 108)

        reindeer_group = [
            (FlyingObstacle(self.screen, reindeer_sprite, "left", 200,
                            random_x_position + (i * sprite_width["reindeer"]), -20,
                            sprite_width["reindeer"], sprite_height["reindeer"],
                            1, 2, 2, 3, 3,
                            20, 18, 100, 110))
            for i in range(4)]

        target = Target(self.screen, frosty_sprite, random.choice(["left", "right"]), 150,
                        random_x_position, 200, 400,
                        sprite_width["snowman"], sprite_height["snowman"],
                        0.75, 1, 5, 2, 2,
                        6, 5, 60, 85)

        obstacles = [*reindeer_group, *elf_group, red_santa, bunny]
        all_entities = obstacles + [target, self.player]
        target_and_obstacles = obstacles + [target]

        return target, self.player, all_entities, target_and_obstacles


if __name__ == "__main__":
    pass
