import pygame

pygame.init()

screenSize = (640, 480)

FPS = 5

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

nRow = 5
nCol = 5

posRow = range(0, screenSize[1], screenSize[1]/nRow)
del posRow[0]

posCol = range(0, screenSize[0], screenSize[0]/nCol)
del posCol[0]

dimRow = posRow[1] - posRow[0]
dimCol = posCol[1] - posCol[0]

indexBall = (2, 2)
sign = 1
dimBall = (dimCol * .75, dimRow * .75)
posBall = ( dimCol * (indexBall[0]+.5) - dimBall[0] * .5, dimRow * (indexBall[1]+.5) - dimBall[1] * .5 )

screen = pygame.display.set_mode(screenSize)
pygame.display.set_caption("Grid ...")

done = False

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done = True

    screen.fill(WHITE)

    # draw horizontal lines
    for i in posRow:
        pygame.draw.line(screen, BLACK, (0, i), (screenSize[0], i))

    # draw vertical lines
    for i in posCol:
        pygame.draw.line(screen, BLACK, (i, 0), (i, screenSize[1]))

    indexBall = (indexBall[0] + sign*1, indexBall[1])
    posBall = ( dimCol * (indexBall[0]+.5) - dimBall[0] * .5, dimRow * (indexBall[1]+.5) - dimBall[1] * .5 )
    sign = -sign

    # draw ball
    pygame.draw.ellipse(screen, RED, (posBall[0], posBall[1], dimBall[0], dimBall[1]))

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
