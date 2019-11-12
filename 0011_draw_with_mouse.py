# 0011_draw_with_mouse.py

# draw lines with the mouse

import pygame

class Line:
    def __init__(self, color):
        self.color = color
        self.start = ()
        self.end = ()
    
    def draw(self, surface):
        pygame.draw.line(surface, self.color, self.start, self.end)

    def setColor(self, color):
        self.color = color
    
    def setStart(self, start):
        self.start = start
    
    def setEnd(self, end):
        self.end = end


SCREENSIZE = (640, 480)

BGCOLOR = (255, 255, 255)
BLACK = (0, 0, 0)           # lines color
GREEN = (0, 255, 0)         # temp line color

FPS = 30

pygame.init()

windowSurface = pygame.display.set_mode(SCREENSIZE)

pygame.display.set_caption("Draw with the mouse")

# status
NO_CLICK = 'no-click'
FIRST_CLICK = 'first-click'

status = NO_CLICK

lines = []

currentLine = Line(GREEN)

clock = pygame.time.Clock()

done = False

# game loop
while not done:
    # events
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done = True

        # mouse events

        # click handler
        if event.type == pygame.MOUSEBUTTONDOWN:
            if status == FIRST_CLICK:
                # second click
                currentLine.setEnd(event.pos)
                currentLine.setColor(BLACK)
                lines.append(currentLine)
                currentLine = Line(GREEN)
                status = NO_CLICK
            else:
                # first click
                position = event.pos
                currentLine.setStart(position)
                currentLine.setEnd(position)
                status = FIRST_CLICK

        # motion handler
        if event.type == pygame.MOUSEMOTION:
            if status == FIRST_CLICK:
                currentLine.setEnd(event.pos)

    windowSurface.fill(BGCOLOR)

    # draw the lines
    for line in lines:
        line.draw(windowSurface)

    # draw current line
    if status == FIRST_CLICK:
        currentLine.draw(windowSurface)

    pygame.display.update()

    clock.tick(FPS)

pygame.quit()
