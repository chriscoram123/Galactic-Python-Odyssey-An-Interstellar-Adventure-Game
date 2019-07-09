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

# Background variables
background_image = pygame.image.load("SPoW_82318_01 copy.png")

# Total enemy ships
# Ship one
EnemyShipOne = pygame.image.load("alien1.png").convert()
EnemyShipOne = pygame.transform.scale(EnemyShipOne, (80,80))
# Ship Two
EnemyShipTwo = pygame.image.load("alien1.png").convert()
EnemyShipTwo = pygame.transform.scale(EnemyShipTwo, (80,80))
# Ship Three
EnemyShipThree = pygame.image.load("alien1.png").convert()
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

screen.blit(background_image, (0,0))
