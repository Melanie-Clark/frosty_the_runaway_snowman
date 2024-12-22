import pygame
import sys


class Movement:

    @staticmethod
    def event_handler(x, y, x_speed, y_speed, move_amount=10):  # 0,0 stationary sprite
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # running = False - # is running even used anywhere??-------------
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_speed -= move_amount
                elif event.key == pygame.K_RIGHT:
                    x_speed += move_amount
                if event.key == pygame.K_UP:
                    y_speed -= move_amount
                elif event.key == pygame.K_DOWN:
                    y_speed += move_amount
                elif event.key == pygame.K_SPACE:  # ---------------add just for snowball -----------
                    y_speed -= move_amount
            elif event.type == pygame.KEYUP:  # keeps smooth running, so that speed only resets in relevant direction
                if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                    x_speed = 0
                if event.key in (pygame.K_UP, pygame.K_DOWN):
                    y_speed = 0

        x += x_speed
        y += y_speed

        return x, y, x_speed, y_speed
