import pygame
from src.config.global_config import SCREEN_WIDTH, BUTTON_COLOR, MENU_FONT, BORDER_COLOR, MENU_COLOR, SCREEN_HEIGHT
from src.screens.base_screen import BaseScreen


class MenuScreen(BaseScreen):
    def __init__(self, screen, game_state_manager, scene, draw):
        super().__init__(screen, game_state_manager)
        self.scene = scene
        self.draw = draw
        self.title = "Frosty: The Runaway Snowman!"

    # Draw rectangle to hold menu options
    def draw_menu_box(self):
        box_width = SCREEN_WIDTH // 2.3
        x = SCREEN_WIDTH // 2 - (box_width // 2)
        y = SCREEN_HEIGHT // 2.8
        height = SCREEN_HEIGHT // 2.1

        pygame.draw.rect(self.screen, BUTTON_COLOR, (x, y, box_width, height), 0, 15)
        pygame.draw.rect(self.screen, BORDER_COLOR, (x, y, box_width, height), 6, 15)

    @staticmethod
    def menu_text():
        menu_options = (
            "Choose an option to continue:\n"
            "[I] Instructions\n"
            "[P] Play\n"
            "[H] High Score\n"
            "[Q] Quit\n"
        )
        return menu_options

    def draw_menu_options(self):
        y_pos = SCREEN_HEIGHT // 2.65
        menu_options = self.menu_text()

        for line in menu_options.splitlines():
            text = MENU_FONT.render(line, True, MENU_COLOR)
            self.screen.blit(text, (SCREEN_WIDTH // 3, y_pos))
            y_pos += text.get_height() * 1.5  # Moves position of next text below

    # draws everything required for menu screen
    def draw_menu_screen(self):
        self.scene.draw_main_scene()
        self.scene.draw_frosty(SCREEN_WIDTH // 6.4)
        self.scene.draw_snow()
        self.draw.draw_title(self.title)
        self.draw_menu_box()
        self.draw_menu_options()
        pygame.display.update()

    def run(self):
        self.draw_menu_screen()


if __name__ == "__main__":
    pass
