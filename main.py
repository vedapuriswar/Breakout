import pygame
import paddle
import ball
import Block


"""Screen Dimensions"""
width, height = 1280, 720

"""Paddle Dimensions"""
offset = 30
paddleWidth = 200
paddleHeight = 20
paddleX = (width/2) - (paddleWidth/2)
paddleY = height - paddleHeight - offset

"""Brick Dimensions"""
brickWidth = 60
brickHeight = 20

"""Ball Dimensions"""
ballDiameter = 20
ballRadius = int(ballDiameter/2)

"""Constraints"""
maxBallX = width - ballDiameter
maxBallY = height - ballDiameter

"""States"""
STATE_BALL_IN_PADDLE = 0
STATE_PLAYING = 1
STATE_WON = 2
STATE_GAME_OVER = 3

"""Colors"""
backgroundColor = [72, 75, 79]
brickColor = [255, 255, 0]
paddleColor = [255, 255, 255]
ballColor = [0, 255, 255]

class Game:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Breakout')
        self.FPSClock = pygame.time.Clock()
        self.display = pygame.display.set_mode([width, height])
        self.init_game()
        self.state = STATE_BALL_IN_PADDLE


    def check_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.state = STATE_PLAYING

    def collisions(self):
        brickArray = self.bricks.getBricks()
        for brick in brickArray:
            if self.ball.sphere.colliderect(brick):
                self.ball.velocity[1] = -self.ball.velocity[1]
                brickArray.remove(brick)
                break
        self.bricks.setBricks(brickArray)
        if len(self.bricks.getBricks()) is 0:
            self.state = STATE_WON
        if self.ball.sphere.colliderect(self.player.paddle):
            self.ball.sphere.top = paddleY - ballDiameter
            self.ball.velocity[1] = -self.ball.velocity[1]
        elif self.ball.sphere.top > self.player.paddle.top:
            self.state = STATE_GAME_OVER


    def init_game(self):
        self.player = paddle.Paddle(paddleX, paddleY, paddleWidth, paddleHeight, paddleColor)
        self.ball = ball.Ball(paddleX + paddleX/2, paddleY - ballRadius, ballRadius, [5, -5], maxBallX, maxBallY, ballColor)
        self.bricks = Block.Block(brickWidth, brickHeight, brickColor)

    def run(self):
        FPS = 60
        gameOver = False
        while not gameOver:
            for event in pygame.event.get():
                if event.type is pygame.QUIT:
                    gameOver = True
            self.display.fill(backgroundColor)
            mouseX = pygame.mouse.get_pos()[0]
            self.check_input()
            if self.state is STATE_PLAYING:
                self.ball.move(self.display)
                self.collisions()
                self.player.draw(self.display)
                self.bricks.draw_blocks(self.display)
                self.ball.draw(self.display)
            elif self.state is STATE_GAME_OVER:
                gameOver = True
            elif self.state is STATE_WON:
                gameOver = True
            self.player.move(mouseX)
            pygame.display.flip()
            pygame.display.update()
            self.FPSClock.tick(FPS)
Game().run()