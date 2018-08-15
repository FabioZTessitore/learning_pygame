# 0015_memory.py

# memory game

import pygame
import sys

SCREENSIZE = (SCREEN_WIDTH, SCREEN_HEIGHT) = (640, 480)
BGCOLOR = (255, 255, 255)
GREEN = (0, 255, 0)

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
# print XMARGIN, YMARGIN
# XMARGIN = 70
# YMARGIN = 65

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

    screen.fill(BGCOLOR)

    # draw the area of the board
    pygame.draw.rect(screen, GREEN, (XMARGIN, YMARGIN, BOARD_WIDTH*(GAPSIZE+BOXSIZE), BOARD_HEIGHT*(GAPSIZE+BOXSIZE)))

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
