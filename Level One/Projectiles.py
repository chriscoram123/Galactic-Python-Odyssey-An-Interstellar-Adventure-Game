"""
@author: Christopher S Coram
Python Space Game / Prpjectiles
7-11-2019 10:13PM
"""

# -------- IMPORTS --------
import pygame
import pygame, sys
import time
from time import sleep
from pygame import mixer
# -------- PROGRAM VARIABLES --------
pygame.init()
Blue = (0,0,255)
bullets = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
# Main player projectile
class Bullet(pygame.sprite.Sprite):
    """ Bullet: Set of code that creates bullet and which
    direction it travels per pixel."""

    def __init__(self, x=80, y=80):
        # Updates console
        print("Player bullet module load")
        # Calls parent class constructor
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([4, 10])
        self.image.fill(Blue)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        # Change in bullet position per pixel, y axis
        self.rect.y += self.speedy
        # kill if bullet moves to the top of screen
        if self.rect.bottom < 0:
            self.kill()

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)
        
# Main player projectile sound
class bullet_sound():
    def __init__(self):
        print("Player bullet soundtrack loaded")

"""
class collisionPlayer():
    # Class collisionPlayer: Set of code that states that player
    image will delete when in contact with enemy projectile.

    def __init__(self, arg):
        super(self).__init__()
        self.arg = arg
        # Updates console
        print("Testing Projectiles Module")

    def collision_check(self):
"""
