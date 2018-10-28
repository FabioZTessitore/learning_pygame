# 0003_falling.py

# Simulation of a falling body
#
# Frame
# -1 < x < 1
# 0 < y < 10m
#
# Screen Size
# Width 640
# Height 480
#
# The ball start at rest at y = h meters
#
# Screen coordinates:
# xs = 1/2 (x + 1) 640 = 320 * (x + 1)
# ys = 480 (1 - y/10)

# frames per second
FPS = 30

# ball real position
h = 7
x, y = 0, h
# ball velocity
v0 = 0
v = v0
# acceleration
g = -9.81
# time step
dt = 1./FPS

import pygame

SCREENSIZE = (WIDTH, HEIGHT) = (640, 480)

BGCOLOR = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()

screen = pygame.display.set_mode(SCREENSIZE)
pygame.display.set_caption("A Falling Body")

# load the image to animate
sphere = pygame.image.load('../png/red_sphere.png')
sphereRect = sphere.get_rect()

# set sphere position
xs = 320 * (x+1)
ys = 480 * (1 - y/10.)

# also display sphere position and speed
#
# font
font = pygame.font.Font("freesansbold.ttf", 16)
# text
textPositionSurf = font.render("Ball Position: (%d, %d)" % (xs, ys), True, BLACK, BGCOLOR)
textSpeedSurf = font.render("Ball Speed: %6.2f" % (v,), True, BLACK, BGCOLOR)
# position
textPositionRect = textPositionSurf.get_rect()
textPositionRect.x = 20
textPositionRect.y = 20
textSpeedRect = textSpeedSurf.get_rect()
textSpeedRect.x = 20
textSpeedRect.y = 40

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
    v += g * dt
    y += v * dt

    #xs = 320 * (x+1)
    ys = 480 * (1 - y/10.)

    if y < 0:
        y = h
        v = v0

    # set text
    textPositionSurf = font.render("Ball Position: (%d, %d)" % (xs, ys), True, BLACK, BGCOLOR)
    textSpeedSurf = font.render("Ball Speed: %6.2f" % (v,), True, BLACK, BGCOLOR)

    screen.fill(BGCOLOR)

    # blit the image
    screen.blit(sphere, (xs-sphereRect.width/2, ys-sphereRect.height/2))

    # blit the text
    screen.blit(textPositionSurf, textPositionRect)
    screen.blit(textSpeedSurf, textSpeedRect)

    pygame.display.flip()

    # pause to mantain FPS
    clock.tick(FPS)

pygame.quit()
