import pygame

pygame.init()

screenSize = (640, 480)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode(screenSize)
pygame.display.set_caption("A Simple Window")

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(WHITE)

    pygame.display.flip()

pygame.quit()
