import pygame
import random

screen_size = (width, height) = (720, 480)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Block(pygame.sprite.Sprite):
    def __init__(self, filename, n_frames, width, height):
        super(Block, self).__init__()

        self.sprite_sheet = pygame.image.load(filename).convert()
       
        self.images = []
        for i in range(n_frames):
            self.images.append(pygame.Surface((width, height)))

        for i in range(n_frames):
            self.images[i].blit(self.sprite_sheet, (0, 0), (0, height*i, width, height))
  
        self.rect = self.images[0].get_rect()
        self.index = 0
        self.image = self.images[self.index]
        self.k = random.randrange(15)

    def anim_sprite(self):
        if self.k % 15 == 0:
            self.index = (self.index+1) % 2
            self.image = self.images[self.index]
            self.k = 0
        self.k += 1

    def reset_pos(self):
        self.rect.x = random.randrange(width-20)
        self.rect.y = random.randrange(-200, -10)
        
    def update(self):
        self.rect.y += 1
        if self.rect.y > height:
            self.reset_pos()
        self.anim_sprite()

pygame.init()

screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("sprite ...")

font = pygame.font.SysFont("Calibri", 40)

clock = pygame.time.Clock()

block_list = pygame.sprite.Group()
all_sprite_list = pygame.sprite.Group()

for i in range(50):
    block = Block('pesciolino_grande.png', 7, 96, 28)

    block.rect.x = random.randrange(width-20)
    block.rect.y = random.randrange(height-15)

    block_list.add(block)
    all_sprite_list.add(block)

player = Block('pesciolino2.png', 2, 48, 48)
all_sprite_list.add(player)

done = False
score = 0

while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done = True

    (posx, posy) = pygame.mouse.get_pos()
    player.rect.x = posx-24
    player.rect.y = posy-24

    block_list.update()
    player.anim_sprite()

    hit_list = pygame.sprite.spritecollide(player, block_list, False)
    for hit in hit_list:
        score += 1
        hit.reset_pos()

    screen.fill(WHITE)

    all_sprite_list.draw(screen)

    score_text = font.render("Score: %d" % (score,), True, BLACK)
    screen.blit(score_text, (screen.get_rect()[2]-score_text.get_rect().width, score_text.get_rect()[1]))
    
    pygame.display.flip()

    clock.tick(30)

pygame.quit()
