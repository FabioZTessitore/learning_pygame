# 0012_button1.py

# an interactive button

import pygame

pygame.init()

# screen data
SCREENSIZE = (640, 480)
SCREEN_BGCOLOR = (255, 255, 255)

# button colors
BTN_BACKGROUND = (0, 102, 153)
BTN_INACTIVE = (234, 167, 65)   # orange
BTN_ACTIVE = (255, 200, 100)    # light orange
# button font
startBtnFont = pygame.font.Font("freesansbold.ttf", 42)

FPS = 30

screen = pygame.display.set_mode(SCREENSIZE)
pygame.display.set_caption("Button")

startBtnTextSurf = startBtnFont.render(
    "Press this button to start",
    True,                   # antialiasing
    BTN_INACTIVE,           # foreground
    BTN_BACKGROUND          # background
)   
startBtnTextRect = startBtnTextSurf.get_rect()
startBtnTextRect.center = screen.get_rect().center

clock = pygame.time.Clock()

done = False

# fake mouse position
mouse = (0, 0)

# game loop
while not done:
    # events
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done = True
        # get mouse position
        if event.type == pygame.MOUSEMOTION:
            mouse = event.pos

    # set startBtn background color
    if startBtnTextRect.x < mouse[0] < startBtnTextRect.x + startBtnTextRect.w and \
            startBtnTextRect.y < mouse[1] < startBtnTextRect.y + startBtnTextRect.h:
        btn_color = BTN_ACTIVE
    else:
        btn_color = BTN_INACTIVE

    screen.fill(SCREEN_BGCOLOR)

    # create and blit the text
    startBtnTextSurf = startBtnFont.render(
        "Press this button to start",
        True,                           # antialiasing
        btn_color,                      # foreground
        BTN_BACKGROUND                  # background
    )   
    screen.blit(startBtnTextSurf, startBtnTextRect)

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
