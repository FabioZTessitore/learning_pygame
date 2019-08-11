import pygame
from colors import BLACK

class Block:
    def __init__(self, size=0):
        self.size = size

    def canMove(self, pos, delta, boardWidth, boardHeight):
        x, y = pos
        dx, dy = delta
        return (0 <= x+dx < boardWidth) and (0 <= y+dy < boardHeight)


    def draw(self, screen, pos, color):
        x, y = pos
        pygame.draw.rect(screen, BLACK, (x * self.size, y * self.size, self.size, self.size), 2)
        pygame.draw.rect(screen, color, (x * self.size + 2, y * self.size + 2, self.size - 3 , self.size - 3))


if __name__ == '__main__':
    from colors import RED, WHITE

    SCREENSIZE = (300, 300)

    block = Block(30)

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

        block.draw(screen, (3, 3), RED)

        pygame.display.flip()

        clock.tick(10)

    pygame.quit()
