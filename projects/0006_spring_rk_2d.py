# 0006_spring_rk_2d.py

# Two Springs - Circle (Runge Kutta integration)
#
#
# Runge-Kutta integration
# for details see 0005_spring_rk.py
#
# In our case:
# x'' = -x              x(0) = 0.75     x'(0) = 0
# y'' = -y              y(0) = 0.0      y'(0) = 0.75
#
# x' = vx               x(0) = 0.75
# vx' = -x              vx(0) = 0.
#
# y' = vy               y(0) = 0.0
# vy' = -y              vy(0) = 0.75
#
# Frame
# -1 < x < 1
# -1 < y < 1
#
# Screen Size
# Width 640
# Height 480
#
# The ball start at (x, y) = (0.75, 0.) with velocity (vx, vy) = (0., 0.75)
#
# Screen coordinates:
# xs = 1/2 (1 + x) 640 = 320 * (x + 1)
# ys = 1/2 (1 + y) 480 = 240 * (y + 1)

# frames per second
FPS = 30

# ball real position
x, y = 0.75, 0.
# ball velocity
vx = 0.
vy = 0.75
# time step
dt = 1./FPS

import pygame
import math

SCREENSIZE = (WIDTH, HEIGHT) = (640, 480)

BGCOLOR = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()

screen = pygame.display.set_mode(SCREENSIZE)
pygame.display.set_caption("Two Springs - Circle")

# load the image to animate
sphere = pygame.image.load('../png/red_sphere.png')
sphereRect = sphere.get_rect()

# set sphere position
xs = 320 * (x+1)
ys = 240 * (y+1)

# also display sphere position and speed
#
# font
font = pygame.font.Font("freesansbold.ttf", 16)
# text
textPositionSurf = font.render("Ball Position: (%d, %d)" % (xs, ys), True, BLACK, BGCOLOR)
textSpeedSurf = font.render("Ball Speed: (%6.2f, %6.2f), %6.2f" % (vx, vy, math.sqrt(vx**2+vy**2)), True, BLACK, BGCOLOR)
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

    # update sphere position and velocity
    F1 = vx
    G1 = -x
    F2 = vx + 0.5 * dt * G1
    G2 = -x - 0.5 * dt * F1
    F3 = vx + 0.5 * dt * G2
    G3 = -x - 0.5 * dt * F2
    F4 = vx + dt * G3
    G4 = -x - dt * F3

    x = x + dt/6. * (F1 + 2.*F2 + 2.*F3 + F4)
    vx = vx + dt/6. * (G1 + 2.*G2 + 2.*G3 + G4)

    F1 = vy
    G1 = -y
    F2 = vy + 0.5 * dt * G1
    G2 = -y - 0.5 * dt * F1
    F3 = vy + 0.5 * dt * G2
    G3 = -y - 0.5 * dt * F2
    F4 = vy + dt * G3
    G4 = -y - dt * F3

    y = y + dt/6. * (F1 + 2.*F2 + 2.*F3 + F4)
    vy = vy + dt/6. * (G1 + 2.*G2 + 2.*G3 + G4)

    xs = 320 * (x+1)
    ys = 240 * (y+1)

    # set text
    textPositionSurf = font.render("Ball Position: (%d, %d)" % (xs, ys), True, BLACK, BGCOLOR)
    textSpeedSurf = font.render("Ball Speed: (%6.2f, %6.2f), %6.2f" % (vx, vy, math.sqrt(vx**2+vy**2)), True, BLACK, BGCOLOR)

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
