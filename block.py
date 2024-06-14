import pygame

from config.config import *
from spriteSheet import *

class Block(pygame.sprite.Sprite):
    def __init__(self, StageManger, x, y, BlockIdx):
        self.stage_manager = StageManger
        self._layer = BLOCK_LAYER
        self.groups = self.stage_manager.all_sprites, self.stage_manager.blocks
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        self.width = TILE_SIZE
        self.height = TILE_SIZE

        self.image = self.stage_manager.background_spriteSheet.get_sprite(*BLOCK_IMAGE_LIST[BlockIdx], self.width, self.height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y