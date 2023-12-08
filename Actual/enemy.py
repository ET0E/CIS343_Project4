import os
import pygame as pg
import random
import math

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
        self.event = pg.USEREVENT + 2


    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def getXLocation(self):
        return self.rect.centery

    def getYLocation(self):
        return self.rect.centerx

    def update(self, delta, player):
        v = -1
        h = -1

        if player.getYLocation() >= self.getYLocation():
            v = -75
        if player.getYLocation() <= self.getYLocation():
            v = 75
        if player.getXLocation() >= self.getXLocation():
            h = 75
        if player.getXLocation() <= self.getXLocation():
            h = -75
        

        dx = player.rect.x - self.rect.x
        dy = player.rect.y - self.rect.y

        dist = math.hypot(dx, dy)


        if (self.rect.x + 50) >= BOUNDARYEAST:
            self.kill()
        
        if (self.rect.x - 50) <= BOUNDARYWEST:
            self.kill()

        if dist == 0:
            self.rect.y += 0
            self.rect.x += 0
        else:
            dx = dx/dist
            dy = dy/dist
            self.rect.y += v * delta * dy
            self.rect.x += h * delta * dx

        checks = pg.sprite.GroupSingle()
        checks.add(player)
        collision = pg.sprite.spritecollideany(self, checks)
        if collision:
            #collision.kill()
            #self.kill()
            pg.event.post(pg.event.Event(self.event))
            print("You've died")

            

