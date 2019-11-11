# 0003_pixel.py

# edit pixels

import random
import pygame

SCREENSIZE = (SCREEN_WIDTH, SCREEN_HEIGHT) = (640, 480)

BGCOLOR = (255, 255, 255)
RED = (255, 0, 0)

pygame.init()

windowSurface = pygame.display.set_mode(SCREENSIZE)

pygame.display.set_caption("Pixel Array")

# fill the window surface with the background color, just once
windowSurface.fill(BGCOLOR)

# pixel matrix
pixels = pygame.PixelArray(windowSurface)
#
for row in range(SCREEN_WIDTH):
    for col in range(SCREEN_HEIGHT):
        color = random.choice([RED, BGCOLOR])
        pixels[row][col] = color
#
pixels.close()

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
