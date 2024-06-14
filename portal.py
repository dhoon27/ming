import pygame
import math
import random

from config.config import *

class Portal(pygame.sprite.Sprite):
    def __init__(self, GameManager, StageManger, x, y, direction):
        self.game_manager = GameManager
        self.stage_manager = StageManger
        self._layer = PORTAL_LAYER
        self.groups = self.stage_manager.all_sprites, self.stage_manager.portals
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.direction = direction
        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        self.width = TILE_SIZE
        self.height = TILE_SIZE

        self.image = pygame.transform.scale(self.stage_manager.portal_image, (self.width, self.height))
        self.image.set_colorkey(COLOR_BLACK)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def IsRide(self, player):
        dx = abs(self.rect.centerx - player.rect.centerx)
        dy = abs(self.rect.centery - player.rect.centery)
        if dx <= TILE_SIZE//2 and dy <= TILE_SIZE//2:
            if self.game_manager.stageIsCleared[self.game_manager.stageIdx]:
                pygame.time.wait(150)
                return True
        return False
