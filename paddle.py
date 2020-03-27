import pygame

class Paddle:
    def __init__(self, posX, posY, width, height, paddleColor):
        self.posX = posX
        self.posY = posY
        self.width = width
        self.height = height
        self.paddle = pygame.Rect(posX, posY, width, height)
        self.paddleColor = paddleColor

    def draw(self, Display):
        pygame.draw.rect(Display, self.paddleColor, self.paddle)


    def move(self, mouseX):
        self.paddle.left = mouseX - (self.width/2)
