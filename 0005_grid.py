# 0005_grid.py

# draw a (dynamic) grid, mouse wheel

import pygame

SCREENSIZE = (640, 480)

BGCOLOR = (255, 255, 255)
BLACK = (0, 0, 0)

# starting number of rows and columns.
# they change on scrolling the mouse wheel
nRow = 3
nCol = 3

# where are horizontal lines?
# ex. nRow = 3
# --------------     -- 0 (not drawn)
# 1                  -- 1/3 ht
# --------------     -- 1px
# 2                  -- 1/3 ht
# --------------     -- 1px
# 3                  -- 1/3 ht
# --------------     -- SCREENSIZE[1]-1 (not drawn)
#
# (Note: width and height are smaller
# then SCREENSIZE[0] and SCREENSIZE[1]
# cause of grid lines)
#
# Row height is 1/3 of available height (SCREENSIZE[1] - 1px * (nRow-1))
#
# Note: first and last will not be drawn.
# first will be deleted
# last will not be considered by for loop
width = SCREENSIZE[0] - (nCol - 1)
height = SCREENSIZE[1] - (nRow - 1)
#
# set row positions
posRow = []
for i in range(nRow):
    posRow.append( i*(height/nRow) + i - 1 )
del posRow[0]   # do not draw first line
#print posRow
# set col positions
posCol = []
for i in range(nCol):
    posCol.append( i*(width/nCol) + i - 1 )
del posCol[0]   # do not draw first line
#print posCol

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
    # set row positions
    posRow = []
    for i in range(nRow):
        posRow.append( i*(height/nRow) + i - 1 )
    del posRow[0]   # do not draw first line
    #print posRow
    # set col positions
    posCol = []
    for i in range(nCol):
        posCol.append( i*(width/nCol) + i - 1 )
    del posCol[0]   # do not draw first line
    #print posCol

    # clear the screen
    screen.fill(BGCOLOR)

    # draw horizontal lines
    for r in posRow:
        pygame.draw.line(screen, BLACK, (0, r), (SCREENSIZE[0]-1, r))
    # draw vertical lines
    for c in posCol:
        pygame.draw.line(screen, BLACK, (c, 0), (c, SCREENSIZE[1]-1))

    pygame.display.flip()

pygame.quit()
