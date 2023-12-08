import os
import pygame as pg
from player import Player

class Projectile(pg.sprite.Sprite):
    """Class defining projectiles in game

    The projectile will be fired from the player in directions, up, down,
    left, right. Upon hitting an enemy the enemy will be killed.

    Attributes:
        image: the image will be a png and the png might need to be resized to fit the game window
        IMAGE_SIZE: the size of the image
        rect: it is the rectangle that the image is in, defines the collision box. (0,0) is not the
        center of the hitbox, it is the top left of the image.
        centerx: helps to define the center of the image, is the x component of the point
        centery: helps to define the center of the image, is the y component of the point
        enemies: defines the enemies that the projectile will kill
        event: defines what event in pygame is happening, assigning USEREVENT 1 to a projectile
        based event
        direction: helps to define which direction the projectiles will be fired in
    """
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

    def draw(self, screen):
        """
        draws the image of the projectile to the screen
        :param screen: the screen that the image will display on
        :return: nothing
        """
        screen.blit(self.image, self.rect)

    def update(self, delta):
        """
        updates the projectile to fire in what direction the player is facing, and
        if the projectile hits an enemy the projectile goes away
        :param delta: the speed the projectile fires in
        :return: noting
        """
        # player facing right, fire right
        if self.direction == 1:
            self.rect.centerx += 750 * delta
        # player facing up, fire up
        if self.direction == .5:
            self.rect.centery -= 750 * delta
        # player facing down, fire down
        if self.direction == -.5:
            self.rect.centery += 750 * delta
        # player facing left, fire left
        if self.direction == 0:
            self.rect.centerx -= 750 * delta
        # if the projectile goes out of the boundry in X direction destroy the projectile
        if self.rect.centerx > 1350 or self.rect.centerx < 0:
            self.kill()
        # if the projectile goes out of the boundry in Y direction destroy the projectile
        if self.rect.centery > 800 or self.rect.centery < 0:
            self.kill()

        # if the projectile collides with an enemy kill the projectile
        collision = pg.sprite.spritecollideany(self, self.enemies)
        if collision:
            collision.kill()
            pg.event.post(pg.event.Event(self.event))
            self.kill()

    def set_direction(self, direction):
        """
        sets the direction the projectile will fire in
        :param direction: the direction the projectile will fire in
        :return: nothing
        """
        self.direction = direction

    def get_direction(self):
        """
        gets the direction the projectile will fire in
        :return: the direction the projectile is currently firing in
        """
        return self.direction
