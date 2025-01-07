import pygame
import sys


class Events:

    @staticmethod
    def event_handler(game_state, instance, game_instance):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Events.quit_game()
            if event.type == pygame.KEYDOWN:  # action once per key press
                if event.key == pygame.K_q:  # added so that quit can be pressed during play
                    Events.quit_game()

                elif game_state == "Welcome":
                    if event.key == pygame.K_p:  # added so that quit can be pressed during play
                        print(instance)
                        instance.game_loop()

                elif game_state == "GameOver":
                    if event.key == pygame.K_p:
                        instance.reset_game(game_instance.target, game_instance.player)
                        game_instance.game_loop()


                elif game_state == "Naughty":
                    if event.key == pygame.K_c:
                        instance.load_game_over(game_instance)


                elif game_state == "Play":
                    if event.key == pygame.K_SPACE:
                        instance.snowball_active = True  # set state to be able to stop item moving left or right when shooting up

        if game_state == "Play":
            keys = pygame.key.get_pressed()  # Continuous movement when key held down

            if keys[pygame.K_LEFT] and not instance.snowball_active:  # stops snowball moving once thrown
                instance.x -= instance.speed
                # self.direction = "left"
            elif keys[pygame.K_RIGHT] and not instance.snowball_active:
                instance.x += instance.speed
                # self.direction = "right"

    @staticmethod
    def quit_game():
        pygame.quit()
        sys.exit()
