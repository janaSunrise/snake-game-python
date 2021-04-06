import pygame

SCREEN_HEIGHT, SCREEN_WIDTH = 480, 480

# Controls
UP = 0, -1
DOWN = 0, 1
LEFT = -1, 0
RIGHT = 1, 0

# Window grid
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH / GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT / GRID_SIZE

# Pygame variables
pygame.init()

font = pygame.font.SysFont("monospace", 16)
