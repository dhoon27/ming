import pygame
import math
import random

from config.config import *

class Attack(pygame.sprite.Sprite):
    def __init__(self, StageManger, x, y):
        self.stage_manager = StageManger
        self._layer = PLAYER_LAYER
        self.groups = self.stage_manager.all_sprites, self.stage_manager.attacks
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x
        self.y = y
        self.width = TILE_SIZE
        self.height = TILE_SIZE

        self.animation_loop = 0
        self.image = self.stage_manager.attack_spriteSheet.get_sprite(0, 0, self.width, self.height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.down_animations = [self.stage_manager.attack_spriteSheet.get_sprite(*ANIMATE_ATTACK_DOWN_0, self.width, self.height),
            self.stage_manager.attack_spriteSheet.get_sprite(*ANIMATE_ATTACK_DOWN_1, self.width, self.height),
            self.stage_manager.attack_spriteSheet.get_sprite(*ANIMATE_ATTACK_DOWN_2, self.width, self.height),
            self.stage_manager.attack_spriteSheet.get_sprite(*ANIMATE_ATTACK_DOWN_3, self.width, self.height),
            self.stage_manager.attack_spriteSheet.get_sprite(*ANIMATE_ATTACK_DOWN_4, self.width, self.height)]

        self.up_animations = [self.stage_manager.attack_spriteSheet.get_sprite(*ANIMATE_ATTACK_UP_0, self.width, self.height),
            self.stage_manager.attack_spriteSheet.get_sprite(*ANIMATE_ATTACK_UP_1, self.width, self.height),
            self.stage_manager.attack_spriteSheet.get_sprite(*ANIMATE_ATTACK_UP_2, self.width, self.height),
            self.stage_manager.attack_spriteSheet.get_sprite(*ANIMATE_ATTACK_UP_3, self.width, self.height),
            self.stage_manager.attack_spriteSheet.get_sprite(*ANIMATE_ATTACK_UP_4, self.width, self.height)]

        self.left_animations = [self.stage_manager.attack_spriteSheet.get_sprite(*ANIMATE_ATTACK_LEFT_0, self.width, self.height),
            self.stage_manager.attack_spriteSheet.get_sprite(*ANIMATE_ATTACK_LEFT_1, self.width, self.height),
            self.stage_manager.attack_spriteSheet.get_sprite(*ANIMATE_ATTACK_LEFT_2, self.width, self.height),
            self.stage_manager.attack_spriteSheet.get_sprite(*ANIMATE_ATTACK_LEFT_3, self.width, self.height),
            self.stage_manager.attack_spriteSheet.get_sprite(*ANIMATE_ATTACK_LEFT_4, self.width, self.height)]

        self.right_animations = [self.stage_manager.attack_spriteSheet.get_sprite(*ANIMATE_ATTACK_RIGHT_0, self.width, self.height),
            self.stage_manager.attack_spriteSheet.get_sprite(*ANIMATE_ATTACK_RIGHT_1, self.width, self.height),
            self.stage_manager.attack_spriteSheet.get_sprite(*ANIMATE_ATTACK_RIGHT_2, self.width, self.height),
            self.stage_manager.attack_spriteSheet.get_sprite(*ANIMATE_ATTACK_RIGHT_3, self.width, self.height),
            self.stage_manager.attack_spriteSheet.get_sprite(*ANIMATE_ATTACK_RIGHT_4, self.width, self.height)]

    def update(self):
        self.animate()
        self.collide()

    def collide(self):
        hits = pygame.sprite.spritecollide(self, self.stage_manager.enemies, True)

    def animate(self):
        dircetion = self.stage_manager.player.facing

        if dircetion == 'up':
            self.image == self.up_animations[math.floor(self.animation_loop)]
            self.animation_loop += 0.5
            if self.animation_loop >= 5:
                self.kill()

        if dircetion == 'down':
            self.image == self.down_animations[math.floor(self.animation_loop)]
            self.animation_loop += 0.5
            if self.animation_loop >= 5:
                self.kill()

        if dircetion == 'left':
            self.image == self.left_animations[math.floor(self.animation_loop)]
            self.animation_loop += 0.5
            if self.animation_loop >= 5:
                self.kill()

        if dircetion == 'right':
            self.image == self.right_animations[math.floor(self.animation_loop)]
            self.animation_loop += 0.5
            if self.animation_loop >= 5:
                self.kill()
