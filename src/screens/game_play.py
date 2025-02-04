from src.screens.base_screen import BaseScreen


class GameLoop(BaseScreen):
    def __init__(self, screen, game_state_manager, health, score, scene, timer, target_and_obstacles, player,
                 all_entities):
        super().__init__(screen, game_state_manager)
        self.health = health
        self.score = score
        self.scene = scene
        self.timer = timer
        self.target_and_obstacles = target_and_obstacles
        self.player = player
        self.all_entities = all_entities

    @staticmethod
    def update_entities(all_entities):
        for entity in all_entities:
            entity.update()
            entity.check_sprite_position()
            entity.draw()
            entity.update_frame()

    def check_collision(self, target_and_obstacles, player):
        # checks collision for any obstacle or target
        for entity in target_and_obstacles:
            player.check_collision(entity, self.health, self.score)

    def game_loop(self):
        self.scene.draw_main_scene()
        self.score.draw()
        self.health.draw()
        self.timer.countdown_timer()

        if self.game_state_manager.get_state() == "game_play":
            self.check_collision(self.target_and_obstacles, self.player)
            self.update_entities(self.all_entities)

    def run(self):
        self.game_loop()
        timer_running = self.timer.get_state()
        if not timer_running:
            # Resets timer when entering the play screen
            self.timer.reset()
            self.timer.set_state(True)


if __name__ == "__main__":
    pass
