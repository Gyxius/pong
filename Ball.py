import random
import pygame

class Ball():
    def __init__(self, x, y, width, height, game) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.dy = random.choice([1,-1])
        self.dx = random.choice([1,-1])
        self.game = game
    
    def reset(self):
        self.x = self.game.WINDOW_WIDTH // 2 - 50
        self.y = self.game.WINDOW_HEIGHT // 2 - 100
        self.dy = random.choice([1,-1])
        self.dx = random.choice([1,-1])

    def update(self, dt):
        self.x = self.x + self.dx * dt
        self.y = self.y + self.dy * dt

    def render(self):
        pygame.draw.rect(self.game.screen, self.game.WHITE, pygame.Rect(self.x, self.y, 20, 20))

    def collides(self, paddle):
        if self.x > paddle.x + paddle.width or paddle.x > self.x + self.width:
            return False
        if self.y > paddle.y + paddle.height or paddle.y > self.y + self.height:
            return False
        return True