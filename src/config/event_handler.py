import sys
import pygame


class EventHandler:
    def __init__(self, game_state_manager, game, player, game_over):
        self.game_state_manager = game_state_manager
        self.game_play = game
        self.game_over = game_over
        self.player = player

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or ((event.type == pygame.KEYDOWN) and (event.key == pygame.K_q)):
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:  # action once per key press
                if (self.game_state_manager.get_state() == "main_menu") or (
                        self.game_state_manager.get_state() == "instructions") or (
                        self.game_state_manager.get_state() == "high_score"):
                    if event.key == pygame.K_p:
                        self.game_state_manager.set_state("game_play")

                    if self.game_state_manager.get_state() == "main_menu":
                        if event.key == pygame.K_i:
                            self.game_state_manager.set_state("instructions")
                        if event.key == pygame.K_h:
                            self.game_state_manager.set_state("high_score")
                    else:
                        if event.key == pygame.K_m:
                            self.game_state_manager.set_state("main_menu")


                elif self.game_state_manager.get_state() == "game_play":
                    if event.key == pygame.K_SPACE:
                        # set state to be able to stop item moving left or right when shooting up
                        self.player.snowball_active = True

                elif self.game_state_manager.get_state() == "naughty_screen":
                    if event.key == pygame.K_RETURN:
                        self.game_state_manager.set_state("game_over")

                elif self.game_state_manager.get_state() == "game_over":
                    if event.key == pygame.K_p or event.key == pygame.K_m:
                        self.game_over.reset_game(self.game_play.target, self.game_play.player)
                        if event.key == pygame.K_p:
                            self.game_state_manager.set_state("game_play")
                        if event.key == pygame.K_m:
                            self.game_state_manager.set_state("main_menu")

        if self.game_state_manager.get_state() == "game_play":
            keys = pygame.key.get_pressed()  # Continuous movement when key held down
            if keys[pygame.K_LEFT] and not self.player.snowball_active:  # stops snowball moving once thrown
                self.player.x -= self.player.speed
            elif keys[pygame.K_RIGHT] and not self.player.snowball_active:
                self.player.x += self.player.speed


if __name__ == "__main__":
    pass
