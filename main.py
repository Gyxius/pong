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
        self.winning_score = 2

        self.sounds = {
            'paddle_hit' : 'sounds/paddle_hit.wav',
            'score' : 'sounds/score.wav',
            'wall_hit' : 'sounds/wall_hit.wav'
        }

        self.screen = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        pygame.display.set_caption('Pong')

        self.text_font = pygame.font.Font('font.ttf', 20)
        self.text = self.text_font.render('Hello Pong!', True, self.WHITE)
        self.start_text = self.text_font.render('Hello Start State!', True, self.WHITE)
        self.play_text = self.text_font.render('Hello Play State!', True, self.WHITE)
        self.score_font = pygame.font.Font('font.ttf', 120)
        self.PADDLE_SPEED = 200
        self.gameState = 'start'
        self.dt = 0.6
        self.servingPlayer = 1

        self.player1 = Paddle(20, 60, 20, 100)
        self.player2 =AIPaddle(self.WINDOW_WIDTH - 40, self.WINDOW_HEIGHT - 200, 20, 100)
        self.ball = Ball(self.WINDOW_WIDTH // 2 - 50, self.WINDOW_HEIGHT // 2 - 100, 4, 4)
    
    def update(self):
        self.player2.update(self.ball, self)
        if self.gameState == 'serve':
            self.ball.dy = random.choice([-1,1])
            if self.servingPlayer == 1:
                self.ball.dx = random.choice([0.5,0.5])
            else:
                self.ball.dx = -random.choice([0.5,0.5])

        if self.gameState == 'play':
            if self.ball.collides(self.player1):
                self.ball.dx = -self.ball.dx * 1.03
                self.ball.x = self.player1.x + 20
                if self.ball.dy < 0:
                    self.ball.dy = -random.randint(1, 3)
                else:
                    self.ball.dy = random.randint(1, 3)
                
                pygame.mixer.music.load(self.sounds['paddle_hit'])
                pygame.mixer.music.play(0)

            if self.ball.collides(self.player2):
                self.ball.dx = -self.ball.dx * 1.03
                self.ball.x = self.player2.x - 20
                if self.ball.dy < 0:
                    self.ball.dy = -random.randint(1, 3)
                else:
                    self.ball.dy = random.randint(1, 3)
                
                pygame.mixer.music.load(self.sounds['paddle_hit'])
                pygame.mixer.music.play(0)

            if self.ball.y <= 0:
                self.ball.y = 0
                self.ball.dy = -self.ball.dy
                pygame.mixer.music.load(self.sounds['wall_hit'])
                pygame.mixer.music.play(0)

            if self.ball.y >= self.WINDOW_HEIGHT - 4:
                self.ball.y = self.WINDOW_HEIGHT - 4
                self.ball.dy = -self.ball.dy
                pygame.mixer.music.load(self.sounds['wall_hit'])
                pygame.mixer.music.play(0)

        if self.ball.x < 0:
            self.servingPlayer = 1
            self.player2.score += 1
            pygame.mixer.music.load(self.sounds['score'])
            pygame.mixer.music.play(0)
            self.ball.reset(self)
            if self.player2.score  >= self.winning_score:
                self.winningPlayer = 2
                self.gameState = 'done'
            else:
                self.gameState = 'serve'
                self.ball.reset(self)

        if self.ball.x > self.WINDOW_WIDTH:
            self.servingPlayer = 2
            self.player1.score += 1
            pygame.mixer.music.load(self.sounds['score'])
            pygame.mixer.music.play(0)
            self.ball.reset(self)
            if self.player1.score  >= self.winning_score:
                self.winningPlayer = 1
                self.gameState = 'done'
            else:
                self.gameState = 'serve'
                self.ball.reset(self)

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
                elif event.key == K_RETURN:
                    if self.gameState == 'start':
                        self.gameState = 'serve'
                    elif self.gameState == 'serve':
                        self.gameState = 'serve'
                        self.gameState = 'play'
                    elif self.gameState == 'done':
                        self.gameState = 'serve'
                        self.ball.reset(game)
                        self.player1.score = 0
                        self.player2.score = 0
                        if self.winningPlayer == 1:
                            self.servingPlayer = 2
                        else:
                            self.servingPlayer = 1
        if self.gameState == 'play':
            self.ball.update(self.dt)

    def draw(self):
        # Score
        score1 = self.score_font.render(str(self.player1.score), True, self.WHITE)
        score2 = self.score_font.render(str(self.player2.score), True, self.WHITE)
        self.screen.blit(score1, (self.WINDOW_WIDTH//2 - 200 + 30, self.WINDOW_HEIGHT//2 - 200))
        self.screen.blit(score2, (self.WINDOW_WIDTH//2 + 40, self.WINDOW_HEIGHT//2 - 200))
        
        if self.gameState == 'start':
            self.welcome_text = self.text_font.render('Welcome to Pong!', True, self.WHITE)
            self.press_enter_text = self.text_font.render('Press Enter to begin!', True, self.WHITE)
            self.screen.blit(self.welcome_text, (self.WINDOW_WIDTH//2 - 100, 50))
            self.screen.blit(self.press_enter_text, (self.WINDOW_WIDTH//2 - 100, 80))
        
        elif self.gameState == 'serve':
            self.player_serve_text = self.text_font.render('Player ' + str(self.servingPlayer) + "'s serve!", True, self.WHITE)
            self.press_enter_to_serve_text = self.text_font.render('Press Enter to serve!', True, self.WHITE)
            self.screen.blit(self.player_serve_text, (self.WINDOW_WIDTH//2 - 100, 50))
            self.screen.blit(self.press_enter_to_serve_text, (self.WINDOW_WIDTH//2 - 100, 80))

        elif self.gameState == 'play':
            pass

        elif self.gameState == 'done':
            self.player_wins_text = self.text_font.render('Player ' + str(self.servingPlayer) + " wins!", True, self.WHITE)
            self.press_enter_to_restart_text = self.text_font.render('Press Enter to restart!', True, self.WHITE)
            self.screen.blit(self.player_wins_text, (self.WINDOW_WIDTH//2 - 100, 50))
            self.screen.blit(self.press_enter_to_restart_text, (self.WINDOW_WIDTH//2 - 100, 80))

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


    