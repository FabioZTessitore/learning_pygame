# 0010_image.py

# display an image

import pygame

SCREENSIZE = (WIDTH, HEIGHT) = (640, 480)

BGCOLOR = (255, 255, 255)

# frames per second
FPS = 30

pygame.init()

windowSurface = pygame.display.set_mode(SCREENSIZE)

pygame.display.set_caption("Png Image")

# load an image (64x64 pixels)
sphere = pygame.image.load('./png/red_sphere.png')
# sphere rect
sphereRect = sphere.get_rect()
# sphere position (bottom right of the screen)
spherePos = (WIDTH-sphereRect.width, HEIGHT-sphereRect.height)

# init the clock
clock = pygame.time.Clock()

done = False

# game loop
while not done:
    # events
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done = True

    windowSurface.fill(BGCOLOR)

    # blit the image
    windowSurface.blit(sphere, spherePos)

    pygame.display.update()

    # pause to mantain FPS
    clock.tick(FPS)

pygame.quit()
