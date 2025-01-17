import pygame
from src.config.global_config import SCREEN, WINDOW_WIDTH, BUTTON_COLOR, MENU_FONT, MENU_SCREEN, \
    BORDER_COLOR, MENU_COLOR
from src.core.instructions import InstructionScreen
from src.utils.utils import Draw


class MenuScreen:
    def __init__(self, scene):
        self.scene = scene
        self.draw = Draw()
        self.title = "Frosty: The Runaway Snowman!"
        self.game_state = MENU_SCREEN
        self.instruction_screen = InstructionScreen()

    # Draw rectangle to hold menu options
    @staticmethod
    def draw_menu_box():
        box_width = 550
        x = WINDOW_WIDTH // 2 - (box_width // 2)
        y = 270
        height = 390

        pygame.draw.rect(SCREEN, BUTTON_COLOR, (x, y, box_width, height), 0, 15)
        pygame.draw.rect(SCREEN, BORDER_COLOR, (x, y, box_width, height), 6, 15)

    @staticmethod
    def menu_text():
        menu_options = (
            "Choose an option to continue:\n"
            "[I] Instructions\n"
            "[P] Play\n"
            "[C] Credits (coming soon)\n"
            "[Q] Quit\n"
        )
        return menu_options

    def draw_menu_options(self):
        y_pos = 300
        menu_options = self.menu_text()

        for line in menu_options.splitlines():
            text = MENU_FONT.render(line, True, MENU_COLOR)
            SCREEN.blit(text, (430, y_pos))
            y_pos += text.get_height() * 1.5  # Moves position of next text below

    # draws everything required for menu screen
    def draw_menu_screen(self):
        self.scene.draw_main_scene()
        self.scene.draw_frosty(200)
        self.scene.draw_snow()
        self.draw.draw_title(self.title)
        self.draw_menu_box()
        self.draw_menu_options()
        pygame.display.update()


if __name__ == "__main__":
    pass
