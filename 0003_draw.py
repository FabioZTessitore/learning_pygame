# 0003_draw.py

# draw lines and rects

import pygame

pygame.init()

SCREENSIZE = (640, 480)

BGCOLOR= (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

screen = pygame.display.set_mode(SCREENSIZE)
pygame.display.set_caption("Lines and Rects")

lineStart = (20, 100)
lineEnd = (420, 300)

done = False

# game loop
while not done:
    # events
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done = True

    # clear the screen
    screen.fill(BGCOLOR)

    # draw the line
    # pygame.draw.lines(screen, Color, (x, y), (x, y))
    pygame.draw.line(screen, GREEN, lineStart, lineEnd)

    # draw some rect(screen, Color, (x, y, width, height))
    pygame.draw.rect(screen, RED, (20, 20, 100, 20))
    pygame.draw.rect(screen, RED, [screen.get_rect().width-20-100, 20, 100, 20])

    pygame.display.flip()

pygame.quit()
