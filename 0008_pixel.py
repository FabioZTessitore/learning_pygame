# 0008_pixel.py

# edit pixels

import random
import pygame

SCREENSIZE = (SCREEN_WIDTH, SCREEN_HEIGHT) = (640, 480)

BGCOLOR = (255, 255, 255)
RED = (255, 0, 0)

# frames per second
FPS = 1

pygame.init()

screen = pygame.display.set_mode(SCREENSIZE)
pygame.display.set_caption("Pixel Array")

# pixel matrix
pixels = pygame.PixelArray(screen)

done = False

# init the clock
clock = pygame.time.Clock()

# game loop
while not done:
    # events
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done = True

    # clear the screen
    screen.fill(BGCOLOR)

    for x in range(SCREEN_WIDTH):
        for y in range(SCREEN_HEIGHT):
            color = random.choice([RED, BGCOLOR])
            pixels[x][y] = color

    pygame.display.flip()

    # pause to mantain FPS
    clock.tick(FPS)

pixels.close()
pygame.quit()
