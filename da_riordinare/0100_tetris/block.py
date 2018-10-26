import pygame
from colors import BLACK

class Block:
    BLOCK_SIZE = 30

    def __init__(self):
        pass

    def canMove(self, pos, delta, boardWidth, boardHeight):
        x, y = pos
        dx, dy = delta

        if (0 <= x+dx < boardWidth) and (0 <= y+dy < boardHeight):
            return True

        return False


    def draw(self, screen, pos, color):
        x, y = pos
        pygame.draw.rect(screen, BLACK, (x * Block.BLOCK_SIZE, y * Block.BLOCK_SIZE, Block.BLOCK_SIZE, Block.BLOCK_SIZE), 2)
        pygame.draw.rect(screen, color, (x * Block.BLOCK_SIZE + 2, y * Block.BLOCK_SIZE + 2, Block.BLOCK_SIZE - 3 , Block.BLOCK_SIZE - 3))
