# 0004_mouse.py

# mouse events

import pygame

SCREENSIZE = (640, 480)

BGCOLOR = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()

screen = pygame.display.set_mode(SCREENSIZE)
pygame.display.set_caption("Mouse Events")

# on first click store mouse coords
# on second click store the line
second_click = False

# no lines at startup
lines = []

done = False

# game loop
while not done:
    # events
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done = True

        # mouse events
        if event.type == pygame.MOUSEBUTTONDOWN:
            if second_click:
                # store line
                lines.append( (position, event.pos) )
                #
                second_click = False
            else:
                # first click,
                # store mouse coords
                position = event.pos
                # flag to second click
                second_click = True

    # clear the screen
    screen.fill(BGCOLOR)

    # draw the lines
    for line in lines:
        pygame.draw.line(screen, BLACK, line[0], line[1])

    pygame.display.flip()

pygame.quit()
