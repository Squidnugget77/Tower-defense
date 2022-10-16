#   Import & Init
import pygame, sys, random
from pygame.locals import *

pygame.init()
pygame.display.set_caption("Flappy")

#   Image Initalization

#   Initalize Variables
screen = pygame.display.set_mode((1000,600))

#   Classes

#   Functions

screen.fill((0,0,0))
#   Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()