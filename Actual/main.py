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

    player = Player()

    enemies = pg.sprite.Group()
    projectiles = pg.sprite.Group()
    enemyspawners = pg.sprite.Group()

    enemyspawnerN = EnemySpawner(700, 50)
    enemyspawnerS = EnemySpawner(700, 750)
    enemyspawnerW = EnemySpawner(50, 400)
    enemyspawnerE = EnemySpawner(1350, 400)
    enemyspawners.add(enemyspawnerN)
    enemyspawners.add(enemyspawnerS)
    enemyspawners.add(enemyspawnerW)
    enemyspawners.add(enemyspawnerE)

    # delete this 
    ##for i in range(400, 1000, 100):
    #   for j in range(100, 600, 90):
    #        enemy = Enemy((i, j))
    #        enemies.add(enemy)

    # Start sound
    # pg.mixer.music.load('./assets/cpu-talk.mp3')
    # pg.mixer.music.play(-1)

    # Get font setup
    # pg.freetype.init()
    # font_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "./assets/", "PermanentMarker-Regular.ttf")
    # font_size = 64
    # font = pg.freetype.Font(font_path, font_size)
    # WHITE = (254, 254, 254)

    # Startup the main game loop
    running = True
    delta = 0
    shotDelta = 500
    fps = 60
    clock = pg.time.Clock()
    clock.tick(fps)
    score = 0
    angle = 0
    while running:
        player.rotating = True
        # First thing we need to clear the events.
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.USEREVENT + 1:
                score += 10
        # if event.type == pg.KEYDOWN:
        # if event.key == pg.K_e:
        # player.rotate(angle-1)
        # player.rotating = True
        # if event.key == pg.K_q:
        # player.rotate(angle+1)
        # player.rotating = True
        # elif event.type == pg.KEYUP:
        # if event.key == pg.K_e:
        # player.rotating = False
        # if event.key == pg.K_q:
        # player.rotating = False

        keys = pg.key.get_pressed()
        player.set_direction(player.get_direction())
        player.set_image(player.get_image())
        if keys[K_s]:
            player.down(delta)
            # if player.get_direction() == .5 and player.get_rotating() is True:
            # image = pg.transform.rotate(player.get_image(), -90)
            # player.set_image(image)
            # player.set_rotating(False)
            player.set_direction(-.5)
        if keys[K_w]:
            player.up(delta)
            player.set_direction(.5)
            # image = pg.transform.rotate(player.get_image(), -90)
            # player.set_image(image)

        """
        These two methods turn the character to the side the user is moving
        If the user changes directions too fast it can kind of mess with the directions
        """
        if keys[K_a]:
            player.left(delta)
            if player.get_direction() == 1 and player.get_rotating() is True:
                image = pg.transform.flip(player.get_image(), True, False)
                player.set_image(image)
                player.set_rotating(False)
            player.set_direction(0)

        if keys[K_d]:
            player.right(delta)
            if player.get_direction() == 0 and player.get_rotating() is True:
                image = pg.transform.flip(player.get_image(), True, False)
                player.set_image(image)
                player.set_rotating(False)
            player.set_direction(1)

            # image = pg.transform.flip(player.get_image(), False, True)
            # player.set_image(image)
        if keys[K_SPACE]:
            if shotDelta >= .25:
                projectile = Projectile(player.rect, enemies, player.get_direction())
                projectiles.add(projectile)
                shotDelta = 0
        # if len(enemies) == 0:
        #    print("You've cleared the galaxy of evil!")
        #    return
        if keys[K_ESCAPE]:
            running = False

        # Ok, events are handled, let's draw!
        screen.fill((0, 0, 0))
        enemyspawnerN.update(enemies)
        enemyspawnerS.update(enemies)
        enemyspawnerW.update(enemies)
        enemyspawnerE.update(enemies)
        player.update(delta)

        for enemy in enemies:
            enemy.update(delta, player)
        for projectile in projectiles:
            projectile.update(delta)

        player.draw(screen)
        enemies.draw(screen)
        enemyspawners.draw(screen)
        # would need to update projectlies.draw to shoot from the character with the changes in the comments
        projectiles.draw(screen)
        # font.render_to(screen, (10, 10), "Score: " + str(score), WHITE, None, size=64)

        # When drawing is done, flip the buffer.
        pg.display.flip()

        delta = clock.tick(fps) / 1000.0
        shotDelta += delta


# Startup the main method to get things going.
if __name__ == "__main__":
    main()
    pg.quit()
