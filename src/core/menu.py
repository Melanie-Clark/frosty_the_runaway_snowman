import pygame
from src.config.global_config import SCREEN, WINDOW_WIDTH, BUTTON_COLOUR, BORDER_COLOUR, BUTTON_FONT, BUTTON_WIDTH, \
    BUTTON_HEIGHT, MENU_SCREEN
from src.core.instructions import InstructionScreen
from src.utils.utils import Draw


class MenuScreen:
    def __init__(self, scene):
        self.scene = scene
        self.draw = Draw()
        self.title = "Frosty: The runaway snowman!"
        self.game_state = MENU_SCREEN
        self.instruction_screen = InstructionScreen()

    @staticmethod
    def draw_button(x, y, width, height, text):
        # Draw button rectangle
        pygame.draw.rect(SCREEN, BUTTON_COLOUR, (x, y, width, height))
        pygame.draw.rect(SCREEN, BORDER_COLOUR, (x, y, width, height), 4, 10)

        # Render and center the text
        text_surface = BUTTON_FONT.render(text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(x + width // 2, y + height // 2))  # adds text to centre of button
        SCREEN.blit(text_surface, text_rect)

    # Example usage:
    def draw_menu_buttons(self):
        x_center = WINDOW_WIDTH // 2
        game_length_buttons_y_pos = 250

        centered_button_x = x_center - BUTTON_WIDTH // 2

        menu_y_pos = 350
        menu_button_text_list = [
            "I - Instructions",
            "P - Play",
            "C - Credits",
            "Q - Quit"
        ]

        for button_text in menu_button_text_list:
            self.draw_button(centered_button_x, menu_y_pos, BUTTON_WIDTH, BUTTON_HEIGHT, button_text)
            menu_y_pos += 100

        self.draw_button(centered_button_x * 0.5, game_length_buttons_y_pos, BUTTON_WIDTH, BUTTON_HEIGHT,
                         "S - Short Game")
        self.draw_button(centered_button_x, game_length_buttons_y_pos, BUTTON_WIDTH, BUTTON_HEIGHT, "M - Medium Game")
        self.draw_button(centered_button_x * 1.5, game_length_buttons_y_pos, BUTTON_WIDTH, BUTTON_HEIGHT,
                         "L - Long Game")

    # draws everything required for menu screen
    def draw_menu_screen(self):
        self.scene.draw_main_scene()
        self.draw.draw_title(self.title)
        self.scene.draw_frosty(200)
        self.draw_menu_buttons()
        pygame.display.update()


if __name__ == "__main__":
    pass
