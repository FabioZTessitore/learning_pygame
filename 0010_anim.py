# 0010_anim.py

# animation

import pygame

SCREENSIZE = (WIDTH, HEIGHT) = (640, 480)

BGCOLOR = (255, 255, 255)
BLACK = (0, 0, 0)

# frames per second
FPS = 30

pygame.init()

screen = pygame.display.set_mode(SCREENSIZE)
pygame.display.set_caption("Animation")

# load the image to animate
sphere = pygame.image.load('./png/red_sphere.png')
# calculate spehere dimensions
sphereRect = sphere.get_rect()
(sphereWidth, sphereHeight) = (sphereRect.width, sphereRect.height)
# set sphere position (at the bottom)
(sphereX, sphereY) = (60, HEIGHT-sphereHeight)

# sphere delta position
sphereDx = 2
sphereDy = 2

# also write sphere position
#
# font
font = pygame.font.Font("freesansbold.ttf", 32)
# text
textSurf = font.render("Ball Position: (%d, %d)" % (sphereX, sphereY),
        True, BLACK, BGCOLOR)
# position
textRect = textSurf.get_rect()
textRect.x = 30
textRect.y = 30

# init the clock
clock = pygame.time.Clock()

done = False

# game loop
while not done:
    # events
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done = True

    # update sphere position
    (sphereX, sphereY) = (sphereX + sphereDx, sphereY + sphereDy)
    if sphereX < 0 or sphereX + sphereWidth > WIDTH:
        sphereDx = -sphereDx
    if sphereY < 0 or sphereY + sphereHeight > HEIGHT:
        sphereDy = -sphereDy

    # set text
    textSurf = font.render("Ball Position: (%d, %d)" % (sphereX, sphereY),
            True, BLACK, BGCOLOR)

    screen.fill(BGCOLOR)

    # blit the image
    screen.blit(sphere, (sphereX, sphereY))

    # blit the text
    screen.blit(textSurf, textRect)

    pygame.display.flip()

    # pause to mantain FPS
    clock.tick(FPS)

pygame.quit()
