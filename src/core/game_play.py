from src.config.global_config import GAME_SCREEN


class GameLoop:
    def __init__(self, game_state, health, score, scene, timer, target_and_obstacles, player,
                 all_entities):
        self.game_state = game_state
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
            result = player.check_collision(entity, self.health, self.score, seconds)
            if result != GAME_SCREEN:  # If collision changes state, return immediately
                return result
        return GAME_SCREEN

    def game_loop(self, timer_running):
        self.scene.draw_main_scene()
        self.score.draw()
        self.health.draw()
        print('GAME PLAY:', timer_running)
        # returns game state
        self.game_state, seconds = self.timer.countdown_timer(timer_running)

        if self.game_state == GAME_SCREEN:
            self.game_state = self.check_collision(self.target_and_obstacles, self.player, seconds)
            self.update_entities(self.all_entities)
        return self.game_state
