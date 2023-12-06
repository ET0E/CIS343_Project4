import os
import pygame as pg
import math

playerLocation = 0


class Player(pg.sprite.Sprite):

    def __init__(self):
        super(Player, self).__init__()
        self.image = pg.image.load(os.path.join('assets', 'Cowboy.png')).convert_alpha()
        IMAGE_SIZE = (125, 125)
        self.image = pg.transform.scale(self.image, IMAGE_SIZE)
        self.rect = self.image.get_rect(center=(self.image.get_rect().x, self.image.get_rect().y))
        self.rect.centerx = 700
        self.rect.centery = 350
        self.angle = 0
        self.rotating = True
        self.direction = 1

    def get_direction(self):
        return self.direction

    def set_direction(self, direction):
        self.direction = direction

    def get_image(self):
        return self.image

    def set_image(self, image):
        self.image = image

    def get_rotating(self):
        return self.rotating

    def set_rotating(self, rotating):
        self.rotating = rotating

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self, delta):
        pass

    def getXLocation(self):
        return self.rect.centery

    def getYLocation(self):
        return self.rect.centerx

    def up(self, delta):
        if self.rect.y > 0:
            self.rect.y -= 240 * delta

    def down(self, delta):
        if self.rect.y < 1080:
            self.rect.y += 240 * delta

    def left(self, delta):
        if self.rect.x > 0:
            self.rect.x -= 240 * delta

    def right(self, delta):
        if self.rect.x < 1920:
            self.rect.x += 240 * delta

    def rotate(self, angle_change):
        self.angle += angle_change
        image = pg.transform.rotate(self.image, self.angle)
        image.rect = image.get_rect(center=self.rect.center)

    # def rotate(self, image, angle):
    # image = pg.transform.rotate(image, angle)
