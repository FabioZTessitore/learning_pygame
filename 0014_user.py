# 0014_user.py

# a simple "game"
# user can modify the velocity of a red box
# while it bounces on the screen
#
# To start the game, the user must click on a button

import pygame

pygame.init()

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# screen data
SCREENSIZE = (640, 480)
SCREEN_BGCOLOR = WHITE

# animation parameters
FPS = 60

# screen
screen = pygame.display.set_mode(SCREENSIZE)
pygame.display.set_caption('A simple game')

# description
DESCR_COLOR = (155, 40, 20)
DESCR_BGCOLOR = WHITE
descr1 = "A simple game"
descr2 = "press Key Up/Down Left/Right"
descr3 = "to change box speed"
descr1Font = pygame.font.Font("freesansbold.ttf", 42)
descr2Font = pygame.font.Font("freesansbold.ttf", 30)
descr1TextSurf = descr1Font.render(
        descr1,
        True,           # antialiasing
        DESCR_COLOR,    # fg
        DESCR_BGCOLOR   # bg
)
descr2TextSurf = descr2Font.render(
        descr2,
        True,           # antialiasing
        DESCR_COLOR,    # fg
        DESCR_BGCOLOR   # bg
)
descr3TextSurf = descr2Font.render(
        descr3,
        True,           # antialiasing
        DESCR_COLOR,    # fg
        DESCR_BGCOLOR   # bg
)
descr1TextRect = descr1TextSurf.get_rect()
descr2TextRect = descr2TextSurf.get_rect()
descr3TextRect = descr3TextSurf.get_rect()
descr1TextRect.centerx = screen.get_rect().centerx
descr2TextRect.centerx = screen.get_rect().centerx
descr3TextRect.centerx = screen.get_rect().centerx
descr1TextRect.centery = 30
descr2TextRect.centery = 90
descr3TextRect.centery = 120

# buttons data
BTN_BACKGROUND = (50, 30, 40)
BTN_INACTIVE = (200, 150, 60)
BTN_ACTIVE = (255, 200, 100)
btnColor = BTN_INACTIVE
btnFont = pygame.font.Font("freesansbold.ttf", 42)

#start button
startBtnTextSurf = btnFont.render(
        "Press this button to start",
        True,
        btnColor,
        BTN_BACKGROUND
)
startBtnTextRect = startBtnTextSurf.get_rect()
startBtnTextRect.center = screen.get_rect().center

#stop button
stopBtnTextSurf = btnFont.render(
        "Press this button to stop",
        True,
        btnColor,
        BTN_BACKGROUND
)
stopBtnTextRect = stopBtnTextSurf.get_rect()
stopBtnTextRect.centerx = screen.get_rect().centerx
stopBtnTextRect.y = SCREENSIZE[1] - 48

# clock
clock = pygame.time.Clock()

# mouse position
mouse = (0, 0)

# red box
boxBorderColor = BLACK
boxColor = RED
boxMinMax = (50, 2000)
boxPos = [0, 0]
boxInnerPos = [boxPos[0]+5, boxPos[1]+5]
boxSpeed = [ boxMinMax[0], boxMinMax[0] ]
boxDim = [100, 100]
boxInnerDim = [90, 90]
boxVel = [1, 1]

done = False

def startScreen():
    global currentState

    if startBtnTextRect.x < mouse[0] < startBtnTextRect.x + startBtnTextRect.w and \
            startBtnTextRect.y < mouse[1] < startBtnTextRect.y + startBtnTextRect.h:
        btnColor = BTN_ACTIVE
        if click:
            currentState = gameScreen
    else:
        btnColor = BTN_INACTIVE

    startBtnTextSurf = btnFont.render(
            "Press this button to start",
            True,
            btnColor,
            BTN_BACKGROUND
    )

    screen.blit(descr1TextSurf, descr1TextRect)
    screen.blit(descr2TextSurf, descr2TextRect)
    screen.blit(descr3TextSurf, descr3TextRect)
    screen.blit(startBtnTextSurf, startBtnTextRect)

def gameScreen():
    global currentState
    global boxPos

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        boxSpeed[1] += 10
        if boxSpeed[1] > boxMinMax[1]:
            boxSpeed[1] = boxMinMax[1]
    if keys[pygame.K_DOWN]:
        boxSpeed[1] -= 10
        if boxSpeed[1] < boxMinMax[0]:
            boxSpeed[1] = boxMinMax[0]
    if keys[pygame.K_RIGHT]:
        boxSpeed[0] += 10
        if boxSpeed[0] > boxMinMax[1]:
            boxSpeed[0] = boxMinMax[1]
    if keys[pygame.K_LEFT]:
        boxSpeed[0] -= 10
        if boxSpeed[0] < boxMinMax[0]:
            boxSpeed[0] = boxMinMax[0]

    if stopBtnTextRect.x < mouse[0] < stopBtnTextRect.x + stopBtnTextRect.w and \
            stopBtnTextRect.y < mouse[1] < stopBtnTextRect.y + stopBtnTextRect.h:
        btnColor = BTN_ACTIVE
        if click:
            currentState = startScreen
    else:
        btnColor = BTN_INACTIVE

    stopBtnTextSurf = btnFont.render(
            "Press this button to stop",
            True,
            btnColor,
            BTN_BACKGROUND
    )

    screen.blit(stopBtnTextSurf, stopBtnTextRect)

    dx = boxVel[0] * boxSpeed[0] / float(FPS)
    dy = boxVel[1] * boxSpeed[1] / float(FPS)
    boxPos[0] += dx
    boxPos[1] += dy
    boxInnerPos = [boxPos[0]+5, boxPos[1]+5]
    
    if boxPos[0] < 0 or boxPos[0] + boxDim[0] > SCREENSIZE[0]:
        boxVel[0] = -boxVel[0]
    if boxPos[1] < 0 or boxPos[1] + boxDim[1] > SCREENSIZE[1]:
        boxVel[1] = -boxVel[1]
    
    pygame.draw.rect(screen, boxBorderColor, boxPos + boxDim)
    pygame.draw.rect(screen, boxColor, boxInnerPos + boxInnerDim)

currentState = startScreen

# game loop
while not done:
    click = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEMOTION:
            mouse = event.pos
        if event.type == pygame.MOUSEBUTTONDOWN:
            click = True

    screen.fill(SCREEN_BGCOLOR)

    currentState()

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
