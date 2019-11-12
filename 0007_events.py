# 0007_events.py

# mouse and keyboard events

def reduceAmount(amount, variation):
    amount -= variation
    if amount < 0:
        amount = 0

    return amount

def increaseAmount(amount, variation):
    amount += variation
    if amount > 255:
        amount = 255

    return amount


import pygame

SCREENSIZE = (WIDTH, HEIGHT) = (640, 480)

redAmount = 0
redVariation = 10
BGCOLOR = (redAmount, 0, 0)
GREY = (200, 200, 200)

# frames per second
FPS = 30

pygame.init()

windowSurface = pygame.display.set_mode(SCREENSIZE)

pygame.display.set_caption("Events")

# import the font
font = pygame.font.Font("freesansbold.ttf", 16)
#
text1Surface = font.render("Click on the left of the screen or press KeyDown to reduce red amount", True, GREY, BGCOLOR)
text1Rect = text1Surface.get_rect()
text1Rect.left = 30
text1Rect.top = 30
#
text2Surface = font.render("Click on the right of the screen or press KeyUp to increase red amount", True, GREY, BGCOLOR)
text2Rect = text2Surface.get_rect()
text2Rect.left = 30
text2Rect.top = 60

# init the clock
clock = pygame.time.Clock()

done = False

# game loop
while not done:
    # events
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done = True

        # mouse events
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.pos[0] < WIDTH/2:
                redAmount = reduceAmount(redAmount, redVariation)
            else:
                redAmount = increaseAmount(redAmount, redVariation)
        
        # keyboard events
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                redAmount = reduceAmount(redAmount, redVariation)
            elif event.key == pygame.K_UP:
                redAmount = increaseAmount(redAmount, redVariation)

    # recalculate bg color with current red amount
    BGCOLOR = (redAmount, 0, 0)

    text1Surface = font.render("Click on the left of the screen or press KeyDown to reduce red amount", True, GREY, BGCOLOR)
    text2Surface = font.render("Click on the right of the screen or press KeyUp to increase red amount", True, GREY, BGCOLOR)

    windowSurface.fill(BGCOLOR)

    windowSurface.blit(text1Surface, text1Rect)
    windowSurface.blit(text2Surface, text2Rect)

    pygame.display.update()

    # pause to mantain FPS
    clock.tick(FPS)

pygame.quit()
