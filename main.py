#   Import & Init
import pygame, sys, random
from pygame.locals import *

pygame.init()
pygame.display.set_caption("Tower Defense")
clock = pygame.time.Clock()

#   Image Initalization
map = pygame.image.load("Images\\map.png")
tower1 = pygame.image.load("Images\\T_Arrow01.png")
#   Initalize Variables
screen = pygame.display.set_mode((1000,600))
mayra = 1000
my_font = pygame.font.SysFont('Comic Sans MS', 30)
money_text = my_font.render(f'${mayra}', False, "red")
towers = []




#   Classes
class Tower():
    def __init__(self, image, type, pos):
        self.image = image
        self.type = type
        self.pos = pos

        
        self.range = 0
        self.damage = 0
        self.level = 1
    
    def identifier(self, type):
        if type == None:
            self.range = 10
            self.damage = 0

#   Functions
# Create towers and place them
def tower_placer(type):
    if type == "arrow":
        # place tower based on mouse click OR arrow movement
        towers.append(Tower(tower1, type, (500,300)))        

# Display towers (Always running)
def tower_display():
    for tower in towers:
        screen.blit(tower.image, tower.pos)

# Spawn enemies
def enemy_spawner():
    pass

# Upgrade Towers
def tower_upgrade():
    pass

# Level Starter and Tracker
def start_level():
    pass

# (Include in spawn enemies) AI for enemies
def enemy_mov():
    pass


screen.blit(map,(0,0))
screen.blit(tower1,(200,200))
#   Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                tower_placer("arrow")
    tower_display()
    screen.blit(money_text,(0,0))
    clock.tick(60)
    pygame.display.flip()