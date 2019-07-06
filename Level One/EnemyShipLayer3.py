"""
@author: Christopher S Coram
Python Space Game / Level One / Enemy Ships Layer 3 / Module
7-5-2019 11:43PM
"""
# -------- IMPORTS --------
import pygame

# -------- PROGRAM VARIABLES --------
pygame.init()
# Open window
size = [800, 600]
screen = pygame.display.set_mode(size)

# Total enemy ships
# Ship one
EnemyShipOne = pygame.image.load("caa0a03c64dbc3d2fa10e7056afb006f.png").convert()
EnemyShipOne = pygame.transform.scale(EnemyShipOne, (80,80))
# Ship Two
EnemyShipTwo = pygame.image.load("caa0a03c64dbc3d2fa10e7056afb006f.png").convert()
EnemyShipTwo = pygame.transform.scale(EnemyShipTwo, (80,80))
# Ship Three
EnemyShipThree = pygame.image.load("caa0a03c64dbc3d2fa10e7056afb006f.png").convert()
EnemyShipThree = pygame.transform.scale(EnemyShipThree, (80,80))
###################

# -------- CLASSES -------- 
class LayerThree():
    def __init__(self):
        print("Testing when called upon")
        
    def EnemyLayer(self):
        # Spaceship One
        screen.blit(EnemyShipOne, (280,100)) # updates screen with enemy ship
        # Spaceship Two
        screen.blit(EnemyShipTwo, (360,100)) # updates screen with enemy ship
        # Spaceship Three
        screen.blit(EnemyShipThree, (440,100)) # updates screen with enemy ship
