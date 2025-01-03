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
INSTRUCTIONS_FONT = pygame.font.SysFont(FONT_NAME, 25)
FEATURE_FONT = pygame.font.SysFont(FONT_NAME, 40)

# UI placement
TITLE_HEIGHT = 10
