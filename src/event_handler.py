import pygame


class Movement:

    @staticmethod
    def event_handler(x, y, x_speed, y_speed, running, move_amount=10):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_speed -= move_amount
                elif event.key == pygame.K_RIGHT:
                    x_speed += move_amount
                if event.key == pygame.K_UP:
                    y_speed -= move_amount
                elif event.key == pygame.K_DOWN:
                    y_speed += move_amount
            elif event.type == pygame.KEYUP:
                if event.key in (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN):
                    x_speed = 0
                    y_speed = 0

        x += x_speed
        y += y_speed

        return x, y, x_speed, y_speed, running