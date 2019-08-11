import pygame
from colors import WHITE
from block import Block
from board import Board

BGCOLOR = WHITE

BLOCK_SIZE = 30
BOARD_WIDTH = 10
BOARD_HEIGHT = 20

SCREENSIZE = (WIDTH, HEIGHT) = (BLOCK_SIZE*BOARD_WIDTH, BLOCK_SIZE*BOARD_HEIGHT)

FPS = 30
dt = FPS * 2
counter = 0

pygame.init()

screen = pygame.display.set_mode(SCREENSIZE)
pygame.display.set_caption("Tetris")

clock = pygame.time.Clock()

done = False

board = Board(BOARD_WIDTH, BOARD_HEIGHT, BLOCK_SIZE)

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

    if counter % dt == 0:
        counter = 0
        dx, dy = delta
        if dy == 0:
            dy = 1
        delta = (dx, dy)

    if board.canMoveCurrentShape(delta):
        board.moveCurrentShape(delta)

    screen.fill(BGCOLOR)

    board.draw(screen)

    pygame.display.flip()

    clock.tick(FPS)
    counter += 1

pygame.quit()
