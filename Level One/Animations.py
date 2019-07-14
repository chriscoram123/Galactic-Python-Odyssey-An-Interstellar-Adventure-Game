"""
@author: Christopher S Coram
Python Space Game / Level One / Animations / Module
7-7-2019 3:53PM
"""
# -------- IMPORTS --------
import pygame

# -------- PROGRAM VARIABLES --------
# Open window
size = [800, 600]
screen = pygame.display.set_mode(size)
# Explosion variables
imageExplode = pygame.image.load("explosion-png-5a37177e259e92.5165511015135599341541.jpg")
# Explosion coordinates relative to player position
posx = 350
posy = 500

# Class contains all functions regarding effects for enemy ships layer 1
class layerEffects():
    def __int__(self):
        print("Testing Animation Module")
    # Sound effects for object exploding / deleation from game
    def effect(self):
        pygame.mixer.music.load("")
        pygame.mixer.music.play(-1)
    # Visual effects for explosion
    def explosion(self):
        pygame.blit(imageExplode, posx, posy, 10, 10)
