#   Import & Init
import pygame as alyssa
import sys, random
from pygame.locals import *

alyssa.init()
alyssa.display.set_caption("Tower Defense")
clock = alyssa.time.Clock()

#   Image Initalization
tessa = alyssa.image.load("Images\\map.png")
tower1 = alyssa.image.load("Images\\T_Arrow01.png")
#   Initalize Variables
screen = alyssa.display.set_mode((1000,600))
mayra = 1000
my_font = alyssa.font.SysFont('Comic Sans MS', 30)
money_text = my_font.render(f'${mayra}', False, "red")
towers = []
phantom_towers = []
key_press = 0




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

class Enemy():
    pass

#   Functions
# Create towers and place them
def tower_placer(type):
    global key_press, phantom_towers, mayra, money_text
    x, y = alyssa.mouse.get_pos()
    if type == "magic":
        if key_press == 0:
            phantom_towers.append(Tower(tower1, type, (x,y)))
            # place tower based on mouse click OR arrow movement
        elif key_press == 1 and mayra >= 200:
            towers.append(Tower(tower1, type, (x,y)))
            key_press =- 1
            phantom_towers = []
            mayra -= 200
            money_text = my_font.render(f'${mayra}', False, "red")
        else:
            print(f'You need $200 for that purchase! ${200-mayra} more!')


# Display towers (Always running)
def tower_display():
    x, y = alyssa.mouse.get_pos()
    for tower in towers:
        screen.blit(tower.image, tower.pos)
    for tower in phantom_towers:
        screen.blit(tower.image,(x,y))
    

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

#   Game Loop
while True:
    for event in alyssa.event.get():
        if event.type == alyssa.QUIT:
            alyssa.quit()
            sys.exit
        if event.type == alyssa.KEYDOWN:
            if event.key == alyssa.K_1:
                tower_placer("magic")
                key_press += 1
            if event.key == alyssa.K_ESCAPE:
                key_press = 0
                phantom_towers = []

    screen.blit(tessa,(0,0))
    tower_display()
    screen.blit(money_text,(0,0))
    alyssa.display.flip()
    clock.tick(60)