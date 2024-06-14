import pygame
import math
import random

from config.config import *
from attack import *

class Player(pygame.sprite.Sprite):
    def __init__(self, StageManger, x, y):
        self.stage_manager = StageManger
        self._layer = PLAYER_LAYER
        self.groups = self.stage_manager.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        # self.isClearedStage = -1

        self.moveCntEnable = False
        self.moveCnt = 0

        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        self.width = TILE_SIZE
        self.height = TILE_SIZE

        self.x_change = 0
        self.y_change = 0
        self.facing = 'down'
        self.animation_loop = 1

        self.image = self.stage_manager.character_spriteSheet.get_sprite(*CHARACTER_PLAYER, self.width, self.height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.down_animations = [self.stage_manager.character_spriteSheet.get_sprite(*CHARACTER_PLAYER_DOWN, self.width, self.height),
            self.stage_manager.character_spriteSheet.get_sprite(*CHARACTER_PLAYER_DOWN_1, self.width, self.height),
            self.stage_manager.character_spriteSheet.get_sprite(*CHARACTER_PLAYER_DOWN_2, self.width, self.height)]

        self.up_animations = [self.stage_manager.character_spriteSheet.get_sprite(*CHARACTER_PLAYER_UP, self.width, self.height),
            self.stage_manager.character_spriteSheet.get_sprite(*CHARACTER_PLAYER_UP_1, self.width, self.height),
            self.stage_manager.character_spriteSheet.get_sprite(*CHARACTER_PLAYER_UP_2, self.width, self.height)]

        self.left_animations = [self.stage_manager.character_spriteSheet.get_sprite(*CHARACTER_PLAYER_LEFT, self.width, self.height),
            self.stage_manager.character_spriteSheet.get_sprite(*CHARACTER_PLAYER_LEFT_1, self.width, self.height),
            self.stage_manager.character_spriteSheet.get_sprite(*CHARACTER_PLAYER_LEFT_2, self.width, self.height)]

        self.right_animations = [self.stage_manager.character_spriteSheet.get_sprite(*CHARACTER_PLAYER_RIGHT, self.width, self.height),
            self.stage_manager.character_spriteSheet.get_sprite(*CHARACTER_PLAYER_RIGHT_1, self.width, self.height),
            self.stage_manager.character_spriteSheet.get_sprite(*CHARACTER_PLAYER_RIGHT_2, self.width, self.height)]

    def update(self):
        self.movement()
        self.animate()
        self.collide_enemy()

        self.rect.x += self.x_change
        self.collide_blocks('x')
        self.rect.y += self.y_change
        self.collide_blocks('y')

        self.x_change = 0
        self.y_change = 0

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            for sprite in self.stage_manager.all_sprites:
                sprite.rect.x += PLAYER_SPEED
            self.x_change -= PLAYER_SPEED
            self.facing = 'left'
            if self.moveCntEnable:
                self.moveCnt += 1
        if keys[pygame.K_RIGHT]:
            for sprite in self.stage_manager.all_sprites:
                sprite.rect.x -= PLAYER_SPEED
            self.x_change += PLAYER_SPEED
            self.facing = 'right'
            if self.moveCntEnable:
                self.moveCnt += 1
        if keys[pygame.K_UP]:
            for sprite in self.stage_manager.all_sprites:
                sprite.rect.y += PLAYER_SPEED
            self.y_change -= PLAYER_SPEED
            self.facing = 'up'
            if self.moveCntEnable:
                self.moveCnt += 1
        if keys[pygame.K_DOWN]:
            for sprite in self.stage_manager.all_sprites:
                sprite.rect.y -= PLAYER_SPEED
            self.y_change += PLAYER_SPEED
            self.facing = 'down'
            if self.moveCntEnable:
                self.moveCnt += 1
        if keys[pygame.K_SPACE]:
            for portal in self.stage_manager.portals:
                if portal.IsRide(self):
                    self.stage_manager.game_manager.stageIdx += portal.direction
                    self.stage_manager.running = False
                    print("IsRide True")
        if keys[pygame.K_a]:
            if self.facing == 'up':
                Attack(self.stage_manager, self.rect.x, self.rect.y - TILE_SIZE)
            if self.facing == 'down':
                Attack(self.stage_manager, self.rect.x, self.rect.y + TILE_SIZE)
            if self.facing == 'left':
                Attack(self.stage_manager, self.rect.x - TILE_SIZE, self.rect.y)
            if self.facing == 'right':
                Attack(self.stage_manager, self.rect.x + TILE_SIZE, self.rect.y)
        if keys[pygame.K_m]:
            for npc in self.stage_manager.npcs:
                npc.dialog(self)

    def collide_blocks(self, direction):
        if direction == "x":
            hits = pygame.sprite.spritecollide(self, self.stage_manager.blocks, False)
            hits += pygame.sprite.spritecollide(self, self.stage_manager.npcs, False)
            if hits:
                if self.x_change > 0:
                    self.rect.x = hits[0].rect.left - self.rect.width
                    for sprite in self.stage_manager.all_sprites:
                        sprite.rect.x += PLAYER_SPEED
                if self.x_change < 0:
                    self.rect.x = hits[0].rect.right
                    for sprite in self.stage_manager.all_sprites:
                        sprite.rect.x -= PLAYER_SPEED
            # ToDo: Check for screen boundaries

        if direction == "y":
            hits = pygame.sprite.spritecollide(self, self.stage_manager.blocks, False)
            hits += pygame.sprite.spritecollide(self, self.stage_manager.npcs, False)
            if hits:
                if self.y_change > 0:
                    self.rect.y = hits[0].rect.top - self.rect.height
                    for sprite in self.stage_manager.all_sprites:
                        sprite.rect.y += PLAYER_SPEED
                if self.y_change < 0:
                    self.rect.y = hits[0].rect.bottom
                    for sprite in self.stage_manager.all_sprites:
                        sprite.rect.y -= PLAYER_SPEED
            # ToDo: Check for screen boundaries

    def collide_enemy(self):
        hits = pygame.sprite.spritecollide(self, self.stage_manager.enemies, False)
        if hits:
            self.kill()
            self.stage_manager.running = False
            self.stage_manager.IsPlay = False
            self.stage_manager.IsOutro = True

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