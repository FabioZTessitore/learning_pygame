import pygame

pygame.init()

screen_size = (640, 480)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("A Simple Window")

done = False

# per il momento qui!
screen.fill(WHITE)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pygame.display.flip()

pygame.quit()
