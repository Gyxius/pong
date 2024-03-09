import random
import pygame


class Paddle():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.dy = 0
        self.score = 0

    def update(self, game):
        if self.dy < 0:
            self.y = max(0, self.y + self.dy * game.dt)
        else:
            self.y = min(game.WINDOW_HEIGHT - 100, self.y + self.dy * game.dt)

    def render(self, game):
        pygame.draw.rect(game.screen, game.WHITE, pygame.Rect(self.x, self.y, 20, 100))


class AIPaddle(Paddle):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.speed = 1.3
        
    def update(self, ball, game):
        if ball.dx > 0:
            if ball.y < self.y:
                self.y =  self.y - self.speed * game.dt
            elif ball.y > self.y:
                self.y =  self.y + self.speed * game.dt
            else:
                pass

        

