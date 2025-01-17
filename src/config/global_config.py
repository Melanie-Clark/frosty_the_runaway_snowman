import pygame

pygame.font.init()  # Initialises the font module

# screen configuration
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
FPS = 60

# UI font details
TITLE_FONT_NAME = "MV Boli"
TEXT_FONT_NAME = "Comic Sans"

FEATURE_COLOR = "red"
MENU_COLOR = (34, 139, 34)

TITLE_FONT = pygame.font.SysFont(TITLE_FONT_NAME, 100, bold=True)
MENU_FONT = pygame.font.SysFont(TEXT_FONT_NAME, 30, bold=True)
INSTRUCTIONS_FONT = pygame.font.SysFont(TEXT_FONT_NAME, 23, bold=True)
FEATURE_FONT = pygame.font.SysFont(TITLE_FONT_NAME, 65)
GAME_TEXT_FONT = pygame.font.SysFont(TEXT_FONT_NAME, 40)

# UI placement
TITLE_HEIGHT = 10

# Button standards
BUTTON_COLOR = (240, 255, 255)
BORDER_COLOR = (34, 139, 34)

# game states - text for debugging
MENU_SCREEN = "Menu Screen"
INSTRUCTION_SCREEN = "Instructions"
GAME_SCREEN = "In play"

NAUGHTY_SCREEN = "Naughty"
TIMES_UP_SCREEN = "Out of time"
GAME_OVER_SCREEN = "Game Over"
QUIT = "Quit"
