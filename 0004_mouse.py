# 0004_mouse.py

# mouse events

import pygame

SCREENSIZE = (640, 480)

BGCOLOR = (255, 255, 255)

pygame.init()

screen = pygame.display.set_mode(SCREENSIZE)
pygame.display.set_caption("Mouse Events")

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
            print "MOUSEBUTTONDOWN", event.pos

        # mouse motion handler
        if event.type == pygame.MOUSEMOTION:
            print "MOUSEMOTION", event.pos

    # clear the screen
    screen.fill(BGCOLOR)

    pygame.display.flip()

pygame.quit()
