import pygame
import sys

from sprite_sheet import SpriteSheet
from event_handler import Movement
from game_window import GameWindow


# main game loop
class GameLoop:
    def __init__(self, display_width, display_height, sprite_width, sprite_height, sprite_scale, row_index):
        self.game_window = GameWindow(display_width, display_height)  # GameWindow instance
        self.DISPLAY_WIDTH = display_width
        self.DISPLAY_HEIGHT = display_height
        self.sprite_width = sprite_width
        self.sprite_height = sprite_height
        self.sprite_scale = sprite_scale
        self.row_index = row_index

    def run(self):

        bunny = SpriteSheet("../assets/images/bunny_sprite_sheet.png")

        animation_steps = 4
        animation_cooldown = 150  # how quickly animation runs (milliseconds)
        frame = 0

        x = 0
        y = 0

        # stationary sprite
        x_speed = 0
        y_speed = 0

        bunny_animation_list = bunny.sprite_animation(animation_steps, self.sprite_width, self.sprite_height,
                                                      self.sprite_scale, self.row_index)
        last_update = pygame.time.get_ticks()  # time of execution

        # Keeps window open until quit
        running = True
        while running:

            self.game_window.draw_background()
            self.game_window.draw_trees()
            self.game_window.draw_mountains()

            x, y, x_speed, y_speed, running = Movement.event_handler(x, y, x_speed, y_speed, running)

            # Keep the bunny within screen bounds
            x = max(0, min(self.DISPLAY_WIDTH - (self.sprite_width * 2), x))
            y = max(0, min(self.DISPLAY_HEIGHT - (self.sprite_height * 2), y))

            current_time = pygame.time.get_ticks()

            if current_time - last_update >= animation_cooldown:
                frame = (frame + 1)
                last_update = current_time  # resets time
                if frame >= len(bunny_animation_list):
                    frame = 0

            # animation
            self.game_window.display.blit(bunny_animation_list[frame], (x, y))

            pygame.display.update()  # flip refreshes entire display surface / update - partial updates for performance
            self.game_window.clock.tick(60)  # Limit to 60 frames per second

        pygame.quit()
        sys.exit()


if __name__ == '__main__':
    game = GameLoop(1200, 700, 55, 74, 2, 2)
    game.run()
