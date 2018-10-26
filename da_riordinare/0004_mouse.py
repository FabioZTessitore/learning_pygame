# 0004_mouse.py

# mouse events

import pygame

SCREENSIZE = (640, 480)

BGCOLOR = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

pygame.init()

screen = pygame.display.set_mode(SCREENSIZE)
pygame.display.set_caption("Mouse Events")

# on first click store mouse coords
# on second click store the line
waitingForSecondClick = False

# no lines at startup
lines = []

# current line, on mouse motion
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
                # clear
                waitingForSecondClick = False
            else:
                # first click,
                # store mouse coords
                position = event.pos
                # set first point of current line
                currentLine.append(position)
                # on click, current line is a point
                currentLine.append(position)
                # flag, waiting for second click
                waitingForSecondClick = True

        # mouse motion handler
        if event.type == pygame.MOUSEMOTION:
            # if waiting for second click, update line end
            if waitingForSecondClick:
                currentLine[1] = event.pos


    # clear the screen
    screen.fill(BGCOLOR)

    # draw the lines
    for line in lines:
        pygame.draw.line(screen, BLACK, line[0], line[1])

    # draw current line
    if waitingForSecondClick:
        pygame.draw.line(screen, GREEN, currentLine[0], currentLine[1])

    pygame.display.flip()

pygame.quit()
