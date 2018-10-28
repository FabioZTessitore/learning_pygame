# 0004_mouse.py

# draw lines with the mouse

import pygame

SCREENSIZE = (640, 480)

BGCOLOR = (255, 255, 255)
BLACK = (0, 0, 0)           # lines
GREEN = (0, 255, 0)         # temp line

pygame.init()

screen = pygame.display.set_mode(SCREENSIZE)
pygame.display.set_caption("Mouse Events")

# on first click store mouse coords
# on second click store the line
waitingForSecondClick = False
# no lines at startup
lines = []
# temp line, on mouse motion
currentLine = []

done = False

# game loop
while not done:
    # events
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done = True

        # mouse events
        # click handler
        if event.type == pygame.MOUSEBUTTONDOWN:
            if waitingForSecondClick:
                # second click happened, store the line
                lines.append( (position, event.pos) )
                # clear current line
                currentLine = []
                # clear the flag
                waitingForSecondClick = False
            else:
                # first click,
                # store mouse coords
                position = event.pos
                # set first point of current line
                currentLine.append(position)
                # on click, current line is a point
                # so add a duplicate point
                # to have a line
                currentLine.append(position)
                # set flag, waiting for second click
                waitingForSecondClick = True

        # mouse motion handler
        if event.type == pygame.MOUSEMOTION:
            # if waiting for second click, update temp line
            if waitingForSecondClick:
                currentLine[1] = event.pos

    # clear the screen
    screen.fill(BGCOLOR)

    # draw the lines
    for line in lines:
        start, end = line
        pygame.draw.line(screen, BLACK, start, end)

    # draw current line
    if waitingForSecondClick:
        start, end = currentLine
        pygame.draw.line(screen, GREEN, start, end)

    pygame.display.flip()

pygame.quit()
