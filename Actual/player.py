import os
import pygame as pg

class Player(pg.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pg.image.load(os.path.join('assets', 'Cowboy.png')).convert_alpha()
        IMAGE_SIZE = (125,125)
        self.image = pg.transform.scale(self.image, IMAGE_SIZE)
        self.rect = self.image.get_rect()
        self.rect.centerx = 100
        self.rect.centery = 350

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self, delta):
        pass

    def up(self, delta):
        if self.rect.y > 0:
            self.rect.y -= 240 * delta

    def down(self, delta):
        if self.rect.y < 1000:
            self.rect.y += 240 * delta

    def left(self, delta):
        if self.rect.x > 0:
            self.rect.x -= 240 * delta

    def right(self, delta):
        if self.rect.x < 1024:
            self.rect.x += 240 * delta
