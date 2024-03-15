import random
import pygame


class Paddle():
    def __init__(self, x, y, width, height, game):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.dy = 0
        self.score = 0
        self.game = game

    def update(self):
        if self.dy < 0:
            self.y = max(0, self.y + self.dy * self.game.dt)
        else:
            self.y = min(self.game.WINDOW_HEIGHT - 100, self.y + self.dy * self.game.dt)

    def render(self):
        pygame.draw.rect(self.game.screen, self.game.WHITE, pygame.Rect(self.x, self.y, 20, 100))


class AIPaddle(Paddle):
    def __init__(self, x, y, width, height, game):
        super().__init__(x, y, width, height, game)
        self.speed = 1.3
        self.game = game
        
    def update(self, ball):
        if ball.dx > 0:
            if ball.y < self.y:
                self.y =  self.y - self.speed * self.game.dt
            elif ball.y > self.y:
                self.y =  self.y + self.speed * self.game.dt
            else:
                pass

        

