import pygame
import sys


class Movement:

    # main event handler for game
    def event_handler(self, x, y, x_speed, y_speed, space_pressed, move_amount=10):  # 0,0 stationary sprite
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit_game()
            if event.type == pygame.KEYDOWN:  # action once per key press
                if event.key == pygame.K_LEFT and not space_pressed:  # stops snowball moving once thrown
                    x_speed -= move_amount
                elif event.key == pygame.K_RIGHT and not space_pressed:
                    x_speed += move_amount
                elif event.key == pygame.K_SPACE:
                    space_pressed = True  # set state to be able to stop item moving left or right when shooting up
                    y_speed -= move_amount
                elif event.key == pygame.K_q:  # added so that quit can be pressed during play
                    self.quit_game()
            elif event.type == pygame.KEYUP:  # keeps smooth running, so that speed only resets in relevant direction
                if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                    x_speed = 0

        x += x_speed
        y += y_speed

        return x, y, x_speed, y_speed, space_pressed

    @staticmethod
    def quit_game():
        pygame.quit()
        sys.exit()
