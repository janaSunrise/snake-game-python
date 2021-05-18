import pygame

from . import GRID_SIZE, GRID_HEIGHT, GRID_WIDTH, SCREEN_HEIGHT, SCREEN_WIDTH
from .colors import Colors
from .food import Food
from .snake import Snake
from .utils import draw_grid


class Game:
    def __init__(self):
        pygame.init()

        self.font = pygame.font.SysFont("monospace", 16)
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

        pygame.display.set_caption("Snake game python")

        self.surface = pygame.Surface(self.screen.get_size())
        self.surface = self.surface.convert()

        self.snake = Snake(self.screen)
        self.food = Food()

        self.score = None
        self.high_score = 0
        self.high_score_ = None

        # Draw the grid
        draw_grid(self.surface, GRID_SIZE, GRID_HEIGHT, GRID_WIDTH)

    def update_score(self):
        self.score = self.font.render(f"Score: {self.snake.score}", True, Colors.WHITE)
        self.high_score_ = self.font.render(f"High Score: {self.high_score}", True, Colors.WHITE)

        self.screen.blit(self.score, (5, 10))
        self.screen.blit(self.high_score_, (5, 26))

    def redraw_graphics(self):
        self.clock.tick(self.snake.snake_speed)
        self.snake.handle_keys()

        draw_grid(self.surface, GRID_SIZE, GRID_HEIGHT, GRID_WIDTH)

        self.snake.move()

        if self.snake.get_head_position() == self.food.position:
            if self.snake.score % 2 == 0:
                self.snake.snake_speed += 1

            self.snake.length += 1
            self.snake.score += 1

            self.food.randomize_position()

            if self.snake.score > self.high_score:
                self.high_score = self.snake.score

        self.snake.draw(self.surface)
        self.food.draw(self.surface)
        self.screen.blit(self.surface, (0, 0))

    def update_screen(self):
        while True:
            self.redraw_graphics()
            self.update_score()

            pygame.display.update()


if __name__ == '__main__':
    game = Game()
    game.update_screen()

