# 0006_pixel.py

# edit pixels

import pygame

SCREENSIZE = (640, 480)

BGCOLOR = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# starting row and columns.
# they change on scrolling the mouse wheel
nRow = 3
nCol = 3

# for an explanation of the grid algorithm
# see 0005_grid.py
width = SCREENSIZE[0] - (nCol - 1)
height = SCREENSIZE[1] - (nRow - 1)
posRow = []
for i in range(nRow):
    posRow.append( i*(height/nRow) + i - 1 )
del posRow[0]   # do not draw first line
# set col positions
posCol = []
for i in range(nCol):
    posCol.append( i*(width/nCol) + i - 1 )
del posCol[0]   # do not draw first line

pygame.init()

screen = pygame.display.set_mode(SCREENSIZE)
pygame.display.set_caption("Pixel Array")

# pixel matrix
pixels = pygame.PixelArray(screen)

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
    posRow = []
    for i in range(nRow):
        posRow.append( i*(height/nRow) + i - 1 )
    del posRow[0]   # do not draw first line
    # set col positions
    posCol = []
    for i in range(nCol):
        posCol.append( i*(width/nCol) + i - 1 )
    del posCol[0]   # do not draw first line

    # clear the screen
    screen.fill(BGCOLOR)

    # draw horizontal lines
    for r in posRow:
        pygame.draw.line(screen, BLACK, (0, r), (SCREENSIZE[0]-1, r))
    # draw vertical lines
    for c in posCol:
        pygame.draw.line(screen, BLACK, (c, 0), (c, SCREENSIZE[1]-1))

    # mark extra pixel with red
    for y in range(int(height/nRow) * nRow + nRow, SCREENSIZE[1]):
        for x in range(0, SCREENSIZE[0]):
            pixels[x][y] = RED
    for x in range(int(width/nCol) * nCol+ nCol, SCREENSIZE[0]):
        for y in range(0, SCREENSIZE[1]):
            pixels[x][y] = RED

    pygame.display.flip()

del pixels
pygame.quit()
