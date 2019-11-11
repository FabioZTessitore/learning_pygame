# 0004_text.py

# display text

import pygame

SCREENSIZE = (640, 480)

BGCOLOR = (255, 255, 255)
BLUE = (0, 102, 153)
ORANGE = (234, 167, 65)

pygame.init()

windowSurface = pygame.display.set_mode(SCREENSIZE)

pygame.display.set_caption("Text")

# import the font
font = pygame.font.Font("freesansbold.ttf", 50)
# make the text surface using the selected font
textSurface = font.render(
        "Hello, World!",    # string to display
        True,               # antialiasing
        ORANGE,             # foreground color
        BLUE                # background color
)
# set text position
# set "text center" to "screen center"
textRect = textSurface.get_rect()
# textRect.centerx = screen.get_rect().centerx
# textRect.centery = screen.get_rect().centery
textRect.center = windowSurface.get_rect().center

# fill the window surface with the background color, just once
windowSurface.fill(BGCOLOR)

# draw the text onto the surface
windowSurface.blit(textSurface, textRect)

# draw the window surface onto the screen
pygame.display.update()

done = False

# game loop
while not done:
    # events
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done = True

pygame.quit()
