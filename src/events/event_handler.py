import pygame
from src.config.global_config import INSTRUCTION_SCREEN, GAME_OVER_SCREEN, NAUGHTY_SCREEN, PLAY_SCREEN, MENU_SCREEN, \
    QUIT


class Events:

    @staticmethod
    def event_handler(game_state, instance, game_over_instance, game_instance):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return QUIT
            if event.type == pygame.KEYDOWN:  # action once per key press
                if event.key == pygame.K_q:  # added so that quit can be pressed during play
                    return QUIT

                elif game_state == MENU_SCREEN:
                    if event.key == pygame.K_i:
                        return INSTRUCTION_SCREEN
                    if event.key == pygame.K_p:
                        return PLAY_SCREEN
                    # if event.key == pygame.K_c: # credits placeholder

                elif game_state == MENU_SCREEN or game_state == INSTRUCTION_SCREEN:
                    if event.key == pygame.K_p:
                        return PLAY_SCREEN

                elif game_state == NAUGHTY_SCREEN:
                    if event.key == pygame.K_c:
                        return GAME_OVER_SCREEN

                elif game_state == GAME_OVER_SCREEN:
                    if event.key == pygame.K_p:
                        game_over_instance.reset_game(game_instance.target, game_instance.player)
                        return PLAY_SCREEN

                elif game_state == PLAY_SCREEN:
                    if event.key == pygame.K_SPACE:
                        instance.snowball_active = True  # set state to be able to stop item moving left or right when shooting up

        if game_state == PLAY_SCREEN:
            keys = pygame.key.get_pressed()  # Continuous movement when key held down
            if keys[pygame.K_LEFT] and not instance.snowball_active:  # stops snowball moving once thrown
                instance.x -= instance.speed
            elif keys[pygame.K_RIGHT] and not instance.snowball_active:
                instance.x += instance.speed

        return game_state


if __name__ == "__main__":
    pass
