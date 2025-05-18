import pygame
import math
import random

from config.config import *
from attack import *

class Player(pygame.sprite.Sprite):
    def __init__(self, stageManager):
        self.stageManager = stageManager
        self.stage = None
        self._layer = PLAYER_LAYER
        self.groups = None
        self.width = TILE_SIZE
        self.height = TILE_SIZE
        self.image = self.stageManager.character_spriteSheet.get_sprite(*CHARACTER_PLAYER, self.width, self.height)

        self.down_animations = [self.stageManager.character_spriteSheet.get_sprite(*CHARACTER_PLAYER_DOWN, self.width, self.height),
            self.stageManager.character_spriteSheet.get_sprite(*CHARACTER_PLAYER_DOWN_1, self.width, self.height),
            self.stageManager.character_spriteSheet.get_sprite(*CHARACTER_PLAYER_DOWN_2, self.width, self.height)]

        self.up_animations = [self.stageManager.character_spriteSheet.get_sprite(*CHARACTER_PLAYER_UP, self.width, self.height),
            self.stageManager.character_spriteSheet.get_sprite(*CHARACTER_PLAYER_UP_1, self.width, self.height),
            self.stageManager.character_spriteSheet.get_sprite(*CHARACTER_PLAYER_UP_2, self.width, self.height)]

        self.left_animations = [self.stageManager.character_spriteSheet.get_sprite(*CHARACTER_PLAYER_LEFT, self.width, self.height),
            self.stageManager.character_spriteSheet.get_sprite(*CHARACTER_PLAYER_LEFT_1, self.width, self.height),
            self.stageManager.character_spriteSheet.get_sprite(*CHARACTER_PLAYER_LEFT_2, self.width, self.height)]

        self.right_animations = [self.stageManager.character_spriteSheet.get_sprite(*CHARACTER_PLAYER_RIGHT, self.width, self.height),
            self.stageManager.character_spriteSheet.get_sprite(*CHARACTER_PLAYER_RIGHT_1, self.width, self.height),
            self.stageManager.character_spriteSheet.get_sprite(*CHARACTER_PLAYER_RIGHT_2, self.width, self.height)]

        self.x = 0 * TILE_SIZE
        self.y = 0 * TILE_SIZE

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.x_change = 0
        self.y_change = 0
        self.facing = 'down'
        self.animation_loop = 1

    def setStage(self, x, y, stage):
        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        self.rect.x = self.x
        self.rect.y = self.y
        self.stage = stage
        self.groups = self.stage.all_sprites, self.stage.player
        pygame.sprite.Sprite.__init__(self, self.groups)

    def update(self):
        self.movement()
        self.animate()
        self.collide_enemy()

        self.rect.x += self.x_change
        self.collide_walls('x')
        self.rect.y += self.y_change
        self.collide_walls('y')

        self.x_change = 0
        self.y_change = 0

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            for sprite in self.stage.all_sprites:
                sprite.rect.x += PLAYER_SPEED
            self.x_change -= PLAYER_SPEED
            self.facing = 'left'
        if keys[pygame.K_RIGHT]:
            for sprite in self.stage.all_sprites:
                sprite.rect.x -= PLAYER_SPEED
            self.x_change += PLAYER_SPEED
            self.facing = 'right'
        if keys[pygame.K_UP]:
            for sprite in self.stage.all_sprites:
                sprite.rect.y += PLAYER_SPEED
            self.y_change -= PLAYER_SPEED
            self.facing = 'up'
        if keys[pygame.K_DOWN]:
            for sprite in self.stage.all_sprites:
                sprite.rect.y -= PLAYER_SPEED
            self.y_change += PLAYER_SPEED
            self.facing = 'down'
        if keys[pygame.K_SPACE]:
            for portal in self.stageManager.cur_stage.portals:
                if portal.IsRide(self) == True:
                    self.stageManager.stageIdx = self.stageManager.stageIdx + portal.direction
                    self.stage.running = False
                    print("portal next stage : ", self.stageManager.stageIdx)
        if keys[pygame.K_a]:
            if self.facing == 'up':
                Attack(self, self.stage, self.rect.x, self.rect.y - TILE_SIZE)
            if self.facing == 'down':
                Attack(self, self.stage, self.rect.x, self.rect.y + TILE_SIZE)
            if self.facing == 'left':
                Attack(self, self.stage, self.rect.x - TILE_SIZE, self.rect.y)
            if self.facing == 'right':
                Attack(self, self.stage, self.rect.x + TILE_SIZE, self.rect.y)
        if keys[pygame.K_m]:
            for npc in self.stage.npcs:
                npc.dialog(self)

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

    def collide_walls(self, direction):
        if direction == "x":
            hits = pygame.sprite.spritecollide(self, self.stage.walls, False)
            hits += pygame.sprite.spritecollide(self, self.stage.npcs, False)
            if hits:
                if self.x_change > 0:
                    self.rect.x = hits[0].rect.left - self.rect.width
                    for sprite in self.stage.all_sprites:
                        sprite.rect.x += PLAYER_SPEED
                if self.x_change < 0:
                    self.rect.x = hits[0].rect.right
                    for sprite in self.stage.all_sprites:
                        sprite.rect.x -= PLAYER_SPEED
            # ToDo: Check for screen boundaries

        if direction == "y":
            hits = pygame.sprite.spritecollide(self, self.stage.walls, False)
            hits += pygame.sprite.spritecollide(self, self.stage.npcs, False)
            if hits:
                if self.y_change > 0:
                    self.rect.y = hits[0].rect.top - self.rect.height
                    for sprite in self.stage.all_sprites:
                        sprite.rect.y += PLAYER_SPEED
                if self.y_change < 0:
                    self.rect.y = hits[0].rect.bottom
                    for sprite in self.stage.all_sprites:
                        sprite.rect.y -= PLAYER_SPEED
            # ToDo: Check for screen boundaries

    def collide_enemy(self):
        hits = pygame.sprite.spritecollide(self, self.stage.enemies, False)
        if hits:
            self.kill()
            self.stage.running = False
            self.stage.gameOver = True
            print("running = False")
