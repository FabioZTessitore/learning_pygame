# 0008_image.py

# display an image

import pygame

SCREENSIZE = (WIDTH, HEIGHT) = (640, 480)

BGCOLOR = (255, 255, 255)

pygame.init()

screen = pygame.display.set_mode(SCREENSIZE)
pygame.display.set_caption("Png Image")

# load an image (64x64 pixels)
sphere = pygame.image.load('./png/red_sphere.png')
# sphere rect
sphereRect = sphere.get_rect()
# sphere position (bottom right)
spherePos = (WIDTH-sphereRect.width, HEIGHT-sphereRect.height)

done = False

# game loop
while not done:
    # events
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done = True

    screen.fill(BGCOLOR)

    # blit the image
    screen.blit(sphere, spherePos)

    pygame.display.flip()

pygame.quit()
