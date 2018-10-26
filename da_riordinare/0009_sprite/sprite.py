import pygame
import random

screen_size = (width, height) = (600, 400)

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

class Block(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super(Block, self).__init__()

        self.image = pygame.Surface((width, height))
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        pygame.draw.ellipse(self.image, color, (0, 0, width, height))

        self.rect = self.image.get_rect()

    def reset_pos(self):
        self.rect.x = random.randrange(width-20)
        self.rect.y = random.randrange(-200, -10)
        
    def update(self):
        self.rect.y += 1
        if self.rect.y > height:
            self.reset_pos()



pygame.init()

screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("sprite ...")

clock = pygame.time.Clock()

block_list = pygame.sprite.Group()
all_sprite_list = pygame.sprite.Group()

for i in range(50):
    block = Block(BLACK, 20, 15)

    block.rect.x = random.randrange(width-20)
    block.rect.y = random.randrange(height-15)

    block_list.add(block)
    all_sprite_list.add(block)

player = Block(RED, 20, 15)
all_sprite_list.add(player)

done = False
score = 0

while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done = True

    (posx, posy) = pygame.mouse.get_pos()
    player.rect.x = posx-10
    player.rect.y = posy-7

    block_list.update()

    hit_list = pygame.sprite.spritecollide(player, block_list, False)
    for hit in hit_list:
        score += 1
        print score
        hit.reset_pos()

    screen.fill(WHITE)

    all_sprite_list.draw(screen)
    
    pygame.display.flip()

    clock.tick(30)

pygame.quit()
