"""
@author: Christopher S Coram
Python Space Game / Level One
6-30-2019 7:15PM
"""
# ------- IMPORTS -------
import pygame, sys
import pygame
import os
# ------- CLASS IMPORTS -------
from pygame.locals import *
from EnemyShipsLayer2 import *
from EnemyShipLayer3 import *
from Animations import *
# ------- CLASS IMPORTS / SCREENS -------
from MainMenu import *

pygame.init()
# Open window
size = [800, 600]
screen = pygame.display.set_mode(size)

# Model classes
EnemyL2 = LayerTwo()
EnemyL3 = LayerThree()
ExplosionAnimation = layerEffects()
# Screen classes
MainM = mainLoop()


# Manages how fast the screen updates
clock = pygame.time.Clock()

# Setup title to the window
pygame.display.set_caption('Python Spaceship Game')

# Setup background for video game
background_image = pygame.image.load("SPoW_82318_01 copy.png").convert()

# Setup player image in display
player = pygame.image.load("856963_spaceship-sprite-png copy.png")
player = pygame.transform.scale(player, (80,80))
# Player state values
lead_x = 350
lead_y = 500

# Setup alien ships
# Enemy ship one
background_alienShip = pygame.image.load("Spaceship-Transparent-PNG copy.png").convert_alpha()
background_alienShip = pygame.transform.scale(background_alienShip, (80, 80))
# Enemy ship two
background_alienShipTwo = pygame.image.load("Spaceship-Transparent-PNG copy.png").convert_alpha()
background_alienShipTwo = pygame.transform.scale(background_alienShipTwo, (80, 80))
# Enemy ship three
background_alienShipThree = pygame.image.load("Spaceship-Transparent-PNG copy.png").convert_alpha()
background_alienShipThree = pygame.transform.scale(background_alienShipThree, (80, 80))
# Enemy ship four
background_alienShipFour = pygame.image.load("Spaceship-Transparent-PNG copy.png").convert_alpha()
background_alienShipFour = pygame.transform.scale(background_alienShipFour, (80, 80))
# Enemy ship five
background_alienShipFive = pygame.image.load("Spaceship-Transparent-PNG copy.png").convert_alpha()
background_alienShipFive = pygame.transform.scale(background_alienShipFive, (80, 80))

# Enemy ship six
background_alienShipSix = pygame.image.load("Spaceship-Transparent-PNG copy.png").convert_alpha()
background_alienShipSix = pygame.transform.scale(background_alienShipSix, (80, 80))
# Enemy ship seven
background_alienShipSeven = pygame.image.load("Spaceship-Transparent-PNG copy.png").convert_alpha()
background_alienShipSeven = pygame.transform.scale(background_alienShipSeven, (80, 80))
# Enemy ship eight
background_alienShipEight = pygame.image.load("Spaceship-Transparent-PNG copy.png").convert_alpha()
background_alienShipEight = pygame.transform.scale(background_alienShipEight, (80, 80))
# Enemy ship nine
background_alienShipNine = pygame.image.load("Spaceship-Transparent-PNG copy.png").convert_alpha()
background_alienShipNine = pygame.transform.scale(background_alienShipNine, (80, 80))
# Enemy ship ten
background_alienShipTen = pygame.image.load("Spaceship-Transparent-PNG copy.png").convert_alpha()
background_alienShipTen = pygame.transform.scale(background_alienShipTen, (80, 80))


class imagesEnemyShips():
    def sectionOne(self):
        # Group 1
        # Spaceship one
        screen.blit(background_alienShip, (0,0)) # updates screen with enemy ship
        # Spaceship two
        screen.blit(background_alienShipTwo, (80,0)) # updates screen with enemy ship
        # Spaceship three
        screen.blit(background_alienShipThree, (160,0)) # updates screen with enemy ship
        # Spaceship four
        screen.blit(background_alienShipFour, (240,0)) # updates screen with enemy ship
        # Spaceship five
        screen.blit(background_alienShipFive, (320,0)) # updates screen with enemy ship

        # Group 2
        # Spaceship one
        screen.blit(background_alienShipSix, (400,0)) # updates screen with enemy ship
        # Spaceship two
        screen.blit(background_alienShipSeven, (480,0)) # updates screen with enemy ship
        # Spaceship three
        screen.blit(background_alienShipEight, (560,0)) # updates screen with enemy ship
        # Spaceship four
        screen.blit(background_alienShipNine, (640,0)) # updates screen with enemy ship
        # Spaceship five
        screen.blit(background_alienShipTen, (720,0)) # updates screen with enemy ship
""" Class Variable """
# Stores images class into object_x variable
object_x = imagesEnemyShips()


class playerObject():
    def playerLoad(self):
        screen.blit(player, (lead_x, lead_y, 10, 10)) # updates screen with player object
""" Class Variable """   
# Stores images class into object_x variable
objectP = playerObject()

        
key = pygame.key.get_pressed()
# -------- MAIN PROGRAM LOOP --------
while True: #main game loop
 screen.fill((255, 255, 255))
 for event in pygame.event.get():
    if event.type == QUIT:
        pygame.quit()
        sys.exit()
##############################
  # Player Movement
    if event.type == pygame.KEYDOWN: # updates screen with player position
      if event.key == pygame.K_LEFT:
        lead_x -= 10
      if event.key == pygame.K_RIGHT:
        lead_x += 10

 screen.blit(background_image, (0,0)) # updates screen with background
 EnemyL2.EnemyLayer() # updates scrren with second enemy layer
 EnemyL3.EnemyLayer() # updates scrren with third enemy layer
 objectP.playerLoad() # updates screen with player img
 object_x.sectionOne()
 pygame.display.flip()
 clock.tick(60)
