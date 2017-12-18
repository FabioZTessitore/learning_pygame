import pygame

screenSize = (width, height) = (640, 480)

FPS = 30

WHITE = (255, 255, 255)

pygame.init()

screen = pygame.display.set_mode(screenSize)
pygame.display.set_caption("Animation")

sphere = pygame.image.load('./png/red_sphere.png')
sphereRect = sphere.get_rect()
(sphereWidth, sphereHeight) = (sphereRect.width, sphereRect.height)
(sphereX, sphereY) = (60, 480-64)

sphereDx = 2
sphereDy = 2

clock = pygame.time.Clock()

done = False

while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done = True

    (sphereX, sphereY) = (sphereX + sphereDx, sphereY + sphereDy)

    if sphereX < 0 or sphereX + sphereWidth > width:
        sphereDx = -sphereDx
    if sphereY < 0 or sphereY + sphereHeight > height:
        sphereDy = -sphereDy

    screen.fill(WHITE)

    screen.blit(sphere, (sphereX, sphereY))

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
