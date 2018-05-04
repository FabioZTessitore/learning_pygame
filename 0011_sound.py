# 0011_sound.py

# sound

import pygame

SCREENSIZE = (640, 480)

BGCOLOR = (255, 255, 255)
BLUE = (0, 102, 153)
ORANGE = (234, 167, 65)

FPS = 30

pygame.init()

screen = pygame.display.set_mode(SCREENSIZE)
pygame.display.set_caption("Sound")

font = pygame.font.Font("freesansbold.ttf", 42)
textSurf = font.render(
        "Can You Hear the Sounds?",
        True,                           # antialiasing
        ORANGE,                         # foreground
        BLUE                            # background
)   
textRect = textSurf.get_rect()
textRect.centerx = screen.get_rect().centerx
textRect.centery = screen.get_rect().centery

# background music (forever loop)
pygame.mixer.music.load('./music/JenyfaDuncan-Australia.ogg')
pygame.mixer.music.play(
        -1,     # loops
        0.0     # start
)

# every 5 sec
laser = pygame.mixer.Sound('./sound/laser5.ogg')

counter = 0

clock = pygame.time.Clock()

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

    # every 5 sec play a sound
    counter += 1
    if counter % (FPS*5) == 0:
        laser.play()

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
