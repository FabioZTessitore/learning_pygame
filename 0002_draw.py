import pygame

pygame.init()

screenSize = (640, 480)

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

screen = pygame.display.set_mode(screenSize)
pygame.display.set_caption("Drawing ...")


done = False

while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done = True

    screen.fill(WHITE)

    # draw some lines
    for i in range(10):
        pygame.draw.line(screen, GREEN, (20+i*10, 100+i*30), (620-i*10, 100+i*30))

    # draw some rect(screen, Color, (x, y, width, height))
    pygame.draw.rect(screen, RED, (20, 20, 100, 20))
    pygame.draw.rect(screen, RED, [screen.get_rect().width-20-100, 20, 100, 20])

    pygame.display.flip()

pygame.quit()
