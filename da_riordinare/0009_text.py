# 0009_text.py

# display text

import pygame

SCREENSIZE = (640, 480)

BGCOLOR = (255, 255, 255)
BLUE = (0, 102, 153)
ORANGE = (234, 167, 65)

pygame.init()

screen = pygame.display.set_mode(SCREENSIZE)
pygame.display.set_caption("Text")

# import the font
font = pygame.font.Font("freesansbold.ttf", 50)
# make the text surface using
# the selected font
textSurf = font.render(
        "Hello, World!",    # string to show
        True,               # antialiasing
        ORANGE,             # foreground color
        BLUE                # background color
)
# set text position
# set "text center" to "screen center"
textRect = textSurf.get_rect()
#textRect.centerx = screen.get_rect().centerx
#textRect.centery = screen.get_rect().centery
textRect.center = screen.get_rect().center

done = False

# game loop
while not done:
    # events
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done = True

    screen.fill(BGCOLOR)

    # blit the text
    screen.blit(textSurf, textRect)

    pygame.display.flip()

pygame.quit()
