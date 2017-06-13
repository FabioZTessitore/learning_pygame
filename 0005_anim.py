import pygame


screen_size = (width, height) = (640, 480)

FPS = 60

WHITE = (255, 255, 255)

pygame.init()

screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Animation")

sfera = pygame.image.load('./png/sfera_rossa.png')
sfera_rect = sfera.get_rect()
(sfera_width, sfera_height) = (sfera_rect.width, sfera_rect.height)
(sfera_x, sfera_y) = (60, 400)

sfera_dx = 2
sfera_dy = 2

clock = pygame.time.Clock()

done = False

while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done = True

    screen.fill(WHITE)

    sfera_x += sfera_dx
    sfera_y += sfera_dy

    if sfera_x < 0 or sfera_x + sfera_width > width:
        sfera_dx = -sfera_dx
    if sfera_y < 0 or sfera_y + sfera_height > height:
        sfera_dy = -sfera_dy
    
    screen.blit(sfera, (sfera_x, sfera_y))

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
