# 0004_ship.py

# Simulation of a ship
#
# T - C v = m a
#
# T     trust
# C     drag coeff
# v     speed
# m     mass
# a     accel
#
# Frame
# 0 < x < 100m
# -1 < y < 1
#
# Screen Size
# Width 640
# Height 480
#
# The ship start at rest at (x, y) = (10m, 0)
#
# Screen coordinates:
# xs = 640 * x/100
# ys = 1/2 (y + 1) 480 = 240 * (y + 1)

# frames per second
FPS = 30

# ship real position
x = 10
y = 0
# ship velocity
v0 = 0.
v = v0
# ship trust
T = 0.       # N
# ship mass
M = 500.    #Kg
# drag coeff
C = 100.
# time step
dt = 1./FPS

import pygame

SCREENSIZE = (WIDTH, HEIGHT) = (640, 480)

BGCOLOR = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()

screen = pygame.display.set_mode(SCREENSIZE)
pygame.display.set_caption("A Ship")

# load the image to animate
ship = pygame.image.load('../png/sailing.png')
shipRect = ship.get_rect()

# set ship position
xs = int(640. * x/100.)
ys = int(240 * (y + 1))

# also display ship position and speed
#
# font
font = pygame.font.Font("freesansbold.ttf", 16)
# text
textPositionSurf = font.render("Ship Position: (%d, %d)" % (xs, ys), True, BLACK, BGCOLOR)
textSpeedSurf = font.render("Ship Speed: %6.2f" % (v,), True, BLACK, BGCOLOR)
textTrustSurf = font.render("Ship Trust: %6.2f" % (T,), True, BLACK, BGCOLOR)
# position
textPositionRect = textPositionSurf.get_rect()
textPositionRect.x = 20
textPositionRect.y = 20
textSpeedRect = textSpeedSurf.get_rect()
textSpeedRect.x = 20
textSpeedRect.y = 40
textTrustRect = textTrustSurf.get_rect()
textTrustRect.x = 20
textTrustRect.y = 60

# init the clock
clock = pygame.time.Clock()

done = False

k = 0

# game loop
while not done:
    # events
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        T += 10
        if T > 1500:
            T = 1500
    elif keys[pygame.K_RIGHT]:
        T -= 10
        if T < 0:
            T = 0.

    # calculate acceleration
    a = (T - C * v) / M

    if k % 100 == 0:
        print "a: ", a
    k += 1

    # calculate velocity
    v = v + a * dt

    # update ship position
    x += v * dt

    xs = int(640. * x/100.)
    ys = int(240 * (y + 1))

    if x > 95:
        x = 0

    # set text
    textPositionSurf = font.render("Ship Position: (%d, %d)" % (xs, ys), True, BLACK, BGCOLOR)
    textSpeedSurf = font.render("Ship Speed: %6.2f" % (v,), True, BLACK, BGCOLOR)
    textTrustSurf = font.render("Ship Trust: %6.2f" % (T,), True, BLACK, BGCOLOR)

    screen.fill(BGCOLOR)

    # blit the image
    screen.blit(ship, (xs-shipRect.width/2, ys-shipRect.height/2))

    # blit the text
    screen.blit(textPositionSurf, textPositionRect)
    screen.blit(textSpeedSurf, textSpeedRect)
    screen.blit(textTrustSurf, textTrustRect)

    pygame.display.flip()

    # pause to mantain FPS
    clock.tick(FPS)

pygame.quit()
