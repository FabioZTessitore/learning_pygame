# 0002_bgcolor.py

# handle key press, change bgcolor

import pygame

pygame.init()

SCREENSIZE = (640, 480)
redAmount = 0
BGCOLOR = (redAmount, 0, 0)

# the window
screen = pygame.display.set_mode(SCREENSIZE)
pygame.display.set_caption("Change BG Color")

done = False

# game loop
while not done:
    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # change red amount
    # with Arrow Key Up/Down
    #
    # get_pressed() return a map
    # of pressed keys
    keys = pygame.key.get_pressed()
    # more red
    if keys[pygame.K_UP]:
        redAmount += 1
        if redAmount > 255:
            redAmount = 255
    # less red
    if keys[pygame.K_DOWN]:
        redAmount -= 1
        if redAmount < 0:
            redAmount = 0


    # logic
    # recalculate bg color
    # with current red amount
    BGCOLOR = (redAmount, 0, 0)
    #print 'BGCOLOR', BGCOLOR

    # redraw
    screen.fill(BGCOLOR)

    # screen flip
    pygame.display.flip()

pygame.quit()
