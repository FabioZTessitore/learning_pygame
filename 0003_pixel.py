import pygame

pygame.init()

screen_size = (640, 480)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Drawing ...")

screen.fill(WHITE)

# pixel
pixel = pygame.PixelArray(screen)
for c in range(screen_size[0]):
    startAt = c % 2
    for r in range(startAt, screen_size[1], 2):
        pixel[c][r] = BLACK
del pixel

done = False

while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done = True
    
    pygame.display.flip()

pygame.quit()
