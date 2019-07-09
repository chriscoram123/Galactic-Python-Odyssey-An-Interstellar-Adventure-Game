"""
@author: Christopher S Coram
Python Space Game / Level One
7-7-2019 3:07PM
"""
# -------- IMPORTS --------
import pygame
import pygame, sys
# -------- PROGRAM VARIABLES --------
pygame.init()

# Pygame window setup
# Open window
size = [800, 600]
screen = pygame.display.set_mode(size)
# Manages how fast the screen updates
clock = pygame.time.Clock()
# Setup background for video game
background_image = pygame.image.load("SPoW_82318_01 copy.png").convert()
# Setup title to the window
pygame.display.set_caption("Main Menu")

# Main menu text setup
# Define RGBA values
white = (255, 255, 255)
blue = (0, 0, 128)
# X and Y variables
X = 400
Y = 400
# Display surface object
display_surface = pygame.display.set_mode((X, Y))
# Font object
font = pygame.font.Font("Roboto-Black.ttf", 32)
# Surface object
text = font.render("Annihilation", True, white, blue)
# Rectangular objext for text surface object
textRect = text.get_rect()
# Center of rectangular object
textRect.center = (X // 2, Y // 2)

class mainLoop():
    def loop(self):
# -------- MAIN PROGRAM LOOP --------
        while True:
         display_surface.blit(text, textRect)
         for event in pygame.event.get():
          if event.type == pygame.QUIT:
           pygame.quit()
           sys.exit()


screen.blit(background_image, (0,0)) # updates screen with background
pygame.display.update()
