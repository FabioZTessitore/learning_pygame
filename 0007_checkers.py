# 0007_checkers.py

# put an item into the grid

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

# cell dimensions
dimRow = height / nRow
dimCol = width / nCol

# the ball
indexBall = (2, 2)
dimBall = ( int(dimCol * .75), int(dimRow * .75) )
posBall = ( int(dimCol * (indexBall[0]+.5) - dimBall[0] * .5),
            int(dimRow * (indexBall[1]+.5) - dimBall[1] * .5) )

pygame.init()
screen = pygame.display.set_mode(SCREENSIZE)
pygame.display.set_caption("Item onto a checkers")

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
                if nRow < 3:
                    nRow = 3
                nCol -= 1
                if nCol < 3:
                    nCol = 3

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

    # update cell dimensions
    dimRow = height / nRow
    dimCol = width / nCol
    print "dimRow", dimRow
    print "dimCol", dimCol

    # update ball dimensions and position
    dimBall = ( int(dimCol * .75), int(dimRow * .75) )
    print "dimBall", dimBall
    posBall = ( int(dimCol * (indexBall[0]+.5) - dimBall[0] * .5 + indexBall[0]),
                int(dimRow * (indexBall[1]+.5) - dimBall[1] * .5 + indexBall[1]) )
    print "posBall", posBall

    screen.fill(BGCOLOR)

    # draw horizontal lines
    for r in posRow:
        pygame.draw.line(screen, BLACK, (0, r), (SCREENSIZE[0]-1, r))
    # draw vertical lines
    for c in posCol:
        pygame.draw.line(screen, BLACK, (c, 0), (c, SCREENSIZE[1]-1))

    # draw the ball
    pygame.draw.ellipse(screen, RED, (posBall[0], posBall[1], dimBall[0], dimBall[1]))

    pygame.display.flip()

pygame.quit()
