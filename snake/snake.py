import random
import sys
import time

import pygame

from . import GRID_SIZE, SCREEN_HEIGHT, SCREEN_WIDTH, UP, DOWN, LEFT, RIGHT
from .colors import Colors


class Snake:
    def __init__(self, screen):
        self.length = 1

        self.positions = [(
            (SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2)
        )]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])

        self.color = Colors.BLUE
        self.score = 0
        self.snake_speed = 2

        self.screen = screen

    def get_head_position(self):
        return self.positions[0]

    def turn(self, point):
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        else:
            self.direction = point

    def move(self):
        cur = self.get_head_position()
        x, y = self.direction

        new = (
            (cur[0] + (x * GRID_SIZE)) % SCREEN_WIDTH,
            (cur[1] + (y * GRID_SIZE)) % SCREEN_HEIGHT
        )

        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new)

            if len(self.positions) > self.length:
                self.positions.pop()

    def draw(self, surface):
        for p in self.positions:
            rect = pygame.Rect((p[0], p[1]), (GRID_SIZE, GRID_SIZE))

            pygame.draw.rect(surface, self.color, rect)
            pygame.draw.rect(surface, Colors.BLACK, rect, 1)

    def reset(self):
        self.length = 1
        self.positions = [((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.score = 0
        self.snake_speed = 2

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == ord('w'):
                    self.turn(UP)
                elif event.key == pygame.K_DOWN or event.key == ord('s'):
                    self.turn(DOWN)
                elif event.key == pygame.K_LEFT or event.key == ord('a'):
                    self.turn(LEFT)
                elif event.key == pygame.K_RIGHT or event.key == ord('d'):
                    self.turn(RIGHT)
                elif event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))
