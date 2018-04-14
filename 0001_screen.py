# 0001_screen.py

# open a window and
# handle QUIT event

import pygame

pygame.init()

SCREENSIZE = (640, 480)
BGCOLOR = (255, 255, 255)

# the window
screen = pygame.display.set_mode(SCREENSIZE)
pygame.display.set_caption("A Simple Window")

done = False

# game loop
while not done:
    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # redraw
    screen.fill(BGCOLOR)

    # screen flip
    pygame.display.flip()

pygame.quit()
