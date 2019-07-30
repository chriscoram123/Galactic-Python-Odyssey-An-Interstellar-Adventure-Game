"""
@author: Christopher S Coram
Python Space Game / Level One
6-30-2019 7:15PM
"""

#######################
#####-- IMPORTS --#####
#######################

import pygame, sys, random, math
import pygame
import pygame.mixer
import os
import time
from pygame import mixer
from time import sleep
from time import time
# ------- CLASS IMPORTS -------
from pygame.locals import *
from EnemyShipsLayer2 import *
# ------ CLASS IMPORTS / PROJECTILES -------
from Projectiles import *
##################################################



#########################
#####-- VARIABLES --#####
#########################

pygame.mixer.pre_init(44100,14,2,4096)
pygame.init()
FPS = 120

# Open window
size = [800, 600]
screen = pygame.display.set_mode(size)
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))


# Ship model classes
EnemyL2 = LayerTwo()
# Projectile classes
playerProjectile = Bullet()


# Manages how fast the screen updates
clock = pygame.time.Clock()

# Setup title to the window
pygame.display.set_caption('Python Spaceship Game')

# Setup background for video game
background_image = pygame.image.load("SPoW_82318_01.png").convert()

# Setup player image in display
player = pygame.image.load("856963_spaceship-sprite-png copy 2.png")
player = pygame.transform.scale(player, (80,80))
# Player state values
lead_x = 350
lead_y = 500

# Setup alien ships
# Enemy ship one
background_alienShip = pygame.image.load("Spaceship-Transparent-PNG copy 2.png").convert_alpha()
background_alienShip = pygame.transform.scale(background_alienShip, (80, 80))
# Enemy ship two
background_alienShipTwo = pygame.image.load("Spaceship-Transparent-PNG copy 2.png").convert_alpha()
background_alienShipTwo = pygame.transform.scale(background_alienShipTwo, (80, 80))
# Enemy ship three
background_alienShipThree = pygame.image.load("Spaceship-Transparent-PNG copy 2.png").convert_alpha()
background_alienShipThree = pygame.transform.scale(background_alienShipThree, (80, 80))
# Enemy ship four
background_alienShipFour = pygame.image.load("Spaceship-Transparent-PNG copy 2.png").convert_alpha()
background_alienShipFour = pygame.transform.scale(background_alienShipFour, (80, 80))
# Enemy ship five
background_alienShipFive = pygame.image.load("Spaceship-Transparent-PNG copy 2.png").convert_alpha()
background_alienShipFive = pygame.transform.scale(background_alienShipFive, (80, 80))

# Enemy ship six
background_alienShipSix = pygame.image.load("Spaceship-Transparent-PNG copy 2.png").convert_alpha()
background_alienShipSix = pygame.transform.scale(background_alienShipSix, (80, 80))
# Enemy ship seven
background_alienShipSeven = pygame.image.load("Spaceship-Transparent-PNG copy 2.png").convert_alpha()
background_alienShipSeven = pygame.transform.scale(background_alienShipSeven, (80, 80))
# Enemy ship eight
background_alienShipEight = pygame.image.load("Spaceship-Transparent-PNG copy 2.png").convert_alpha()
background_alienShipEight = pygame.transform.scale(background_alienShipEight, (80, 80))
# Enemy ship nine
background_alienShipNine = pygame.image.load("Spaceship-Transparent-PNG copy 2.png").convert_alpha()
background_alienShipNine = pygame.transform.scale(background_alienShipNine, (80, 80))
# Enemy ship ten
background_alienShipTen = pygame.image.load("Spaceship-Transparent-PNG copy 2.png").convert_alpha()
background_alienShipTen = pygame.transform.scale(background_alienShipTen, (80, 80))

# Alien ship list....
alien_ship_obj = [background_alienShip, background_alienShipTwo, background_alienShipThree, background_alienShipFour,
                  background_alienShipFive, background_alienShipSix, background_alienShipSeven, background_alienShipEight,
                  background_alienShipNine]
#....

# Text colors
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
Blue = (0,0,255)

# Projectile variables
bullets = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
##################################################



#######################
#####-- CLASSES --#####
#######################

""" Layer 1 Enemy Ships: Set of code displays a row of image imported
enemy ships at the top of the display.
"""
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
""" ....... """
# Enemy ship blit origin positions variables
ship_one_position = screen.blit(background_alienShip, (0,0))
ship_two_position = screen.blit(background_alienShipTwo, (80,0))
ship_three_position = screen.blit(background_alienShipThree, (160,0))
ship_four_position = screen.blit(background_alienShipFour, (240,0))
ship_five_position = screen.blit(background_alienShipFive, (320,0))
ship_six_position = screen.blit(background_alienShipSix, (400,0))
ship_seven_position = screen.blit(background_alienShipSeven, (480,0))
ship_eight_position = screen.blit(background_alienShipEight, (560,0))
ship_nine_position = screen.blit(background_alienShipNine, (640,0))
ship_ten_position = screen.blit(background_alienShipTen, (720,0))


""" Player Projectile: Set of code that draws player projectile as well as
identifying it's x and y coordinates.
"""
# Player class variables / functions....
bullets = pygame.sprite.Group()
screen.fill(white)
x_cord = 380 # x coordinates for bullet obj position
y_cord = 500 # y coordinates for bullet obj position
# Layer One....
# Draw bullets by seprate ships
""" Layer 1 / Ship 1 Projectile """
b1_x_cord = 30 # Layer 1 x coordinates
b1_y_cord = 83 # Layer 1 y coordinates

""" Layer 1 / Ship 2 Projectile """
b2_x_cord = 110 # Layer 1 x coordinates
b2_y_cord = 83 # Layer 1 y coordinates

""" Layer 1 / Ship 3 Projectile """
b3_x_cord = 190 # Layer 1 x coordinates
b3_y_cord = 83 # Layer 1 y coordinates

""" Layer 1 / Ship 4 Projectile """
b4_x_cord = 270 # Layer 1 x coordinates
b4_y_cord = 83 # Layer 1 y coordinates

""" Layer 1 / Ship 5 Projectile """
b5_x_cord = 350 # Layer 1 x coordinates
b5_y_cord = 83 # Layer 1 y coordinates

""" Layer 1 / Ship 6 Projectile """
b6_x_cord = 430 # Layer 1 x coordinates
b6_y_cord = 83 # Layer 1 y coordinates

""" Layer 1 / Ship 7 Projectile """
b7_x_cord = 505 # Layer 1 x coordinates
b7_y_cord = 83 # Layer 1 y coordinates

""" Layer 1 / Ship 8 Projectile """
b8_x_cord = 590 # Layer 1 x coordinates
b8_y_cord = 83 # Layer 1 y coordinates

""" Layer 1 / Ship 9 Projectile """
b9_x_cord = 668 # Layer 1 x coordinates
b9_y_cord = 83 # Layer 1 y coordinates

""" Layer 1 / Ship 10 Projectile """
b10_x_cord = 750 # Layer 1 x coordinates
b10_y_cord = 83 # Layer 1 y coordinates
#....

# Bullet variables to assist with bullet wraps
# Bullet L1 - 1
bullet_img_x1 = b1_x_cord
bullet_img_y1 = b1_y_cord
bullet_width1 = 20
bullet_height1 = 10
origin_position_1 = ship_one_position
# Bullet L1 - 2
bullet_img_x2 = b2_x_cord
bullet_img_y2 = b2_y_cord
bullet_width2 = 20
bullet_height2 = 10
origin_position_2 = ship_two_position
# Bullet L1 - 3
bullet_img_x3 = b3_x_cord
bullet_img_y3 = b3_y_cord
bullet_width3 = 20
bullet_height3 = 10
origin_position_3 = ship_three_position
# Bullet L1 - 4
bullet_img_x4 = b4_x_cord
bullet_img_y4 = b4_y_cord
bullet_width4 = 20
bullet_height4 = 10
origin_position_4 = ship_four_position
# Bullet L1 - 5
bullet_img_x5 = b5_x_cord
bullet_img_y5 = b5_y_cord
bullet_width5 = 20
bullet_height5 = 10
origin_position_5 = ship_five_position
# Bullet L1 - 6
bullet_img_x6 = b6_x_cord
bullet_img_y6 = b6_y_cord
bullet_width6 = 20
bullet_height6 = 10
origin_position_6 = ship_six_position
# Bullet L1 - 7
bullet_img_x7 = b7_x_cord
bullet_img_y7 = b7_y_cord
bullet_width7 = 20
bullet_height7 = 10
origin_position_7 = ship_seven_position
# Bullet L1 - 8
bullet_img_x8 = b8_x_cord
bullet_img_y8 = b8_y_cord
bullet_width8 = 20
bullet_height8 = 10
origin_position_8 = ship_eight_position
# Bullet L1 - 9
bullet_img_x9 = b9_x_cord
bullet_img_y9 = b9_y_cord
bullet_width9 = 20
bullet_height9 = 10
origin_position_9 = ship_nine_position
# Bullet L1 - 10
bullet_img_x10 = b10_x_cord
bullet_img_y10 = b10_y_cord
bullet_width10 = 20
bullet_height10 = 10
origin_position_10 = ship_ten_position

# Enemy odd bullet coordinates
enemy_bullet_rect = pygame.Rect(bullet_img_x1, bullet_img_y1, bullet_width1, bullet_height1)
enemy_bullet_rect3 = pygame.Rect(bullet_img_x3, bullet_img_y3, bullet_width3, bullet_height3)
enemy_bullet_rect5 = pygame.Rect(bullet_img_x5, bullet_img_y5, bullet_width5, bullet_height5)
enemy_bullet_rect7 = pygame.Rect(bullet_img_x7, bullet_img_y7, bullet_width7, bullet_height7)
enemy_bullet_rect9 = pygame.Rect(bullet_img_x9, bullet_img_y9, bullet_width9, bullet_height9)

# Enemy even bullet coordinates
enemy_bullet_rect2 = pygame.Rect(bullet_img_x2, bullet_img_y2, bullet_width2, bullet_height2)
enemy_bullet_rect4 = pygame.Rect(bullet_img_x4, bullet_img_y4, bullet_width4, bullet_height4)
enemy_bullet_rect6 = pygame.Rect(bullet_img_x6, bullet_img_y6, bullet_width6, bullet_height6)
enemy_bullet_rect8 = pygame.Rect(bullet_img_x8, bullet_img_y8, bullet_width8, bullet_height8)
enemy_bullet_rect10 = pygame.Rect(bullet_img_x10, bullet_img_y10, bullet_width10, bullet_height10)

def drawn_load():
   # Enemy Bullets....
   pygame.draw.rect(screen, red, enemy_bullet_rect) # updates screen with drawn object
   pygame.draw.rect(screen, red, enemy_bullet_rect2) # updates screen with drawn object
   pygame.draw.rect(screen, red, enemy_bullet_rect3) # updates screen with drawn object
   pygame.draw.rect(screen, red, enemy_bullet_rect4) # updates screen with drawn object
   pygame.draw.rect(screen, red, enemy_bullet_rect5) # updates screen with drawn object
   pygame.draw.rect(screen, red, enemy_bullet_rect6) # updates screen with drawn object
   pygame.draw.rect(screen, red, enemy_bullet_rect7) # updates screen with drawn object
   pygame.draw.rect(screen, red, enemy_bullet_rect8) # updates screen with drawn object
   pygame.draw.rect(screen, red, enemy_bullet_rect9) # updates screen with drawn object
   pygame.draw.rect(screen, red, enemy_bullet_rect10) # updates screen with drawn object
   pygame.display.update()
   #....
""" ....... """


""" Collision System: Set of code that identifies two objects. If those two objects should
come in contact with one another, than both objects will kill(). But bullet object will respawn
after x amount of seconds.
"""
alien_sprite = alien_ship_obj[0]
bullet = drawn_load()
# Collision function
def collide(self, sprite):
    pygame.sprite.collide_rect()
   # collide_rect(alien_sprite, bullet) == bool
#....


""" Player Class: Contains all actions that will update player img
to pygame screen.
"""
player_img_x = lead_x
player_img_y = lead_y
player_width = 5
player_height = 5
# Player class
class playerObject():
    def __init__(self):
        print("Player image load")

    def playerLoad(self):
        pygame.draw.rect(screen, Blue, (x_cord, y_cord, 20, 10)) # updates screen with drawn object
        screen.blit(player, (player_img_x, player_img_y, player_width, player_height)) # updates screen with player object

    # import class from projectile module
    def playerShoot(self):
        if bullet.is_collided_with(alien_sprite):
            print("Collision")
            bullet.kill()
            alien_sprite.kill()
""" Class Variable """
# Stores images class object_x variable
objectP = playerObject()
""" ...... """



""" Pause Button: Set of code that craete a pause menu when
player keydowns Z.
"""
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
""" ....... """



""" Soundtrack: Set of code creates functions for background music and sound
effects when player starts game and carries out certain actions.
"""
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
""" ....... """

# Player movemnet soundtrack...
movePSound = pygame.mixer.Sound("playerSound.wav")
pygame.mixer.music.set_volume(0.50)
pygame.mixer.music.play(0)
#...

# Player bullet soundtrack...
player_bullet_sound = pygame.mixer.Sound("PlayerBulletSound.wav")
pygame.mixer.music.set_volume(0.10)
pygame.mixer.music.play(0)
#...



# Boundries class that exits game when player interacts with Boundries
class boundries_gameover():
    def __init__(self):
        print("boundries class active")

    def screen_boundries(self):
        global lead_x
        global lead_y
        if lead_x > 800:
            pygame.quit()
            sys.exit()
""" Class Variable """
# Stores images class object_x variable
object_boundries = boundries_gameover()
#....



# Contains Layer 2 bullet movments
def enemy_BL2_movement():
    # global variables
    # L2B variables....
    global EL2B_ship1
    global EL2B_ship1
    global EL2B_ship1
    global EL2B_ship1
    global EL2B_ship1
    global EL2B_ship1

    # L1 odd variables....
    global enemy_bullet_rect
    global enemy_bullet_rect3
    global enemy_bullet_rect5
    global enemy_bullet_rect7
    global enemy_bullet_rect9

    # L1 even variables....
    global enemy_bullet_rect2
    global enemy_bullet_rect4
    global enemy_bullet_rect6
    global enemy_bullet_rect8
    global enemy_bullet_rect10
    
    # Event type for time loop that will chgange L2B positions
    EL2B_ship1.centery += 10
    EL2B_ship2.centery += 10
    EL2B_ship3.centery += 10
    EL2B_ship4.centery += 10
    EL2B_ship5.centery += 10
    EL2B_ship6.centery += 10

    # Odd enemy bullets change position 
    enemy_bullet_rect.centery += 20
    enemy_bullet_rect3.centery += 20
    enemy_bullet_rect5.centery += 20
    enemy_bullet_rect7.centery += 20
    enemy_bullet_rect9.centery += 20

    # Even enemy bullets change position
    enemy_bullet_rect2.centery += 30
    enemy_bullet_rect4.centery += 30
    enemy_bullet_rect6.centery += 30
    enemy_bullet_rect8.centery += 30
    enemy_bullet_rect10.centery += 30
     

#################################
######- MAIN PROGRAM LOOP -######
#################################
            
key = pygame.key.get_pressed()
running = True
while running: #main game loop
 screen.fill((255, 255, 255))
 for event in pygame.event.get():
    if event.type == QUIT:
        pygame.quit()
        sys.exit()

  # If / else player movement
    if event.type == pygame.KEYDOWN: # updates screen with player position
      if event.key == pygame.K_LEFT:
        player_img_x -= 10 # Player object x coordinates
        x_cord -= 10 # Player bullet y coordinates

      if event.key == pygame.K_RIGHT:
        player_img_x += 10 # Player object x coordinates
        x_cord += 10 # Player bullet y coordinates

      if event.key == pygame.K_UP:
          player_img_y -= 7 # Player object x coordinates
          y_cord -= 7 # Player bullet y coordinates


  # elif statement for player projectiles
      elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_SPACE:
              pygame.mixer.Sound.play(player_bullet_sound)
              y_cord -= 60
          if event.key == pygame.K_DOWN:
              player_img_y += 10 # Player object x coordinates
              y_cord += 10 # Player bullet y coordinates

    # Control so player never leaves screen area
      object_boundries.screen_boundries()
##################################################




#######################
#####-- UPDATES --#####
#######################
  
 all_sprites.draw(screen)
 screen.blit(background_image, (0,0)) # updates screen with background
 EnemyL2.EnemyLayer() # updates scrren with second enemy layer
 EnemyL2.bullet_load() # updates scrren with second enemy layer
 objectP.playerLoad() # updates screen with player img
 object_x.sectionOne() # updates screen with enemy ship image layer
 drawn_load()
 enemy_BL2_movement() # updates screen bullet layer y axis movement
 clock.tick(FPS)
 pygame.display.update()

