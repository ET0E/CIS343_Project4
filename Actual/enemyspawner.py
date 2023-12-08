import os
import pygame as pg
import random
from enemy import Enemy



class EnemySpawner(pg.sprite.Sprite):
    """Class to define what and how the enemy spawns work

        The enemies spawn out of these spawners to attack and kill the player at a hard coded frequency

        Attributes:
            image: the image will be a png and the png might need to be resized to fit the game window
            IMAGE_SIZE: the size of the image
            rect: it is the rectangle that the image is in, defines the collision box. (0,0) is not the
            center of the hitbox, it is the top left of the image.
            centerx: helps to define the center of the image, is the x component of the point
            centery: helps to define the center of the image, is the y component of the point
        """
    def __init__(self, XLocation, YLocation):
        super (EnemySpawner, self).__init__()
        self.image = pg.image.load(os.path.join('assets', 'cave.png')).convert_alpha()
        IMAGE_SIZE = (125,125)
        self.image = pg.transform.scale(self.image, IMAGE_SIZE)
        self.rect = self.image.get_rect()
        self.rect.centerx = XLocation
        self.rect.centery = YLocation
    
    def draw(self, screen):
        """puts the image of the enemy spawner on the screen

        :param screen: the screen that the image draws too
        :return: nothing
        """
        screen.blit(self.image, self.rect)

    # add delta (1000 == 1 second)
    # randomly choose one of the spawner objects in here
    # randomly choose a number every update 0-1000 (which is every frame)

    def update(self, enemies):
        """
        controls the spawn rate of enemies from the spawner
        :param enemies: the object of enemies
        :return: nothing
        """
        if random.randint(0, 100) == 25:
            enemy = Enemy((random.randint((self.rect.centerx - 80), (self.rect.centerx + 80)), random.randint((self.rect.centery - 80), (self.rect.centery + 80))))
            enemies.add(enemy)

    
        

        
