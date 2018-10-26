import pygame
import random

BLOCK_SIZE = 5
BOARD_WIDTH = 120
BOARD_HEIGHT = 120

SCREENSIZE = (WIDTH, HEIGHT) = (BOARD_WIDTH * BLOCK_SIZE, BOARD_HEIGHT * BLOCK_SIZE)

WHITE = (255, 255, 255)
RED = (255, 0, 0)

BGCOLOR = WHITE
BLOCK_COLOR = RED

class Block:
    def __init__(self, alive):
        self.alive = alive

    def draw(self, screen, pos):
        y, x = pos
        pygame.draw.rect(screen, BLOCK_COLOR, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = {}
        self.createBlocks()

    def createBlocks(self):
        for r in range(self.height):
            for c in range(self.width):
                self.cells[(r,c)] = Block(False)

    def seed(self, coords):
        for pos in coords:
            self.cells[pos].alive = True

    def getBlockNeighbors(self, pos):
        y, x = pos
        neighbors = []
        for r in range(y-1, y+2):
            for c in range(x-1, x+2):
                if (r,c) != pos and self.cells.get((r,c)):
                    neighbors.append( (r,c) )
        return neighbors

    def aliveNeighbors(self, pos):
        neighbors = self.getBlockNeighbors(pos)
        n = 0
        for neighbor in neighbors:
            if self.cells[neighbor].alive:
                n += 1
        return n

    def simulate(self):
        cells = self.cells.copy()
        for pos in self.cells.keys():
            n = self.aliveNeighbors(pos)
            if self.cells[pos].alive == False:
                if n == 3:
                    cells[pos].alive = True
            else:
                if n < 2 or n > 3:
                    cells[pos].alive = False
                else:
                    cells[pos].alive = True
        self.cells = cells.copy()

    def draw(self, screen):
        cells = self.cells.keys()
        for pos in cells:
            cell = self.cells[pos]
            if cell.alive:
                cell.draw(screen, pos)

# frames per second
FPS = 10

pygame.init()

screen = pygame.display.set_mode(SCREENSIZE)
pygame.display.set_caption("MIT HW")

clock = pygame.time.Clock()

done = False

board = Board(BOARD_WIDTH, BOARD_HEIGHT)
cells = []
for i in range(3000):
    cells.append( (random.randrange(0, BOARD_HEIGHT), random.randrange(0, BOARD_WIDTH)) )
board.seed(cells)

while not done:
    # events
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done = True

    screen.fill(BGCOLOR)

    board.draw(screen)
    board.simulate()

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
