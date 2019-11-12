# 0009_collisions.py

# rect collisions

import pygame
import random

def getRandomSpeed():
    return random.choice([+1, -1]) * random.randrange(1, 4)

def getRandomSize():
    return random.randrange(30, 60)

# An animated box
###################################################################
# here it's very important to have the Rect member called "rect", #
# so collidelist() can work properly!                             #
###################################################################
class Box:
    def __init__(self, (left, top, width, height), bgcolor, (dx, dy)):
        self.bgcolor = bgcolor
        self.dx = dx
        self.dy = dy
        self.rect = pygame.Rect(left, top, width, height)
    
    def draw(self, surface):
        pygame.draw.rect(surface, self.bgcolor, self.rect)
    
    def update(self, surfaceWidth, surfaceHeight):
        self.rect.left += self.dx
        self.rect.top += self.dy

        if self.rect.left < 0 or self.rect.left > surfaceWidth-self.rect.width:
            self.dx = -self.dx
        
        if self.rect.top < 0 or self.rect.top > surfaceHeight-self.rect.height:
            self.dy = -self.dy


SCREENSIZE = (WIDTH, HEIGHT) = (640, 480)

BGCOLOR = GREY = (200, 200, 200)
DARK_GREY = (50, 50, 50)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# frames per second
FPS = 30

pygame.init()

windowSurface = pygame.display.set_mode(SCREENSIZE)

pygame.display.set_caption("Collisions")

# import the font
font = pygame.font.Font("freesansbold.ttf", 16)
#
text1Surface = font.render("Use Arrow Keys to move the player", True, DARK_GREY, BGCOLOR)
text1Rect = text1Surface.get_rect()
text1Rect.left = 30
text1Rect.top = 30
#
text2Surface = font.render("Click to create new box", True, DARK_GREY, BGCOLOR)
text2Rect = text2Surface.get_rect()
text2Rect.left = 30
text2Rect.top = 60

boxes = []

# the player is a BLACK box, starting at WIDTH-130, 30,
# sized 100x100, at rest (0, 0)
player = Box((WIDTH-130, 30, 100, 100), BLACK, (0, 0))

# init the clock
clock = pygame.time.Clock()

done = False

# game loop
while not done:
    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        
        # on mouse button down create a new box
        if event.type == pygame.MOUSEBUTTONDOWN:
            size = getRandomSize()
            dx = getRandomSpeed()
            dy = getRandomSpeed()
            b = Box((30, 30, size, size), DARK_GREY, (dx, dy))
            boxes.append(b)

    # get_pressed() return a map of pressed keys
    keys = pygame.key.get_pressed()

    # move the player with arrow key
    player.dx = player.dy = 0
    #
    if keys[pygame.K_UP]:
        player.dy = -1
    #
    if keys[pygame.K_DOWN]:
        player.dy = 1
    #
    if keys[pygame.K_LEFT]:
        player.dx = -1
    #
    if keys[pygame.K_RIGHT]:
        player.dx = 1

    # update boxes position and direction
    for b in boxes:
        b.update(WIDTH, HEIGHT)
    #
    player.update(WIDTH, HEIGHT)

    # check for collisions
    index = player.rect.collidelist(boxes)
    if index >= 0:
        del boxes[index]

    text1Surface = font.render("Use Arrow Keys to move the player", True, DARK_GREY, BGCOLOR)
    text2Surface = font.render("Click to create new box", True, DARK_GREY, BGCOLOR)

    windowSurface.fill(BGCOLOR)

    windowSurface.blit(text1Surface, text1Rect)
    windowSurface.blit(text2Surface, text2Rect)

    # draw the boxes
    for b in boxes:
        b.draw(windowSurface)
    #
    player.draw(windowSurface)

    pygame.display.update()

    # pause to mantain FPS
    clock.tick(FPS)

pygame.quit()
