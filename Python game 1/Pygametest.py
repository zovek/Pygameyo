#importing pygame
import pygame
pygame.init()
import random
import math

#defining color variables
BLACK = (  0,  0,  0)
WHITE = (255,255,255)
RED   = (255,  0,  0)
GREEN = (  0,255,  0)
BLUE  = (  0,  0,255)

#window settings
size = (800, 800)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Test Pygame Game")

#setting fps variable
clock = pygame.time.Clock()

#creating a variable that starts main loop.
done = False

#global variables
x_offset = 0
y_offset = 0



#***classes under***
class Block(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        
    



#defining groups
block_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()
red_blocks = pygame.sprite.Group()
black_blocks = pygame.sprite.Group()
#creating player sprite
player = Block(GREEN, 10,10)
all_sprites_list.add(player)
#creating sprites
for i in range(20):
    b_block = Block(BLACK, 20,20)
    r_block = Block(RED, 20,20)


    b_block.rect.x= random.randrange(800-20)
    b_block.rect.y= random.randrange(800-20)

    r_block.rect.x= random.randrange(800-20)
    r_block.rect.y= random.randrange(800-20)
    
    block_list.add(b_block)
    block_list.add(r_block)
    all_sprites_list.add(b_block)
    all_sprites_list.add(r_block)
    red_blocks.add(r_block)
    black_blocks.add(b_block)
    

score = 0
lives = 3
#*********main program loop**********
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    
    #Game logic here
    pos = pygame.mouse.get_pos()

    player.rect.x=pos[0]
    player.rect.y=pos[1]
    
    black_hit_list = pygame.sprite.spritecollide(player, black_blocks, True)
    red_hit_list = pygame.sprite.spritecollide(player, red_blocks, True)
    for block in red_hit_list:
        lives -= 1
        print(lives)
        if lives <=0:
            print("Game Over")
    for block in black_hit_list:
        score += 1
        print(score)

    
    #all drawing here
    screen.fill(WHITE)
    all_sprites_list.draw(screen)
   
    
    for x_offset in range(0, 800, 5):
        pygame.draw.line(screen,BLACK, [0+x_offset,0],[0+x_offset,800],1)
    for y_offset in range(0, 800, 5):
        pygame.draw.line(screen,BLACK, [0,0+y_offset],[800,0+y_offset],1)
    
    

    












    pygame.display.flip()

    clock.tick(60)

#after exiting main loop this closes the game
pygame.quit()