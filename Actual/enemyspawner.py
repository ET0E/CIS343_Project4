import os
import pygame as pg
import random
from enemy import Enemy



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

    # add delta (1000 == 1 second)
    # randomly choose one of the spawner objects in here
    # randomly choose a number every update 0-1000 (which is every frame)

    def update(self, enemies):
        if random.randint(0, 50) == 25:
            enemy = Enemy((self.rect.centerx, self.rect.centery))
            enemies.add(enemy)

    
        

        
