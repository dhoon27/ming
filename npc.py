import pygame
import math
import random

from config.config import *
from button import *
from message import *

class Npc(pygame.sprite.Sprite):
    def __init__(self, stage, x, y, idx):
        self.stage = stage
        self._layer = NPC_LAYER
        self.groups = self.stage.all_sprites, self.stage.npcs
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.isCleared = False
        self.idx = idx
        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        self.width = TILE_SIZE
        self.height = TILE_SIZE

        self.x_change = 0
        self.y_change = 0

        self.facing = 'down'

        self.image = pygame.image.load(NPC_IMAGE[self.idx]).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.image.set_colorkey(COLOR_BLACK)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def dialog(self, player):
        dx = abs(self.rect.centerx - player.rect.centerx)
        dy = abs(self.rect.centery - player.rect.centery)
        if dx <= TILE_SIZE and dy <= TILE_SIZE:
            print("npc idx = %d" % self.idx)
            messageRest = NPC_MESSAGE_COUNT[self.idx]
            messageCnt = 0

            while messageCnt < messageRest:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.stage.running = False
                        self.stage.playing = False
                        return

                speaker, message = NPC_MESSAGE_LIST[self.idx][messageCnt]
                messagebox = Message(*MESSAGE_POS, *MESSAGE_SIZE, MESSAGE_FONT_SIZE, speaker, message)

                mouse_pos = pygame.mouse.get_pos()
                mouse_pressed = pygame.mouse.get_pressed()

                messagebox.draw(self.stage.gameManager.screen)
                pygame.display.update()

                if messageCnt > 0 and messagebox.is_prev_pressed(mouse_pos, mouse_pressed):
                    messageCnt -= 1

                if messagebox.is_next_pressed(mouse_pos, mouse_pressed):
                    messageCnt += 1

            if messageCnt == messageRest:
                self.isCleared = True