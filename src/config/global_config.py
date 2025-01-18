import pygame

pygame.font.init()  # Initialises the font module

# screen configuration
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
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
