# 0002_draw.py

# draw lines, rects, circles, and ellipses

import pygame

pygame.init()

SCREENSIZE = (640, 480)

BGCOLOR= (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
MAGENTA = (255, 0, 255)

windowSurface = pygame.display.set_mode(SCREENSIZE)
pygame.display.set_caption("Lines, Rects, Circles, Ellipses")

# fill the window surface with the background color,
# then draw some figures, just once
windowSurface.fill(BGCOLOR)

# pygame.draw.lines(windowSurface, Color, (startX, startY), (endX, endY))
pygame.draw.line(windowSurface, RED, (20, 100), (420, 300))
# pygame.draw.rect(windowSurface, Color, (x, y, width, height))
pygame.draw.rect(windowSurface, GREEN, (20, 20, 100, 20))
# pygame.draw.circle(windowSurface, BLUE, (x, y), radius, thickness)
pygame.draw.circle(windowSurface, BLUE, (300, 50), 20, 0)
# pygame.draw.ellipse(windowSurface, RED, (startX, startY, width, height), thickness)
pygame.draw.ellipse(windowSurface, MAGENTA, (300, 250, 40, 80), 1)

# draw the window surface onto the screen
pygame.display.update()

done = False

# game loop
while not done:
    # events
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done = True

pygame.quit()
