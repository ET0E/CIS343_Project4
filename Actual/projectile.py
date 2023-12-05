import os
import pygame as pg
from player import Player

class Projectile(pg.sprite.Sprite):
    def __init__(self, shipLocation, enemies, direction):
        super(Projectile, self).__init__()
        self.image = pg.image.load(os.path.join('assets', 'cannonball.png')).convert_alpha()
        IMAGE_SIZE = (40,40)
        self.image = pg.transform.scale(self.image, IMAGE_SIZE)
        self.rect = self.image.get_rect()
        self.rect.centerx = shipLocation.x + 100
        self.rect.centery = shipLocation.y + 37
        self.enemies = enemies
        self.event = pg.USEREVENT + 1
        self.direction = direction
        #self.fireSound = pg.mixer.Sound("./assets/fire.wav")
        #self.fireSound.play()
        #self.explosionSound = pg.mixer.Sound("./assets/explosion.wav")

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self, delta):
<<<<<<< HEAD
        self.rect.centerx += 750 * delta
        if self.rect.centerx > 1350:
=======
        if self.direction == 1:
            self.rect.centerx += 750 * delta
        if self.direction == .5:
            self.rect.centery -= 750 * delta
        if self.direction == -.5:
            self.rect.centery += 750 * delta
        if self.direction == 0:
            self.rect.centerx -= 750 * delta
        if self.rect.centerx > 1080:
>>>>>>> Multi-Directional
            self.kill()
        collision = pg.sprite.spritecollideany(self, self.enemies)
        if collision:
            collision.kill()
            pg.event.post(pg.event.Event(self.event))
            #self.explosionSound.play()
            self.kill()

    def set_direction(self, direction):
        self.direction = direction

    def get_direction(self):
        return self.direction
