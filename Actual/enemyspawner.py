import os
import pygame as pg
import random


class EnemySpawner(pg.sprite.Sprite):
    def __init__(self, XLocation, YLocation):
        super (EnemySpawner, self).__init__()
        self.image = pg.image.load(os.path.join('assets', 'cave.png')).convert_alpha()
        IMAGE_SIZE = (125,125)
        self.image = pg.transform.scale(self.image, IMAGE_SIZE)
        self.rect = self.image.get_rect()
        self.rect.centerx = XLocation
        self.rect.centery = YLocation
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self, delta):
        pass

    

        
