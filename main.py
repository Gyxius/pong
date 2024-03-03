import pygame
import sys
from pygame.locals import *
from Ball import *
from Paddle import *

class Game:

    def __init__(self):
        pygame.init()
        self.WINDOW_WIDTH = 1280
        self.WINDOW_HEIGHT = 720
        self.WHITE = (255, 255, 255)
        self.GREEN = (0, 255, 0)
        self.BLUE = (0, 0, 128)
        self.BACKGROUND_COLOR =  (40, 45, 52, 255)

        self.screen = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))

        self.text_font = pygame.font.Font('font.ttf', 20)
        self.text = self.text_font.render('Hello Pong!', True, self.WHITE)
        self.score_font = pygame.font.Font('font.ttf', 120)
        self.PADDLE_SPEED = 200
        self.gameState = 'start'
        self.dt = 0.4

        self.player1 = Paddle(20, 60, 20, 100)
        self.player2 = Paddle(self.WINDOW_WIDTH - 40, self.WINDOW_HEIGHT - 200, 20, 100)
        self.ball = Ball(self.WINDOW_WIDTH // 2 - 50, self.WINDOW_HEIGHT // 2 - 100, 4, 4)
    
    def update(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == K_z:
                    self.player1.dy = -self.PADDLE_SPEED
                    self.player1.update(self)
                elif event.key == K_s:
                    self.player1.dy = self.PADDLE_SPEED
                    self.player1.update(self)
                elif event.key == K_UP:
                    self.player2.dy = -self.PADDLE_SPEED
                    self.player2.update(self)
                elif event.key == K_DOWN:
                    self.player1.dy = self.PADDLE_SPEED
                    self.player2.update(self)
                elif event.key == K_RETURN:
                    print("Enter")
                    if self.gameState == 'start':
                        self.gameState = 'play'
                    else:
                        self.gameState = 'start'

        if self.gameState == 'play':
            self.ball.update(self.dt)

    def draw(self):
        # Score
        score1 = self.score_font.render(str(self.player1.score), True, self.WHITE)
        score2 = self.score_font.render(str(self.player2.score), True, self.WHITE)
        self.screen.blit(score1, (self.WINDOW_WIDTH//2 + 40, self.WINDOW_HEIGHT//2 - 200))
        self.screen.blit(score2, (self.WINDOW_WIDTH//2 - 200 + 30, self.WINDOW_HEIGHT//2 - 200))

        # Hello Pong Text
        self.screen.blit(self.text, (self.WINDOW_WIDTH//2 - 100, 50))

        # First Paddle
        self.player1.render(self)
        # Second Paddle
        self.player2.render(self)

        # Ball 
        self.ball.render(self)
        
        pygame.display.update()

    def gameLoop(self):
        while True:
            self.screen.fill(self.BACKGROUND_COLOR)
            self.update()
            self.draw()


if __name__ == "__main__":
    game = Game()
    game.gameLoop()


    