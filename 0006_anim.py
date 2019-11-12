# 0006_anim.py

# animation of boxes

import pygame

# An animated box
class Box:
    def __init__(self, (left, top, width, height), font, bgcolor, fgcolor, (dx, dy)):
        self.font = font
        self.bgcolor = bgcolor
        self.fgcolor = fgcolor
        self.dx = dx
        self.dy = dy
        self.rect = pygame.Rect(left, top, width, height)
    
    def draw(self, surface):
        pygame.draw.rect(surface, self.bgcolor, self.rect)

        textSurface = self.font.render("(%d, %d)" % (self.rect.left, self.rect.top), True, self.fgcolor, self.bgcolor)
        textRect = textSurface.get_rect()
        textRect.center = (self.rect.left+self.rect.width/2, self.rect.top+self.rect.height/2)
        surface.blit(textSurface, textRect)
    
    def update(self, surfaceWidth, surfaceHeight):
        self.rect.left += self.dx
        self.rect.top += self.dy

        if self.rect.left < 0 or self.rect.left > surfaceWidth-self.rect.width:
            self.dx = -self.dx
        
        if self.rect.top < 0 or self.rect.top > surfaceHeight-self.rect.height:
            self.dy = -self.dy


SCREENSIZE = (WIDTH, HEIGHT) = (640, 480)

BGCOLOR = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (200, 200, 200)

# frames per second
FPS = 30

pygame.init()

windowSurface = pygame.display.set_mode(SCREENSIZE)

pygame.display.set_caption("Animation")

# import the font
font = pygame.font.Font("freesansbold.ttf", 16)

# create some boxes
b1 = Box((30, 30, 100, 100), font, BLACK, GREY, (2, 2))
b2 = Box((130, 230, 100, 100), font, BLACK, GREY, (-2, 2))
boxes = [b1, b2]

# init the clock
clock = pygame.time.Clock()

done = False

# game loop
while not done:
    # events
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done = True

    # update boxes position and direction
    for b in boxes:
        b.update(WIDTH, HEIGHT)

    windowSurface.fill(BGCOLOR)

    # draw the boxes
    for b in boxes:
        b.draw(windowSurface)

    pygame.display.update()

    # pause to mantain FPS
    clock.tick(FPS)

pygame.quit()
