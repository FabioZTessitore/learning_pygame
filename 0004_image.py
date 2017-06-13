import pygame

screen_size = (width, height) = (640, 480)

WHITE = (255, 255, 255)

pygame.init()

screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Png Image")

sfera = pygame.image.load('./png/sfera_rossa.png')
pos_sfera = (60, 400)

screen.fill(WHITE)

screen.blit(sfera, pos_sfera)

done = False

while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done = True

    pygame.display.flip()

pygame.quit()
