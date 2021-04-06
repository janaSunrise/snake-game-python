import pygame

from . import GRID_SIZE, GRID_HEIGHT, GRID_WIDTH, SCREEN_HEIGHT, SCREEN_WIDTH
from .colors import Colors
from .food import Food
from .snake import Snake
from .utils import draw_grid

if __name__ == '__main__':
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    draw_grid(surface, GRID_SIZE, GRID_HEIGHT, GRID_WIDTH)

    snake = Snake()
    food = Food()

    font = pygame.font.SysFont("monospace", 16)
    high_score = 0

    while True:
        clock.tick(snake.snake_speed)
        snake.handle_keys()
        draw_grid(surface, GRID_SIZE, GRID_HEIGHT, GRID_WIDTH)

        snake.move()

        if snake.get_head_position() == food.position:
            snake.length += 1
            snake.score += 1
            snake.snake_speed += 1

            food.randomize_position()

            if snake.score > high_score:
                high_score = snake.score

        snake.draw(surface)
        food.draw(surface)
        screen.blit(surface, (0, 0))

        score = font.render(f"Score: {snake.score}", True, Colors.WHITE)
        high_score_ = font.render(f"High Score: {high_score}", True, Colors.WHITE)

        screen.blit(score, (5, 10))
        screen.blit(high_score_, (5, 26))

        pygame.display.update()

