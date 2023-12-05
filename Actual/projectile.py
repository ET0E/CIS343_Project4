import os
import pygame as pg

class Projectile(pg.sprite.Sprite):
    def __init__(self, shipLocation, enemies):
        super(Projectile, self).__init__()
        self.image = pg.image.load(os.path.join('assets', 'cannonball.png')).convert_alpha()
        IMAGE_SIZE = (40,40)
        self.image = pg.transform.scale(self.image, IMAGE_SIZE)
        self.rect = self.image.get_rect()
        self.rect.centerx = shipLocation.x + 100
        self.rect.centery = shipLocation.y + 37
        self.enemies = enemies
        self.event = pg.USEREVENT + 1
        #self.fireSound = pg.mixer.Sound("./assets/fire.wav")
        #self.fireSound.play()
        #self.explosionSound = pg.mixer.Sound("./assets/explosion.wav")

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self, delta):
        self.rect.centerx += 750 * delta
        if self.rect.centerx > 1350:
            self.kill()
        collision = pg.sprite.spritecollideany(self, self.enemies)
        if collision:
            collision.kill()
            pg.event.post(pg.event.Event(self.event))
            #self.explosionSound.play()
            self.kill()
