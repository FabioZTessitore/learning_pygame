# 0005_grid.py

# draw a (dynamic) grid

import pygame

SCREENSIZE = (640, 480)

BGCOLOR = (255, 255, 255)
BLACK = (0, 0, 0)

# starting row and columns.
# they change on scrolling the mouse wheel
nRow = 3
nCol = 3

# where are horizontal lines?
# es nRow = 3
# --------------
# 1
# --------------
# 2
# --------------
# 3
# --------------
# first is at 0
# last is at height
# (Note: width and height are smaller
# then SCREENSIZE[0] and SCREENSIZE[1]
# cause of grid lines)
# the other two are after 1/3 and 2/3 of height
# Note: first and last will not be drawn.
# first will be deleted
# last will not be considered by for loop
width = SCREENSIZE[0] - (nCol - 1)
height = SCREENSIZE[1] - (nRow - 1)
posRow = range(0, height, height/nRow)
del posRow[0]   # do not draw first line
# vertical lines
posCol = range(0, width, width/nCol)
del posCol[0]   # do not draw first line

pygame.init()

screen = pygame.display.set_mode(SCREENSIZE)
pygame.display.set_caption("Dynamic Grid")

done = False

# game loop
while not done:
    # events
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done = True

        # mouse wheel
        if event.type == pygame.MOUSEBUTTONDOWN:
            # button 4: wheel up
            if event.button == 4:
                nRow += 1
                if nRow > 40:
                    nRow = 40
                nCol += 1
                if nCol > 40:
                    nCol = 40
            # button 5: wheel down
            elif event.button == 5:
                nRow -= 1
                if nRow < 2:
                    nRow = 2
                nCol -= 1
                if nCol < 2:
                    nCol = 2

    # recreate the grid
    width = SCREENSIZE[0] - (nCol - 1)
    height = SCREENSIZE[1] - (nRow - 1)
    posRow = range(0, height, height/nRow)
    del posRow[0]   # do not draw first line
    posCol = range(0, width, width/nCol)
    del posCol[0]   # do not draw first line

    # clear the screen
    screen.fill(BGCOLOR)

    # draw horizontal lines
    for counter, i in enumerate(posRow):
        pygame.draw.line(screen, BLACK, (0, counter+i), (SCREENSIZE[0], counter+i))

    # draw vertical lines
    for counter, i in enumerate(posCol):
        pygame.draw.line(screen, BLACK, (counter+i, 0), (counter+i, SCREENSIZE[1]))

    pygame.display.flip()

pygame.quit()
