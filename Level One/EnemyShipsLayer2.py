"""
@author: Christopher S Coram
Python Space Game / Level One / Enemy Ships Layer 2 / Module
7-5-2019 2:03PM
"""
# -------- IMPORTS --------
import pygame

# -------- PROGRAM VARIABLES --------
pygame.init()
# Open window
size = [800, 600]
screen = pygame.display.set_mode(size)

# Background variable
background_image = pygame.image.load("SPoW_82318_01.png")

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
# Ship Four
EnemyShipFour = pygame.image.load("alien1.png").convert()
EnemyShipFour = pygame.transform.scale(EnemyShipFour, (80,80))
# Ship Five
EnemyShipFive = pygame.image.load("alien1.png").convert()
EnemyShipFive = pygame.transform.scale(EnemyShipFive, (80,80))
# Ship Six
EnemyShipSix = pygame.image.load("alien1.png").convert()
EnemyShipSix = pygame.transform.scale(EnemyShipSix, (80,80))
###################

# -------- CLASSES --------
class LayerTwo():
    def __init__(self):
        print("Testing when called upon")

    def EnemyLayer(self):
        # Spaceship One
        screen.blit(EnemyShipOne, (40,100)) # updates screen with enemy ship
        # Spaceship Two
        screen.blit(EnemyShipTwo, (120,100)) # updates screen with enemy ship
        # Spaceship Three
        screen.blit(EnemyShipThree, (200,100)) # updates screen with enemy ship
        # Spaceship Four
        screen.blit(EnemyShipFour, (520,100)) # updates screen with enemy ship
        # Spaceship Five
        screen.blit(EnemyShipFive, (600,100)) # updates screen with enemy ship
        # Spaceship Six
        screen.blit(EnemyShipSix, (680,100)) # updates screen with enemy ship


screen.blit(background_image, (0,0))
