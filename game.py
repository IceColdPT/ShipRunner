import pygame
import random

pygame.init()
pygame.mixer.init()

ASTEROID_IMAGES = [
    "art/ast1.png",
    "art/ast2.png",
    "art/ast3.png",
    "art/ast4.png"
]

#--------Colors-----------

WHITE = (255,255,255)
BLACK = (0,0,0)
RED =   (255,0,0)
BLUE =  (0,0,255)
GREEN = (0,255,0)
#---------------------------

WIDTH = 800
HEIGHT = 600
FPS = 30

last_y = 0
last_x = 0

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("This is cool")
clock = pygame.time.Clock()


all_sprites = pygame.sprite.Group()

#game loop

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("art/ship.png")
        #self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2
        self.rect.bottom = HEIGHT - 20
        self.xspeed = 0
    def update(self): 
        self.rect.x += self.xspeed
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > screen.get_width() - self.rect.width:
            self.rect.x = screen.get_width() - self.rect.width

class Monster(pygame.sprite.Sprite):
    def __init__(self,last_x,last_y):
        pygame.sprite.Sprite.__init__(self)
    
       # self.rad = rad
        self.image = pygame.image.load(random.choice(ASTEROID_IMAGES))
        
        self.rect = self.image.get_rect()

        self.rect.x = random.randrange(0, screen.get_width() - self.rect.width, 60)
        self.rect.y = random.randrange(-screen.get_height(),-60,60)
        
            
        self.speed = 3
    def update(self):
        #----respawn---#
        if self.rect.y > screen.get_height() +10:
            
            
            self.rect.x = random.randrange(0, screen.get_width() - self.rect.width, 60)
            self.rect.y = random.randrange(-screen.get_height(),-60,60)

            self.rect.h = random.randint(5,50)
        self.rect.y += self.speed
        
            
        


player = Player()
list_enemies = []
max_enemies = 10
for i in range(max_enemies):
    list_enemies.append(
        Monster(random.randint(0,screen.get_width() - 30), 50 )
    )

for i in range(max_enemies):
    list_enemies.append(
        Monster(random.randint(0,screen.get_width() - 30), 150 )
    )
all_sprites.add(player)

for enemy in list_enemies:
    all_sprites.add(enemy)

running = True

while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #Aceleraçao = a=dv/dt
        #vel = dx/dt
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
        
                player.xspeed = player.xspeed -3
            elif event.key == pygame.K_d:
                player.xspeed = player.xspeed + 3
        else:
            player.xspeed = 0
    all_sprites.update()


    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.flip() #this is the last thing

pygame.quit()