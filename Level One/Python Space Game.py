"""
@author: Christopher S Coram
Python Space Game / Level One
6-30-2019 7:15PM
"""

#########################
# ------- IMPORTS -------
#########################
import pygame, sys
import pygame
import pygame.mixer
import os
import time
from pygame import mixer
from time import sleep
# ------- CLASS IMPORTS -------
from pygame.locals import *
from EnemyShipsLayer2 import *
from EnemyShipLayer3 import *
from Animations import *
# ------- CLASS IMPORTS / SCREENS -------
from MainMenu import *
# ------- CLASs IMPORTS SOUND / SCREENS -------
from Layer1SoundEffectsProjectiles import *
from Layer2SoundEffectsProjectiles import *
from Layer3SoundEffectsProjectiles import *
# ------ CLASS IMPORTS / PROJECTILES -------
from Projectiles import *
##################################################

#########################
# ------- VARIABLES -------
#########################
pygame.mixer.pre_init(44100,14,2,4096)
pygame.init()

# Open window
size = [800, 600]
screen = pygame.display.set_mode(size)
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))

# Ship model classes
EnemyL2 = LayerTwo()
EnemyL3 = LayerThree()
# Animation classes
ExplosionAnimation = layerEffects()
# Screen classes
MainM = mainLoop()
# Enemy sound effects classes
L1Sound = layerBotEffects()
L2Sound = layerTwoBotEffects()
L3Sound = layerThreeBotEffects()
# Projectile classes
playerProjectile = Bullet()
player_bullet_sound = bullet_sound()

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

# Text colors
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
Blue = (0,0,255)

# Projectile variables
bullets = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
##################################################

#########################
# ------- CLASSES -------
#########################
# Enemy ships class
class imagesEnemyShips():
    def __init__(self):
        print("Enemy layer load")
        
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
# Stores images class object_x variable
object_x = imagesEnemyShips()

# Player class
bullets = pygame.sprite.Group()
class playerObject():
    def __init__(self):
        print("Player image load")
        
    def playerLoad(self):
        screen.blit(player, (lead_x, lead_y, 10, 10)) # updates screen with player object

    # import class from projectile module
    def playerShoot(self):
        playerProjectile.shoot()
    
""" Class Variable """   
# Stores images class object_x variable
objectP = playerObject()


# Functions create pause button display
def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('Roboto-Black.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    game_loop()
        
def message():
    message_display("Pause")
    
def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    pygame.display.update()


# Plays main soundtrack
class main_soundtrack():
    # Updates console
    def __init__(self):
        print("Soundtrack have been loaded")

    # Main video game soundtrack 
    def soundtrackOne(self):
        pygame.mixer.music.load("mainSoundtrack.wav")
        pygame.mixer.music.set_volume(0.10)
        pygame.mixer.music.play(-1)
""" Class Variable """   
# Stores images class object_x variable
objectSound = main_soundtrack()
objectSound.soundtrackOne()

# Player movemnet soundtrack
movePSound = pygame.mixer.Sound("playerSound.wav")
pygame.mixer.music.set_volume(0.50)
pygame.mixer.music.play(0)
# Player bullet soundtrack
player_bullet_sound = pygame.mixer.Sound("PlayerBulletSound.wav")
pygame.mixer.music.set_volume(0.10)
pygame.mixer.music.play(0)
##################################################
    
#####################################
# -------- MAIN PROGRAM LOOP --------
#####################################
key = pygame.key.get_pressed()
running = True
while running: #main game loop
 screen.fill((255, 255, 255))
 for event in pygame.event.get():
    if event.type == QUIT:
        pygame.quit()
        sys.exit()
  # If else player movement
    if event.type == pygame.KEYDOWN: # updates screen with player position
      if event.key == pygame.K_LEFT:
        pygame.mixer.Sound.play(movePSound)
        lead_x -= 10
      if event.key == pygame.K_RIGHT:
        pygame.mixer.Sound.play(movePSound)
        lead_x += 10
  # elif statement for player projectiles
      elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_SPACE:
              pygame.mixer.Sound.play(player_bullet_sound)
              objectP.playerShoot()

          
  # If else pause button
      if event.key == pygame.K_DOWN:
        message()
##################################################

#####################################
# -------- UPDATES --------
#####################################
 all_sprites.draw(screen)
 screen.blit(background_image, (0,0)) # updates screen with background
 EnemyL2.EnemyLayer() # updates scrren with second enemy layer
 EnemyL3.EnemyLayer() # updates scrren with third enemy layer
 objectP.playerLoad() # updates screen with player img
 object_x.sectionOne()
 pygame.display.flip()
 clock.tick(60)
