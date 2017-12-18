import pygame

pygame.init()

screenSize = (640, 480)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

nRow = 15
nCol = 16

posRow = range(0, screenSize[1], screenSize[1]/nRow)
del posRow[0]

posCol = range(0, screenSize[0], screenSize[0]/nCol)
del posCol[0]

screen = pygame.display.set_mode(screenSize)
pygame.display.set_caption("Grid ...")

done = False

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

    pygame.display.flip()

pygame.quit()
