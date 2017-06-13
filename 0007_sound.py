import pygame

screen_size = (640, 480)

FPS = 30

WHITE = (255, 255, 255)
BLUE = (0, 102, 153)
ORANGE = (234, 167, 65)

pygame.init()

screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Sound")

font = pygame.font.Font("freesansbold.ttf", 42)
textSurf = font.render("Can You Hear the Sounds?",
        True, # antialiasing
        ORANGE,
        BLUE)
textRect = textSurf.get_rect()
textRect.centerx = screen.get_rect().centerx
textRect.centery = screen.get_rect().centery

screen.fill(WHITE)

screen.blit(textSurf, textRect)

# background music (forever loop)
pygame.mixer.music.load('./music/JenyfaDuncan-Australia.ogg')
pygame.mixer.music.play(-1, 0.0)

# every 5 sec
laser = pygame.mixer.Sound('./sound/laser5.ogg')

counter = 0

clock = pygame.time.Clock()

done = False

while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done = True

    counter += 1
    if counter % (FPS*5) == 0:
        laser.play()
    
    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
