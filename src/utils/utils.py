from src.config.global_config import WINDOW_WIDTH, SCREEN, TITLE_FONT, FEATURE_COLOR, TITLE_HEIGHT, \
    FEATURE_FONT, INSTRUCTIONS_COLOR


# class available for use across the game project
class Draw:
    @staticmethod
    def draw_title(title):
        # render creates a surface (graphical object) for text to be displayed
        title_font = TITLE_FONT.render(title, False, FEATURE_COLOR)  # antialias (TRUE smooth text)
        # draws rendered text onto screen (SCREEN)
        SCREEN.blit(title_font, (WINDOW_WIDTH // 2 - title_font.get_width() // 2, TITLE_HEIGHT))

    @staticmethod
    def draw_text(text, font, color, y_pos):
        for line in text.splitlines():
            text = font.render(line, False, color)
            SCREEN.blit(text, (WINDOW_WIDTH // 2 - text.get_width() // 2, y_pos))
            y_pos += text.get_height()  # Moves position of next text to the line below

    # draws menu options for welcome and game over screens
    def draw_menu_options(self, menu_options="Press P to Play or Q to Quit"):
        self.draw_text(menu_options, FEATURE_FONT, INSTRUCTIONS_COLOR, 650)
