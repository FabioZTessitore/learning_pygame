# 0004_ship.py

# Simulation of a ship
#
# T - C v = m a
#
# T     thrust
# C     drag coeff
# v     speed
# m     mass
# a     accel
#
# Frame
# 0 < x < 200m
# -1 < y < 1
#
# Screen Size
# Width 640
# Height 480
#
# The ship start at rest at (x, y) = (10m, 0)
#
# Screen coordinates:
# xs = 640 * x/200
# ys = 1/2 (y + 1) 480 = 240 * (y + 1)

# frames per second
FPS = 30

# ship real position
x = 10
y = 0
distanza = 0.
# ship velocity
v0 = 0.
v = v0
# ship thrust
T = 0.       # N
# ship mass
M = 500.    #Kg
# drag coeff
C = 15
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

ship2 = pygame.image.load('../png/sailing.png')
shipRect2 = ship2.get_rect()

# set ship position
xs = int(640. * x/200.)
ys = int(240 * (y + 1)) - 100

xs2 = 640 * (x % 20)/20
ys2 = int(240 * (y + 1)) + 100

# also display ship position and speed
#
# font
font = pygame.font.Font("freesansbold.ttf", 16)
# text
textPositionSurf = font.render("Ship Position: (%d, %d)" % (xs, ys), True, BLACK, BGCOLOR)
textSpeedSurf = font.render("Ship Speed: %6.2f m/s (%.1f Km/h)" % (v, v*3.6), True, BLACK, BGCOLOR)
textThrustSurf = font.render("Ship Thrust: %6.2f" % (T,), True, BLACK, BGCOLOR)
textDistanzaSurf = font.render("Distanza: %.1f" % (distanza,), True, BLACK, BGCOLOR)
# position
textPositionRect = textPositionSurf.get_rect()
textPositionRect.x = 20
textPositionRect.y = 20
textSpeedRect = textSpeedSurf.get_rect()
textSpeedRect.x = 20
textSpeedRect.y = 40
textThrustRect = textThrustSurf.get_rect()
textThrustRect.x = 20
textThrustRect.y = 60
textDistanzaRect = textDistanzaSurf.get_rect()
textDistanzaRect.x = 20
textDistanzaRect.y = 80

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
    if keys[pygame.K_RIGHT]:
        T += 15
        if T > 105:
            T = 105
    elif keys[pygame.K_LEFT]:
        T -= 15
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
    distanza += v * dt

    xs = int(640. * x/200.)
    ys = int(240 * (y + 1)) - 100

    xs2 = 640 * (x % 20)/20
    ys2 = int(240 * (y + 1)) + 100

    if x > 200:
        x = 10

    # set text
    textPositionSurf = font.render("Ship Position: (%d, %d)" % (xs, ys), True, BLACK, BGCOLOR)
    textSpeedSurf = font.render("Ship Speed: %6.2f m/s (%.1f Km/h)" % (v, v*3.6), True, BLACK, BGCOLOR)
    textThrustSurf = font.render("Ship Thrust: %6.2f" % (T,), True, BLACK, BGCOLOR)
    textDistanzaSurf = font.render("Distanza: %.1f" % (distanza,), True, BLACK, BGCOLOR)

    screen.fill(BGCOLOR)

    # blit the image
    screen.blit(ship, (xs-shipRect.width/2, ys-shipRect.height/2))
    screen.blit(ship2, (xs2-shipRect2.width/2, ys2-shipRect2.height/2))

    # blit the text
    screen.blit(textPositionSurf, textPositionRect)
    screen.blit(textSpeedSurf, textSpeedRect)
    screen.blit(textThrustSurf, textThrustRect)
    screen.blit(textDistanzaSurf, textDistanzaRect)

    pygame.display.flip()

    # pause to mantain FPS
    clock.tick(FPS)

pygame.quit()
