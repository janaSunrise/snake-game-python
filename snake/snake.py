import random
import sys

import pygame

from . import GRID_SIZE, SCREEN_HEIGHT, SCREEN_WIDTH, UP, DOWN, LEFT, RIGHT


class Snake:
    def __init__(self):
        self.length = 1

        self.positions = [(
            (SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2)
        )]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])

        self.color = (64, 224, 208)
        self.score = 0

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
            ((cur[0] + (x * GRID_SIZE)) % SCREEN_WIDTH),
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
            pygame.draw.rect(surface, (17, 24, 47), rect, 1)

    def reset(self):
        self.length = 1
        self.positions = [((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.score = 0

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn(UP)
                elif event.key == pygame.K_DOWN:
                    self.turn(DOWN)
                elif event.key == pygame.K_LEFT:
                    self.turn(LEFT)
                elif event.key == pygame.K_RIGHT:
                    self.turn(RIGHT)
