import pygame

class Block:
    def __init__(self, brickWidth, brickHeight, brickColor):
        self.brickColor = brickColor
        self.brickWidth = brickWidth
        self.brickHeight = brickHeight
        self.bricks = []
        y_ofs = 20
        for i in range(7):
            x_ofs = 20
            for j in range(20):
                self.bricks.append(pygame.Rect(x_ofs, y_ofs, self.brickWidth, brickHeight))
                x_ofs += self.brickWidth + 2
            y_ofs += self.brickHeight + 2

    def draw_blocks(self, Display):
        for brick in self.bricks:
            pygame.draw.rect(Display, self.brickColor, brick)

    def getBricks(self):
        return self.bricks

    def setBricks(self, Bricks):
        self.bricks = Bricks