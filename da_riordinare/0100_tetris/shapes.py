from block import Block
from colors import BLUE, ORANGE, CYAN, RED, GREEN, YELLOW, PURPLE

class Shape:
    def __init__(self, blocks, blockSize=30):
        self.blocks = blocks
        self.blockSize = blockSize

    def canMove(self, delta, boardWidth, boardHeight):
        for blockPosition in self.blocks:
            b = Block()
            if not b.canMove(blockPosition, delta, boardWidth, boardHeight):
                return False

        return True

    def move(self, delta):
        dx, dy = delta
        newBlocks = []
        for coord in self.blocks:
            x, y = coord
            newBlocks.append( (x+dx, y+dy) )
        self.blocks = newBlocks

    def draw(self, screen):
        for point in self.blocks:
            b = Block(self.blockSize)
            b.draw(screen, point, self.color)

class I_Shape(Shape):
    def __init__(self, center, blockSize):
        x, y = center
        blocks = [ (x-2, y), (x-1, y), (x, y), (x+1, y) ]
        self.color = BLUE
        Shape.__init__(self, blocks, blockSize)

class J_Shape(Shape):
    def __init__(self, center, blockSize):
        x, y = center
        blocks = [ (x-1, y), (x, y), (x+1, y), (x+1, y+1) ]
        self.color = ORANGE
        Shape.__init__(self, blocks, blockSize)

class L_Shape(Shape):
    def __init__(self, center, blockSize):
        x, y = center
        blocks = [ (x-1, y), (x, y), (x+1, y), (x-1, y+1) ]
        self.color = CYAN
        Shape.__init__(self, blocks, blockSize)

class O_Shape(Shape):
    def __init__(self, center, blockSize):
        x, y = center
        blocks = [ (x-1, y), (x, y), (x, y+1), (x-1, y+1) ]
        self.color = RED
        Shape.__init__(self, blocks, blockSize)

class S_Shape(Shape):
    def __init__(self, center, blockSize):
        x, y = center
        blocks = [ (x-1, y+1), (x, y), (x, y+1), (x+1, y) ]
        self.color = GREEN
        Shape.__init__(self, blocks, blockSize)

class T_Shape(Shape):
    def __init__(self, center, blockSize):
        x, y = center
        blocks = [ (x-1, y), (x, y), (x, y+1), (x+1, y) ]
        self.color = YELLOW
        Shape.__init__(self, blocks, blockSize)

class Z_Shape(Shape):
    def __init__(self, center, blockSize):
        x, y = center
        blocks = [ (x-1, y), (x, y), (x, y+1), (x+1, y+1) ]
        self.color = PURPLE
        Shape.__init__(self, blocks, blockSize)

if __name__ == '__main__':
    import pygame
    from colors import RED, WHITE

    SCREENSIZE = (300, 300)

    zShape = Z_Shape( (3, 3) )

    pygame.init()
    
    screen = pygame.display.set_mode(SCREENSIZE)
    pygame.display.set_caption("Testing Block")

    clock = pygame.time.Clock()

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                done = True
    
        screen.fill(WHITE)

        zShape.draw(screen)

        pygame.display.flip()

        clock.tick(10)

    pygame.quit()
