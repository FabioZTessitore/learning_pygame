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

# lines
lines = []
# first line starts at (20, 100) and ends at (620, 100)
xi = 20
xf = 620
y = 100
lineStart = (xi, y)
lineEnd = (xf, y)
lines.append( (lineStart, lineEnd) )

# next lines
for i in range(9):
    xi += 10        # a little smaller
    xf -= 10        #
    y += 30         # up 30px
    lineStart = (xi, y)
    lineEnd = (xf, y)
    lines.append( (lineStart, lineEnd) )

done = False

# game loop
while not done:
    # events
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done = True

    # clear the screen
    screen.fill(BGCOLOR)

    # draw the lines
    # pygame.draw.lines(screen, Color, (x, y), (x, y))
    for line in lines:
        pygame.draw.line(screen, GREEN, line[0], line[1])

    # draw some rect(screen, Color, (x, y, width, height))
    pygame.draw.rect(screen, RED, (20, 20, 100, 20))
    pygame.draw.rect(screen, RED, [screen.get_rect().width-20-100, 20, 100, 20])

    pygame.display.flip()

pygame.quit()
