import os
import pygame as pg
import random
from player import Player

BOUNDARYNORTH = 50
BOUNDARYEAST = 1350
BOUNDARYSOUTH = 800
BOUNDARYWEST = 50

class Enemy(pg.sprite.Sprite):
    def __init__(self, startLocation):
        super(Enemy, self).__init__()
        self.image = pg.image.load(os.path.join('assets', 'skeleton.png')).convert_alpha()
        IMAGE_SIZE = (60,100)
        self.image = pg.transform.scale(self.image, IMAGE_SIZE)
        self.rect = self.image.get_rect()
        self.rect.centerx = startLocation[0]
        self.rect.centery = startLocation[1]
        self.startLocation = startLocation
        self.direction = 1

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def getXLocation(self):
        return self.rect.centery

    def getYLocation(self):
        return self.rect.centerx

    def update(self, delta, player):
        #self.rect.y += 10 * delta * self.direction
        #if self.rect.y > BOUNDARYSOUTH:
        #    self.rect.y += -1 * delta * player.getYLocation()
        
        #if self.rect.y > BOUNDARYEAST:
        #    self.rect.x += -1 * delta * player.getXLocation()
        v = -1
        h = -1

        if(player.getYLocation() >= self.getYLocation()):
            v = 0.1
        if(player.getYLocation() <= self.getYLocation()):
            v = -0.1
        if(player.getXLocation() >= self.getXLocation()):
            h = 0.1
        if(player.getXLocation() <= self.getXLocation()):
            h = -0.1
        
        
        self.rect.y += v * delta * player.getYLocation()
        self.rect.x += h * delta * player.getXLocation()




        #if(player.getXLocation() > self.getXLocation()):
        #    self.rect.x += 0.1 * delta * player.getXLocation()

        #if(player.getXLocation() < self.getXLocation()):
        #    self.rect.x += -0.1 * delta * player.getXLocation()

        #self.rect.y += 1 * delta * player.getYLocation()
        #self.rect.x += 1 * delta * player.getXLocation()

        def add(x, y):
            return x+y