# 0001_draw.py

# a draw

import pygame

pygame.init()

SCREENSIZE = (640, 480)

BLACK = (0, 0, 0)
CYAN = (0, 100, 200)
GREEN = (0, 180, 0)
FOLIAGE = (0, 100, 0)
BROWN = (130, 70, 20)

BGCOLOR = CYAN

screen = pygame.display.set_mode(SCREENSIZE)
pygame.display.set_caption("A Draw")

greenField = (0, 320, 640, 160)

# wood: (x, y, width, height)
woods = []
woods.append( (200, 240, 60, 160) )
woods.append( (400, 280, 30, 80) )

# foliage: ((x, y), radius)
foliages = []
foliages.append( ((230, 240), 100) )
foliages.append( ((415, 280), 40) )

# bird: ( birdPart1, birdPart2 )
# where a birdPart is (LineStart, LineEnd)
birds = []
birds.append( (
    ( (320, 30), (330, 40) ),   # Part 1
    ( (330, 40), (340, 30) )    # Part 2
))
birds.append( (
    ( (500, 40), (510, 45) ),   # Part 1
    ( (510, 45), (520, 40) )    # Part 2
))
done = False

# game loop
while not done:
    # events
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done = True

    # clear the screen
    screen.fill(BGCOLOR)

    # draw some rect(screen, Color, (x, y, width, height))
    pygame.draw.rect(screen, GREEN, greenField)
    for wood in woods:
        pygame.draw.rect(screen, BROWN, wood)

    # draw circles
    for foliage in foliages:
        position, radius = foliage
        pygame.draw.circle(screen, FOLIAGE, position, radius)

    # draw the lines
    # pygame.draw.lines(screen, Color, (x, y), (x, y))
    for bird in birds:
        birdsPt1, birdsPt2 = bird
        birdsPt1Start, birdsPt1End = birdsPt1
        birdsPt2Start, birdsPt2End = birdsPt2
        pygame.draw.line(screen, BLACK, birdsPt1Start, birdsPt1End, 2)
        pygame.draw.line(screen, BLACK, birdsPt2Start, birdsPt2End, 2)

    #for line in lines:


    pygame.display.flip()

pygame.quit()
