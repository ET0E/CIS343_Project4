#!/usr/bin/env python3

import pygame as pg
import os
from enemy import Enemy
from player import Player
from projectile import Projectile
from enemyspawner import EnemySpawner
from pygame.locals import *
import random
import math


def main():
    # Startup pygame
    pg.init()

    # Get a screen object
    screen = pg.display.set_mode([1400, 800])

    # initialize the player, enemies, projectiles, and enemy spawners
    enemies = pg.sprite.Group()
    projectiles = pg.sprite.Group()
    enemyspawners = pg.sprite.Group()
    player = Player(enemies)

    # Place all four enemy spawners in game, east, west, north and south
    # The west and east locations are at the far ends of the screen in the x direction and in the middle of the y direction
    # The north and south locations are at the far ends of the screen in the y direction and in the middle of the x direction
    enemyspawnerN = EnemySpawner(700, 50)
    enemyspawnerS = EnemySpawner(700, 750)
    enemyspawnerW = EnemySpawner(150, 400)
    enemyspawnerE = EnemySpawner(1325, 400)
    # adds the spawners into the world
    enemyspawners.add(enemyspawnerN)
    enemyspawners.add(enemyspawnerS)
    enemyspawners.add(enemyspawnerW)
    enemyspawners.add(enemyspawnerE)

    # delete this 
    ##for i in range(400, 1000, 100):
    #   for j in range(100, 600, 90):
    #        enemy = Enemy((i, j))
    #        enemies.add(enemy)
    
    
    # pg.mixer.music.load('./assets/cpu-talk.mp3')
    # pg.mixer.music.play(-1)

    # Get font setup
    pg.freetype.init()
    font_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "./assets/", "PixelifySans-Medium.ttf")
    font_size = 64
    font = pg.freetype.Font(font_path, font_size)
    WHITE = (254, 254, 254)

    # Startup the main game loop
    running = True
    # delta starts at 0 and updates in game loop
    delta = 0
    # initialized to 500 so the projectiles shoot
    shotDelta = 500
    # the frames per second the game runs at
    fps = 60
    # keeps track of the clock so things happen on time
    clock = pg.time.Clock()
    # Things happen at 60 frames per second
    clock.tick(fps)
    # score initialized to 0
    score = 0
    # main game loop
    while running:
        # rotating initialized to True so the player can rotate
        player.rotating = True
        # First thing we need to clear the events.
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.USEREVENT + 1:
                score += 1
            if event.type == pg.USEREVENT + 2:
                running = False
            if(score >= 50):
                print("You saved the town! Game Over!")
                running = False

        # how to check if keys get pressed
        keys = pg.key.get_pressed()
        # if the player is going in a direction keep them going in that direction until user switches direction
        player.set_direction(player.get_direction())
        # if the player has rotated the image stays as the rotated image
        player.set_image(player.get_image())
        # if the s key is pressed the direction gets set to coded number for down (-.5)
        if keys[K_s]:
            player.down(delta)
            player.set_direction(-.5)
        # if the w key is pressed the direction gets set to coded number for up (.5)
        if keys[K_w]:
            player.up(delta)
            player.set_direction(.5)

        """
        These two methods turn the character to the side the user is moving
        If the user changes directions too fast it can kind of mess with the directions
        """

        # if the a key is pressed the direction gets set to coded number for up (0)
        if keys[K_a]:
            player.left(delta)
            if player.get_direction() == 1 and player.get_rotating() is True:
                image = pg.transform.flip(player.get_image(), True, False)
                player.set_image(image)
                player.set_rotating(False)
            player.set_direction(0)

        # if the d key is pressed the direction gets set to coded number for up (0)
        if keys[K_d]:
            player.right(delta)
            if player.get_direction() == 0 and player.get_rotating() is True:
                image = pg.transform.flip(player.get_image(), True, False)
                player.set_image(image)
                player.set_rotating(False)
            player.set_direction(1)

        # if the space key is pressed a projectile gets fired
        if keys[K_SPACE]:
            # this is so the projectiles shoot one at a time instead of all at once
            if shotDelta >= .25:
                projectile = Projectile(player.rect, enemies, player.get_direction())
                projectiles.add(projectile)
                shotDelta = 0

        # if the escape key is pressed the
        if keys[K_ESCAPE]:
            running = False

        # Ok, events are handled, let's draw!
        screen.fill((0, 0, 0))
        # spawns the enemies out of the spawners
        enemyspawnerN.update(enemies)
        enemyspawnerS.update(enemies)
        enemyspawnerW.update(enemies)
        enemyspawnerE.update(enemies)

        # updates all the enemies in the game
        for enemy in enemies:
            enemy.update(delta, player)
        # updates all the projectiles in the game
        for projectile in projectiles:
            projectile.update(delta)

        # draws all the entities on the screen
        player.draw(screen)
        enemies.draw(screen)
        enemyspawners.draw(screen)
        projectiles.draw(screen)
        font.render_to(screen, (10, 10), "Score: " + str(score), WHITE, None, size=64)

        # When drawing is done, flip the buffer.
        pg.display.flip()

        # update the delta and shotDelta
        delta = clock.tick(fps) / 1000.0
        shotDelta += delta


# Startup the main method to get things going.
if __name__ == "__main__":
    main()
    pg.quit()
