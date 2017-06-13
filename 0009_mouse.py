import pygame

screen_size = (640, 480)

FPS = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()

screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Drawing ...")

font = pygame.font.Font("freesansbold.ttf", 18)
helpText = font.render("Click to draw lines", True, BLACK)
helpTextPos = helpText.get_rect()
helpTextPos.centerx = screen.get_rect().centerx
helpTextPos.y = 15

mouseText = font.render("Mouse X: %d   Y: %d" % (0, 0), True, BLACK)
mouseTextPos = mouseText.get_rect()
mouseTextPos.topleft = (10, 10)

clock = pygame.time.Clock()

done = False

first_click = True
lines = []

while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done = True
        if event.type==pygame.MOUSEBUTTONDOWN:
            if first_click:
                first_click = False
                first_pos = event.pos
            else:
                first_click = True
                lines.append((first_pos, event.pos))

    screen.fill(WHITE)

    screen.blit(helpText, helpTextPos)

    mouseText = font.render("Mouse X: %d   Y: %d" % pygame.mouse.get_pos(), True, BLACK)
    screen.blit(mouseText, mouseTextPos)


    for line in lines:
        pygame.draw.line(screen, BLACK, line[0], line[1])

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
