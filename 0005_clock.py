# 0005_clock.py

# clock

import pygame

pygame.init()
clock = pygame.time.Clock()

SCREENSIZE = (640, 480)

redAmount = 0
BGCOLOR = (redAmount, 0, 0)

windowSurface = pygame.display.set_mode(SCREENSIZE)

pygame.display.set_caption("Animated BG Color")

done = False

# game loop
while not done:
    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # change the red amount
    redAmount += 1
    if redAmount > 255:
        redAmount = 0

    # recalculate bg color with current red amount
    BGCOLOR = (redAmount, 0, 0)

    # refill the window surface with the new background color
    windowSurface.fill(BGCOLOR)

    # draw the window surface onto the screen
    pygame.display.update()

    # pause to mantain 30 FPS
    clock.tick(30)

pygame.quit()
