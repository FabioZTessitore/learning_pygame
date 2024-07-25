# 0001_screen.py

# open a window and
# handle QUIT event

import pygame

pygame.init()

SCREENSIZE = (640, 480)
BGCOLOR = (255, 255, 255)

# the window surface
windowSurface = pygame.display.set_mode(SCREENSIZE)

# set the window caption
pygame.display.set_caption("A Simple Window")

# fill the window surface with the background color, just once
windowSurface.fill(BGCOLOR)

# draw the window surface onto the screen
pygame.display.update()

done = False

# game loop
while not done:
    events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

pygame.quit()
