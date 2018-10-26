# 0017_memory.py

# memory game

# create data structure and show symbols, maybe

import pygame
import sys

SCREENSIZE = (SCREEN_WIDTH, SCREEN_HEIGHT) = (640, 480)

BOXSIZE = 40
GAPSIZE = 10
BOARD_WIDTH = 10
BOARD_HEIGHT = 7

# +----------------------------------------------------------------------+
# |            ^            SCREEN_WIDTH                                 |
# |            |                                                         |
# |         YMARGIN              BOARD_WIDTH = 10 Box                    |
# |            |                                                         |
# |            -                                                         |
# |               BOXSIZE                                                |
# |                 +---+    +---+                                       |
# | <- XMARGIN ->   |   |    |   |     .....                             |
# |                 +---+    +---+                                       |
# |         GAPSIZE/2    GAPSIZE/2                                       |
# |                            .                                         |
# |  SCREEN_HEIGHT             .                                         |
# |                            .   BOARD_HEIGHT = 7 Box                  |
# |                                                                      |
# |                                                                      |
# |                                                                      |
# |                                                                      |
# |                                                                      |
# +----------------------------------------------------------------------+

if BOARD_WIDTH * BOARD_HEIGHT % 2 != 0:
    print "I Box devono essere pari"
    sys.exit()

XMARGIN = (SCREEN_WIDTH - BOARD_WIDTH * (BOXSIZE + GAPSIZE)) / 2
YMARGIN = (SCREEN_HEIGHT - BOARD_HEIGHT * (BOXSIZE + GAPSIZE)) / 2

GREY = (100, 100, 100)
NAVYBLUE = (60, 60, 100)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
PURPLE = (255, 0, 255)
CYAN = (0, 255, 255)

BGCOLOR = NAVYBLUE
BOXCOLOR = WHITE

DONUT = 'donut'
SQUARE = 'square'
DIAMOND = 'diamond'
LINES = 'lines'
OVAL = 'oval'

ALLCOLORS = (RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, CYAN)
ALLSHAPES = (DONUT, SQUARE, DIAMOND, LINES, OVAL)

# board is a list of list
# [
#   [ (shape, color), ... ],     # first column
#   [ (shape, color), ... ],     # second column
#   ...
# ]
board = []
icons = []
for color in ALLCOLORS:
    for shape in ALLSHAPES:
        icons.append( (shape, color) )
icons += icons[:]
print len(icons)
print BOARD_WIDTH*BOARD_HEIGHT
for i in range(BOARD_WIDTH):
    col = []
    for j in range(BOARD_HEIGHT):
        col.append(icons.pop())
    board.append(col)
print board

FPS = 30

pygame.init()

screen = pygame.display.set_mode(SCREENSIZE)
pygame.display.set_caption("Memory Game")

clock = pygame.time.Clock()

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.MOUSEMOTION:
            #print event.pos
            pass

        if event.type == pygame.MOUSEBUTTONDOWN:
            #print "click at ", event.pos
            (x, y) = event.pos
            x -= XMARGIN
            y -= YMARGIN
            x /= float(BOXSIZE+GAPSIZE)
            y /= float(BOXSIZE+GAPSIZE)
            x_int = int(x)
            y_int = int(y)
            x -= x_int
            y -= y_int
            if 0.5*GAPSIZE/(GAPSIZE+BOXSIZE) < x < (0.5*GAPSIZE+BOXSIZE)/(GAPSIZE+BOXSIZE) and \
                0.5*GAPSIZE/(GAPSIZE+BOXSIZE) < y < (0.5*GAPSIZE+BOXSIZE)/(GAPSIZE+BOXSIZE):
                print x_int, y_int
                #print x, y

    screen.fill(BGCOLOR)

    # draw the area of the board
    #pygame.draw.rect(screen, GREEN, (XMARGIN, YMARGIN, BOARD_WIDTH*(GAPSIZE+BOXSIZE), BOARD_HEIGHT*(GAPSIZE+BOXSIZE)))

    # draw boxes
    for y in range(BOARD_HEIGHT):
        for x in range(BOARD_WIDTH):
            pygame.draw.rect(screen, BOXCOLOR,
                (
                XMARGIN+GAPSIZE/2+(GAPSIZE + BOXSIZE)*x,
                YMARGIN+GAPSIZE/2+(GAPSIZE + BOXSIZE)*y, BOXSIZE, BOXSIZE
                )
            )

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
