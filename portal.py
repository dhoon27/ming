import pygame
import math
import random

from config.config import *

class Portal(pygame.sprite.Sprite):
    def __init__(self, stage, x, y, direction):
        self.stage = stage
        self._layer = PORTAL_LAYER
        self.groups = self.stage.all_sprites, self.stage.portals
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.direction = direction
        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        self.width = TILE_SIZE
        self.height = TILE_SIZE

        self.image = pygame.transform.scale(self.stage.stageManager.portal_image, (self.width, self.height))
        self.image.set_colorkey(COLOR_BLACK)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def IsRide(self, player):
        dx = abs(self.rect.centerx - player.rect.centerx)
        dy = abs(self.rect.centery - player.rect.centery)
        if dx <= TILE_SIZE//2 and dy <= TILE_SIZE//2:
            if self.stage.stageIsCleared == True:
                pygame.time.wait(200)
                return True
        return False
