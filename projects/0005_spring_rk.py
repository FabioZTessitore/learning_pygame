# 0005_spring_rk.py

# Spring (Runge Kutta integration)
#
#
#
# Runge-Kutta integration
#
# x' = f(t, x, y)   x(t0) = x0
# y' = g(t, x ,y)   y(t0) = y0
#
# x_n+1 = x_n + h/6 (F1 + 2F2 + 2F3 + F4)
# y_n+1 = y_n + h/6 (G1 + 2G2 + 2G3 + G4)
#
# F1 = f(t_n, x_n, y_n)                                 G1 = ...
# F2 = f(t_n + h/2, x_n + h F1/2, y_n + h G1/2)         G2 = ...
# F3 = f(t_n + h/2, x_n + h F2/2, y_n + h G2/2)         G3 = ...
# F4 = f(t_n + h, x_n + h F3, y_n + h G3)               G4 = ...
#
#
# Given
# x'' = g(t, x, x')     x(t0) = x0,     x'(t0) = y0
#
# Write as a system of two equations:
#
# x' = y                x(t0) = x0
# y' = g(t, x, y)       y(t0) = y0
#
#
# In our case:
# x'' = -x              x(0) = 0.9      x'(0) = 0
#
# x' = y                x(0) = 0.9
# y' = -x               y(0) = 0.
#
# f(t, x, y) = y
# g(t, x, y) = -x
#
# F1 = y_n                      G1 = -x_n
# F2 = y_n + 1/2 h G1           G2 = -x_n - 1/2 h F1
# F3 = y_n + 1/2 h G2           G3 = -x_n - 1/2 h F2
# F4 = y_n + h G3               G4 = -x_n - h F3
#
# Frame
# -1 < x < 1
# -1 < y < 1
#
# Screen Size
# Width 640
# Height 480
#
# The ball start at rest at (x, y) = (0.9, 0.)
#
# Screen coordinates:
# xs = 1/2 (1 + x) 640 = 320 * (x + 1)
# ys = 480 / 2 = 240

# frames per second
FPS = 30

# ball real position
x, y = 0.9, 0.
# ball velocity
v0 = 0
v = v0
# acceleration
a = 0.
# time step
dt = 1./FPS

import pygame

SCREENSIZE = (WIDTH, HEIGHT) = (640, 480)

BGCOLOR = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()

screen = pygame.display.set_mode(SCREENSIZE)
pygame.display.set_caption("Spring")

# load the image to animate
sphere = pygame.image.load('../png/red_sphere.png')
sphereRect = sphere.get_rect()

# set sphere position
xs = 320 * (x+1)
ys = 480 / 2.

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
    F1 = v
    G1 = -x
    F2 = v + 0.5 * dt * G1
    G2 = -x - 0.5 * dt * F1
    F3 = v + 0.5 * dt * G2
    G3 = -x - 0.5 * dt * F2
    F4 = v + dt * G3
    G4 = -x - dt * F3

    x = x + dt/6. * (F1 + 2.*F2 + 2.*F3 + F4)
    v = v + dt/6. * (G1 + 2.*G2 + 2.*G3 + G4)

    xs = 320 * (x+1)
    ys = 480 / 2

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
