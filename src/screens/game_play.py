from src.screens.base_screen import BaseScreen


class GameLoop(BaseScreen):
    def __init__(self, screen, game_state_manager, timer_running, health, score, scene, timer, target_and_obstacles, player,
                 all_entities):
        super().__init__(screen, game_state_manager)
        self.timer_running = timer_running
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

    def check_collision(self, target_and_obstacles, player, seconds):
        # checks collision for any obstacle or target
        for entity in target_and_obstacles:
            player.check_collision(entity, self.health, self.score, seconds)

    def game_loop(self, timer_running):
        self.scene.draw_main_scene()
        self.score.draw()
        self.health.draw()
        seconds = self.timer.countdown_timer(timer_running)

        if self.game_state_manager.get_state() == "game_play":
            self.check_collision(self.target_and_obstacles, self.player, seconds)
            self.update_entities(self.all_entities)

    def run(self):
        self.game_loop(self.timer_running)
        if not self.timer_running:
            # Resets timer when entering the play screen
            self.timer.reset()
            self.timer_running = True


if __name__ == "__main__":
    pass
