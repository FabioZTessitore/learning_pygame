import pygame

screenSize = (width, height) = (640, 480)

WHITE = (255, 255, 255)

pygame.init()

screen = pygame.display.set_mode(screenSize)
pygame.display.set_caption("Png Image")

sphere = pygame.image.load('./png/red_sphere.png')
posSphere = (60, 480-64)

done = False

while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done = True

    screen.fill(WHITE)

    screen.blit(sphere, posSphere)

    pygame.display.flip()

pygame.quit()
