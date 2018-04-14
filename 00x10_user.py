import pygame

screen_size = (screen_width, screen_height) = (640, 480)

FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (100, 100, 100)
RED = (255, 0, 0)

class Box:
    def __init__(self, x, y, dx, dy):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.width = 100
        self.height = 100

    def speedUp(self):
        if self.dx >= 0:
            self.inc_dx()
        else:
            self.dec_dx()

    def speedDown(self):
        if self.dx >= 0:
            self.dec_dx()
        else:
            self.inc_dx()

    def inc_dx(self):
        self.dx += 2

    def dec_dx(self):
        self.dx -= 2

    def update(self):
        self.x += self.dx
        self.y += self.dy

    def checkPos(self, limitX, limitY):
        if self.x < 0 or self.x + self.width > limitX:
            self.dx = -self.dx
        if self.y < 0 or self.y + self.height > limitY:
            self.dy = -self.dy

    def draw(self, screen):
        pygame.draw.rect(screen, BLACK, [self.x, self.y, self.width, self.height])
        pygame.draw.rect(screen, RED, [self.x+5, self.y+5, self.width-10, self.height-10])

box = Box(300, 200, 2, 2)

pygame.init()

screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Bouncing ...")

headerFont = pygame.font.Font("freesansbold.ttf", 18)
headerTextSurface = headerFont.render("Bouncing Box", True, RED)
headerTextPos = headerTextSurface.get_rect()
headerTextPos.topleft = (10, 10)

infoFont = pygame.font.Font("freesansbold.ttf", 14)
infoTextSurface = infoFont.render('Press Arrows UP and DOWN to modify Box speed', True, BLACK)
infoTextPos = infoTextSurface.get_rect()
infoTextPos.topleft = (10, 30)

debugFont = pygame.font.Font("freesansbold.ttf", 16)
debugTextSurface = debugFont.render('DX: %d    DY: %d' % (box.dx, box.dy), True, GREY)
debugTextPos = debugTextSurface.get_rect()
debugTextPos.topleft = (10, 50)

clock = pygame.time.Clock()

done = False

while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done = True
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                box.speedUp()
            elif event.key==pygame.K_DOWN:
                box.speedDown()

    screen.fill(WHITE)

    screen.blit(headerTextSurface, headerTextPos)
    screen.blit(infoTextSurface, infoTextPos)
    debugTextSurface = debugFont.render('DX: %d    DY: %d' % (box.dx, box.dy), True, GREY)
    screen.blit(debugTextSurface, debugTextPos)

    box.update()
    box.checkPos(screen_width, screen_height)
    box.draw(screen)

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
