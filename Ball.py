import random
import pygame

class Ball():
    def __init__(self, x, y, width, height) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.dy = random.choice([1,-1])
        self.dx = random.choice([0.5,-0.5])
    
    def reset(self, game):
        self.x = game.VIRTUAL_WIDTH / 2 - 2
        self.y = game.VIRTUAL_HEIGHT / 2 - 2
        self.dy = random.choice([1,-1])
        self.dx = random.choice([0.5,-0.5])

    def update(self, dt):
        self.x = self.x + self.dx * dt
        self.y = self.y + self.dy * dt

    def render(self, game):
        pygame.draw.rect(game.screen, game.WHITE, pygame.Rect(self.x, self.y, 20, 20))
