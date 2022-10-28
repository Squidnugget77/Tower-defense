#   Import & Init
import pygame, sys, random
from pygame.locals import *

pygame.init()
pygame.display.set_caption("Tower Defense")
clock = pygame.time.Clock()

#   Image Initalization
map = pygame.image.load("Images\\map.png")
#   Initalize Variables
screen = pygame.display.set_mode((1000,600))
money = 1000
my_font = pygame.font.SysFont('Comic Sans MS', 30)
money_text = my_font.render(f'${money}', False, "red")




#   Classes
class Tower():
    def __init__(self, image, type):
        self.image = image
        self.type = type
        
        self.range = 0
        self.damage = 0
        self.level = 1
        self.pos = (500,300)
    
    def identifier(self, type):
        if type == None:
            self.range = 10
            self.damage = 0

#   Functions
# Count and Display All Towers
def tower_placer():
    pass

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
#   Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.blit(money_text,(0,0))
    pygame.display.flip()
    clock.tick(60)