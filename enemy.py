import pygame
import math
import random

from config.config import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self, StageManger, x, y):

        self.stage_manager = StageManger
        self._layer = ENEMY_LAYER
        self.groups = self.stage_manager.all_sprites, self.stage_manager.enemies
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        self.width = TILE_SIZE
        self.height = TILE_SIZE

        self.x_change = 0
        self.y_change = 0

        self.facing = random.choice(['left', 'right'])
        self.animation_loop = 1
        self.movement_loop =  0
        self.max_travel = random.randint(*ENEMY_MIN_MAX_TRAVEL)

        self.image = self.stage_manager.enemy_spriteSheet.get_sprite(3, 2, self.width, self.height)
        self.image.set_colorkey(COLOR_BLACK)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.down_animations = [self.stage_manager.enemy_spriteSheet.get_sprite(*CHARACTER_ENEMY_DOWN, self.width, self.height),
            self.stage_manager.enemy_spriteSheet.get_sprite(*CHARACTER_ENEMY_DOWN_1, self.width, self.height),
            self.stage_manager.enemy_spriteSheet.get_sprite(*CHARACTER_ENEMY_DOWN_2, self.width, self.height)]

        self.up_animations = [self.stage_manager.enemy_spriteSheet.get_sprite(*CHARACTER_ENEMY_UP, self.width, self.height),
            self.stage_manager.enemy_spriteSheet.get_sprite(*CHARACTER_ENEMY_UP_1, self.width, self.height),
            self.stage_manager.enemy_spriteSheet.get_sprite(*CHARACTER_ENEMY_UP_2, self.width, self.height)]

        self.left_animations = [self.stage_manager.enemy_spriteSheet.get_sprite(*CHARACTER_ENEMY_LEFT, self.width, self.height),
            self.stage_manager.enemy_spriteSheet.get_sprite(*CHARACTER_ENEMY_LEFT_1, self.width, self.height),
            self.stage_manager.enemy_spriteSheet.get_sprite(*CHARACTER_ENEMY_LEFT_2, self.width, self.height)]

        self.right_animations = [self.stage_manager.enemy_spriteSheet.get_sprite(*CHARACTER_ENEMY_RIGHT, self.width, self.height),
            self.stage_manager.enemy_spriteSheet.get_sprite(*CHARACTER_ENEMY_RIGHT_1, self.width, self.height),
            self.stage_manager.enemy_spriteSheet.get_sprite(*CHARACTER_ENEMY_RIGHT_2, self.width, self.height)]

    def update(self):
        self.movement()
        self.animate()

        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change = 0
        self.y_change = 0

    def movement(self):
        if self.facing == 'left':
            self.x_change -= ENEMY_SPEED
            self.movement_loop -= 1
            if self.movement_loop <= -self.max_travel:
                self.facing = 'right'

        if self.facing == 'right':
            self.x_change += ENEMY_SPEED
            self.movement_loop += 1
            if self.movement_loop >= self.max_travel:
                self.facing = 'left'

    def animate(self):
        if self.facing == "down":
            if self.y_change == 0:
                self.image = self.down_animations[0]
            else:
                self.image = self.down_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1

        if self.facing == "up":
            if self.y_change == 0:
                self.image = self.up_animations[0]
            else:
                self.image = self.up_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1

        if self.facing == "left":
            if self.x_change == 0:
                self.image = self.left_animations[0]
            else:
                self.image = self.left_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1

        if self.facing == "right":
            if self.x_change == 0:
                self.image = self.right_animations[0]
            else:
                self.image = self.right_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1