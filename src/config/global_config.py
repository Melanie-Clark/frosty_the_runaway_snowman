import pygame

pygame.font.init()  # Initializes the font module

# screen configuration
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
FPS = 60

# UI font details
FONT_NAME = "Verdana"

FEATURE_COLOR = "red"
INSTRUCTIONS_COLOR = "dark green"

TITLE_FONT = pygame.font.SysFont(FONT_NAME, 60)
INSTRUCTIONS_FONT = pygame.font.SysFont(FONT_NAME, 22)
FEATURE_FONT = pygame.font.SysFont(FONT_NAME, 40)

BUTTON_FONT = pygame.font.SysFont(FONT_NAME, 20, bold=True)

# UI placement
TITLE_HEIGHT = 10

# Button standards
BUTTON_COLOUR = (240, 248, 255)  # Light frosty background
BORDER_COLOUR = (173, 216, 230)  # Icy blue background

BUTTON_WIDTH = 220
BUTTON_HEIGHT = 50

# game states - text for debugging
MENU_SCREEN = "Menu Screen"
INSTRUCTION_SCREEN = "Instructions"
PLAY_SCREEN = "Play"
NAUGHTY_SCREEN = "Naughty"
GAME_OVER_SCREEN = "Game Over"
QUIT = "Quit"
