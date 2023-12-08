import os
import pygame as pg
import math

playerLocation = 0


class Player(pg.sprite.Sprite):
    """Class defining the player of the game

        The Player will be user controlled, every input the user makes will affect the behavior of this
        object.

        Attributes:
            image: the image will be a png and the png might need to be resized to fit the game window
            IMAGE_SIZE: the size of the image
            rect: it is the rectangle that the image is in, defines the collision box. (0,0) is not the
            center of the hitbox, it is the top left of the image.
            centerx: int that helps to define the center of the image, is the x component of the point
            centery: int that helps to define the center of the image, is the y component of the point
            rotating: boolean that defines wahether the player is rotating or not, aids in the rotating
            of the player image
            direction: int that defines which direction the player object is moving
            score: int that keeps a score of the player and how many enemies the player has eliminated
             enemies: defines the enemies that the player has to avoid and eliminate
        """

    def __init__(self, enemies):
        super(Player, self).__init__()
        self.image = pg.image.load(os.path.join('assets', 'Cowboy.png')).convert_alpha()
        IMAGE_SIZE = (100, 100)
        self.image = pg.transform.scale(self.image, IMAGE_SIZE)
        self.rect = self.image.get_rect(center=(self.image.get_rect().x, self.image.get_rect().y))
        self.rect.centerx = 700
        self.rect.centery = 350
        self.rotating = True
        self.direction = 1
        self.score = 0
        self.enemies = enemies

    def get_direction(self):
        """
        returns the direction of the player
        :return: the direction of the player
        """
        return self.direction

    def set_direction(self, direction):
        """
        sets the direction of the player
        :param direction: the direction the player is going to be set to
        :return: nothing
        """
        self.direction = direction

    def get_image(self):
        """
        gets the current player image
        :return: the current image of the player
        """
        return self.image

    def set_image(self, image):
        """
        sets the image of the player to parameter image
        :param image: the image the player image will be set to
        :return: nothing
        """
        self.image = image

    def get_rotating(self):
        """
        gets the current value of the rotating variable
        :return: the current value of the variable rotating
        """
        return self.rotating

    def set_rotating(self, rotating):
        """
        sets the value rotating to parameter rotating
        :param rotating: the value the player rotating variable will be set to
        :return: nothing
        """
        self.rotating = rotating

    def draw(self, screen):
        """
        draws the player image to the screen
        :param screen: the screen the player image will be drawn to
        :return: nothing
        """
        screen.blit(self.image, self.rect)


    def getXLocation(self):
        """
        gets the x location of the player
        :return: the center of the player rectangle (x)
        """
        return self.rect.centerx

    def getYLocation(self):
        """
        gets the y location of the player
        :return: the center of the player rectangle (y)
        """
        return self.rect.centery

    def up(self, delta):
        """
        moves the player image up
        :param delta: the amount the player rectangle will move
        :return: nothing
        """
        if self.rect.y > 0:
            self.rect.y -= 240 * delta

    def down(self, delta):
        """
        moves the player image down
        :param delta: the amount the player rectangle will move
        :return: nothing
        """
        if self.rect.y < 1080:
            self.rect.y += 240 * delta

    def left(self, delta):
        """
        moves the player image left
        :param delta: the amount the player rectangle will move
        :return: nothing
        """
        if self.rect.x > 0:
            self.rect.x -= 240 * delta

    def right(self, delta):
        """
        moves the player image right
        :param delta: the amount the player rectangle will move
        :return: nothing
        """
        if self.rect.x < 1920:
            self.rect.x += 240 * delta

    def update_score(self):
        """
        updates the score
        :return: nothing
        """
        self.score += 1
