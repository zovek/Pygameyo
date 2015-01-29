#importing pygame
import pygame, random, math, sys
from pygame.locals import *
pygame.init()

#defining color variables
BLACK = (  0,  0,  0)
WHITE = (255,255,255)
RED   = (255,  0,  0)
GREEN = (  0,255,  0)
BLUE  = (  0,  0,255)

#window settings
xres = 1280
yres = 720
screen = pygame.display.set_mode((xres, yres), DOUBLEBUF)
pygame.display.set_caption("Test Pygame Game")
pygame.mouse.set_visible(False)

#setting fps variable
fpsClock = pygame.time.Clock()

#creating a variable that starts main loop.
done = False

#global variables
x_offset = 0
y_offset = 0
score = 0
lives = 3

#***classes under***
class Block(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

    def update(self):
        x = random.randint(0,xres- 20)
        self.rect.y += random.randint(1, 5)
        self.rect.x += random.randint(1, 5)
        self.rect.y -= random.randint(1, 5)
        self.rect.x -= random.randint(1, 5)
        if self.rect.x >= xres-20:
            self.rect.x = xres-20
        if self.rect.x <= 0:
            self.rect.x = 0
        if self.rect.y >= yres-20:
            self.rect.y = yres-20
        if self.rect.y <= 0:
            self.rect.y = 0
class Player(Block):
    x_speed = 0
    y_speed = 0
    
    def update_m(self):
        pos = pygame.mouse.get_pos()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
    def update_k(self):  
        self.rect.x += self.x_speed 
        self.rect.y += self.y_speed
        


#defining groups
block_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()
red_blocks = pygame.sprite.Group()
black_blocks = pygame.sprite.Group()
#creating player sprite
player = Player(GREEN, 10,10)
all_sprites_list.add(player)
#creating sprites
for i in range(20):
    b_block = Block(BLACK, 20,20)
    r_block = Block(RED, 20,20)


    b_block.rect.x= random.randrange(xres-20)
    b_block.rect.y= random.randrange(yres-20)

    r_block.rect.x= random.randrange(xres-20)
    r_block.rect.y= random.randrange(yres-20)
    
    block_list.add(b_block)
    block_list.add(r_block)
    all_sprites_list.add(b_block)
    all_sprites_list.add(r_block)
    red_blocks.add(r_block)
    black_blocks.add(b_block)
    


#*********main program loop**********
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.x_speed = -3
            if event.key == pygame.K_RIGHT:
                player.x_speed = 3
            if event.key == pygame.K_UP:
                player.y_speed = -3
            if event.key == pygame.K_DOWN:
                player.y_speed = 3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.x_speed = 0
            if event.key == pygame.K_RIGHT:
                player.x_speed = 0
            if event.key == pygame.K_UP:
                player.y_speed = 0
            if event.key == pygame.K_DOWN:
                player.y_speed = 0 
        
            
    #Game logic here
    player.update_k()
    
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
   
    for x_offset in range(0, xres, 5):
        pygame.draw.line(screen,BLACK, [0+x_offset,0],[0+x_offset,yres],1)
    for y_offset in range(0, yres, 5):
        pygame.draw.line(screen,BLACK, [0,0+y_offset],[xres,0+y_offset],1)

    for block in block_list:
        block.update()

    

    












    pygame.display.flip()

    fpsClock.tick(60)

#after exiting main loop this closes the game
pygame.quit()
