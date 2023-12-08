import os
import pygame as pg
import random
import math

BOUNDARYNORTH = 50
BOUNDARYEAST = 1350
BOUNDARYSOUTH = 800
BOUNDARYWEST = 50

class Enemy(pg.sprite.Sprite):
    """Class defining the enemies of the game

            The enemies act on their own, AI that has a set behavior to move toward and kill the player

            Attributes:
                image: the image will be a png and the png might need to be resized to fit the game window
                IMAGE_SIZE: the size of the image
                rect: it is the rectangle that the image is in, defines the collision box. (0,0) is not the
                center of the hitbox, it is the top left of the image.
                centerx: int that helps to define the center of the image, is the x component of the point
                centery: int that helps to define the center of the image, is the y component of the point
                direction: defines the direction the enemy AI is moving in
                event: defines what event in pygame is happening, assigning USEREVENT 2 to an enemy
                based event
            """
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
        """
        draws the enemy image to the screen
        :param screen: the screen the enemy image will be drawn
        :return: nothing
        """
        screen.blit(self.image, self.rect)

    def getXLocation(self):
        """
        gets the x location of the enemy
        :return: the center of the enemy rectangle (x)
        """
        return self.rect.centery

    def getYLocation(self):
        """
        gets the x location of the enemy
        :return: the center of the enemy rectangle (y)
        """
        return self.rect.centerx

    def update(self, delta, player):
        """
        updates the enemy location to go toward the player location
        :param delta: the speed of the enemies
        :param player: the player the enemies will move toward
        :return: nothing
        """

        # initialized values, used in calculations later in function
        v = -1
        h = -1

        # updating those iniitialize values depending on location relative to player current position
        if player.getYLocation() >= self.getYLocation():
            v = -75
        if player.getYLocation() <= self.getYLocation():
            v = 75
        if player.getXLocation() >= self.getXLocation():
            h = 75
        if player.getXLocation() <= self.getXLocation():
            h = -75
        
        # calculating the distance from the player on x and y axis
        dx = player.rect.x - self.rect.x
        dy = player.rect.y - self.rect.y

        # getting the hypotenuse of the triangle
        dist = math.hypot(dx, dy)

        # if the enemy goes outside the boundry of the screen it dies
        if (self.rect.x + 50) >= BOUNDARYEAST:
            self.kill()
        if (self.rect.x - 50) <= BOUNDARYWEST:
            self.kill()

        # if the enemies are on the player it doesn't go anywhere
        if dist == 0:
            self.rect.y += 0
            self.rect.x += 0
        # moves the enemy in the direction of the player
        else:
            dx = dx/dist
            dy = dy/dist
            self.rect.y += v * delta * dy
            self.rect.x += h * delta * dx

        # gets the player and checks if the enemy has collided with the player hitbox
        checks = pg.sprite.GroupSingle()
        checks.add(player)
        collision = pg.sprite.spritecollideany(self, checks)
        # If the enemy has collided with the player then the player dies.
        if collision:
            #collision.kill()
            #self.kill()
            pg.event.post(pg.event.Event(self.event))
            print("You've died")

            

