import pygame

class Ball:
    def __init__(self, posX, posY, radius, velocity, maxBallX, maxBallY, ballColor):
        self.posX = int(posX)
        self.posY = int(posY)
        self.radius = radius
        self.velocity = velocity
        self.maxBallX = maxBallX
        self.maxBallY = maxBallY
        self.sphere = pygame.Rect(posX, posY, radius, radius)
        self.ballColor = ballColor

    def draw(self, Display):
        pygame.draw.rect(Display, self.ballColor, self.sphere)


    def move(self, Display):
        self.Display = Display
        self.sphere.left += self.velocity[0]
        self.sphere.top += self.velocity[1]
        if self.sphere.left <= 0:
            self.sphere.left = 0
            self.velocity[0] = -self.velocity[0]
        elif self.sphere.left >= self.maxBallX:
            self.sphere.left = self.maxBallX
            self.velocity[0] = -self.velocity[0]
        if self.sphere.top < 0:
            self.sphere.top = 0
            self.velocity[1] = -self.velocity[1]
        elif self.sphere.top >= self.maxBallY:
            self.sphere.top = self.maxBallY
            self.velocity[1] = -self.velocity[1]



