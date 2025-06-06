import pygame
from spriteSheet import *
from config.config import *

class Ground(pygame.sprite.Sprite):
    def __init__(self, stage, x, y, GroundIdx):
        self.stage = stage
        self._layer = GROUND_LAYER
        self.groups = self.stage.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        self.width = TILE_SIZE
        self.height = TILE_SIZE

        self.image = self.stage.stageManager.background_spriteSheet.get_sprite(*GROUND_IMAGE_LIST[GroundIdx], self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y