import pygame

from config.config import *
from spriteSheet import *

class Wall(pygame.sprite.Sprite):
    def __init__(self, stage, x, y, WallIdx):
        self.stage = stage
        self._layer = WALL_LAYER
        self.groups = self.stage.all_sprites, self.stage.walls
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        self.width = TILE_SIZE
        self.height = TILE_SIZE

        self.image = self.stage.stageManager.background_spriteSheet.get_sprite(*WALL_IMAGE_LIST[WallIdx], self.width, self.height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y