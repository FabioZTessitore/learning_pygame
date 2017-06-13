import pygame

pygame.init()

screen_size = (640, 480)

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Drawing ...")

screen.fill(WHITE)

# draw some rect (x, y, width, height)

# top left
pygame.draw.rect(screen, RED, (20, 20, 100, 20))

# top right
pygame.draw.rect(screen, RED, [screen.get_rect().width-20-100, 20, 100, 20])

# draw some lines
for i in range(10):
    pygame.draw.line(screen, GREEN, (20+i*10, 100+i*30), (620-i*10, 100+i*30))

done = False

while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done = True
    
    pygame.display.flip()

pygame.quit()
