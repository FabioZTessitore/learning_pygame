# 0013_button2.py

# an interactive button

import pygame

pygame.init()

# screen data
SCREENSIZE = (640, 480)
SCREEN_BGCOLOR = (255, 255, 255)

# buttons colors
BTN_BACKGROUND = (0, 102, 153)
BTN_INACTIVE = (234, 167, 65)   # orange
BTN_ACTIVE = (255, 200, 100)    # light orange
# buttons font
startBtnFont = pygame.font.Font("freesansbold.ttf", 42)
endBtnFont = startBtnFont

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

endBtnTextSurf = endBtnFont.render(
    "Press this button to exit",
    True,
    BTN_INACTIVE,
    BTN_ACTIVE
)
endBtnTextRect = endBtnTextSurf.get_rect()
endBtnTextRect.center = screen.get_rect().center

clock = pygame.time.Clock()

done = False

# game state: 'intro' or 'play'
state = 'intro'

# fake mouse position
mouse = (0, 0)

# game loop
while not done:
    click = False

    # events
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done = True
        # get mouse position
        if event.type == pygame.MOUSEMOTION:
            mouse = event.pos
        # mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:
            click = True

    screen.fill(SCREEN_BGCOLOR)

    if state == 'intro':
        # set startBtn background color
        if startBtnTextRect.x < mouse[0] < startBtnTextRect.x + startBtnTextRect.w and \
                startBtnTextRect.y < mouse[1] < startBtnTextRect.y + startBtnTextRect.h:
            btn_color = BTN_ACTIVE
            if click:
                state = 'play'
        else:
            btn_color = BTN_INACTIVE


        # create and blit the text
        startBtnTextSurf = startBtnFont.render(
            "Press this button to start",
            True,                           # antialiasing
            btn_color,                      # foreground
            BTN_BACKGROUND                  # background
        )   
        screen.blit(startBtnTextSurf, startBtnTextRect)

    elif state == 'play':
        # set endBtn background color
        if endBtnTextRect.x < mouse[0] < endBtnTextRect.x + endBtnTextRect.w and \
                endBtnTextRect.y < mouse[1] < endBtnTextRect.y + endBtnTextRect.h:
            btn_color = BTN_ACTIVE
            if click:
                done = True
        else:
            btn_color = BTN_INACTIVE

        # create and blit the text
        endBtnTextSurf = endBtnFont.render(
            "Press this button to exit",
            True,                           # antialiasing
            btn_color,                      # foreground
            BTN_BACKGROUND                  # background
        )   
        screen.blit(endBtnTextSurf, endBtnTextRect)

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
