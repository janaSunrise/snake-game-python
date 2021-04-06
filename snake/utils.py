import pygame


def draw_grid(surface, grid_size, grid_height, grid_width):
    for y in range(0, int(grid_height)):
        for x in range(0, int(grid_width)):
            rect = pygame.Rect((x * grid_size, y * grid_size), (grid_size, grid_size))
            pygame.draw.rect(surface, (253, 231, 76), rect)
