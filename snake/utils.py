import pygame

from . import SCREEN_WIDTH, SCREEN_HEIGHT, font
from .colors import Colors


def flash(screen, message, color):
    msg = font.render(message, True, color)
    screen.blit(msg, [SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2])


def draw_grid(surface, grid_size, grid_height, grid_width):
    for y in range(0, int(grid_height)):
        for x in range(0, int(grid_width)):
            if (x + y) % 2 == 0:
                r = pygame.Rect((x * grid_size, y * grid_size), (grid_size, grid_size))
                pygame.draw.rect(surface, Colors.DARK_BLUE, r)
            else:
                rr = pygame.Rect((x * grid_size, y * grid_size), (grid_size, grid_size))
                pygame.draw.rect(surface, Colors.LESS_DARK_BLUE, rr)
