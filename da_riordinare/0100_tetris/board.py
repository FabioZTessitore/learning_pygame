import random
from shapes import I_Shape, J_Shape, L_Shape, O_Shape, S_Shape, T_Shape, Z_Shape
from block import Block
from colors import BLACK

class Board:
    def __init__(self, width=10, height=20, blockSize=30):
        self.width = width
        self.height = height
        self.blockSize = blockSize
        self.grid = []
        self.createNewShape()

    def createNewShape(self):
        shapes = [
            I_Shape((4, 1), self.blockSize),
            J_Shape((4, 1), self.blockSize),
            L_Shape((4, 1), self.blockSize),
            O_Shape((4, 1), self.blockSize),
            S_Shape((4, 1), self.blockSize),
            T_Shape((4, 1), self.blockSize),
            Z_Shape((4, 1), self.blockSize)
        ]
        self.currentShape = random.choice(shapes)

    def canMoveCurrentShape(self, delta):
        # canMove on the board
        canMove = self.currentShape.canMove(delta, self.width, self.height)

        # intersect with grid?
        if canMove:
            for blockPosition in self.currentShape.blocks:
                x, y = blockPosition
                dx, dy = delta
                blockPosition = (x+dx, y+dy)
                canMove = canMove and not (blockPosition in self.grid)
        
        dx, dy = delta
        if not canMove and dy == 1:
            self.addShapeToGrid()
        return canMove

    def moveCurrentShape(self, delta):
        self.currentShape.move(delta)


    def addShapeToGrid(self):
        print "arrivato"
        for blockPosition in self.currentShape.blocks:
            self.grid.append(blockPosition)
        self.createNewShape()

        print self.grid

    def draw(self, screen):
        for blockPosition in self.grid:
            b = Block(self.blockSize)
            b.draw(screen, blockPosition, BLACK)
        self.currentShape.draw(screen)



if __name__ == '__main__':
    import pygame
    from colors import RED, WHITE

    SCREENSIZE = (300, 600)

    board = Board()

    pygame.init()
    
    screen = pygame.display.set_mode(SCREENSIZE)
    pygame.display.set_caption("Testing Block")

    clock = pygame.time.Clock()

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                done = True
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            delta = (-1, 0)
        elif keys[pygame.K_RIGHT]:
            delta = (1, 0)
        elif keys[pygame.K_DOWN]:
            delta = (0, 1)
        else:
            delta = (0, 0)

        if board.canMoveCurrentShape(delta):
            board.moveCurrentShape(delta)
    
        screen.fill(WHITE)

        board.draw(screen)

        pygame.display.flip()

        clock.tick(30)

    pygame.quit()