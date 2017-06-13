import pygame

screen_size = (640, 480)

WHITE = (255, 255, 255)
BLUE = (0, 102, 153)
ORANGE = (234, 167, 65)

pygame.init()

screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Text")

font = pygame.font.Font("freesansbold.ttf", 50)
textSurf = font.render("Hello, World!",
        True, # antialiasing
        ORANGE,
        BLUE)
textRect = textSurf.get_rect()
textRect.centerx = screen.get_rect().centerx
textRect.centery = screen.get_rect().centery

screen.fill(WHITE)

screen.blit(textSurf, textRect)

done = False

while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done = True
    
    pygame.display.flip()

pygame.quit()
