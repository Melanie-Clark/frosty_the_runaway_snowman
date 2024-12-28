import pygame
import sys


class Movement:

    @staticmethod
    def event_handler(x, y, x_speed, y_speed, move_amount=10):  # 0,0 stationary sprite
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN: # action once per key press
                if event.key == pygame.K_LEFT: # -----------change so can only shoot up in a straight line
                    x_speed -= move_amount
                elif event.key == pygame.K_RIGHT:
                    x_speed += move_amount
                elif event.key == pygame.K_SPACE:
                    y_speed -= move_amount
            elif event.type == pygame.KEYUP:  # keeps smooth running, so that speed only resets in relevant direction
                if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                    x_speed = 0

        x += x_speed
        y += y_speed

        return x, y, x_speed, y_speed
