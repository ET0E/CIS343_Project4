import os
import pygame as pg

class Enemy(pg.sprite.Sprite):
    def __init__(self, startLocation):
        super(Enemy, self).__init__()
        self.image = pg.image.load(os.path.join('assets', 'skeleton.png')).convert_alpha()
        IMAGE_SIZE = (80,100)
        self.image = pg.transform.scale(self.image, IMAGE_SIZE)
        self.rect = self.image.get_rect()
        self.rect.centerx = startLocation[0]
        self.rect.centery = startLocation[1]
        self.startLocation = startLocation
        self.direction = 1

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self, delta):
        self.rect.y += 100 * delta * self.direction
        if self.rect.y > self.startLocation[1] + 100 or self.rect.y < self.startLocation[1] - 100:
            self.direction *= -1
