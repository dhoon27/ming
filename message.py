import pygame
import math
import random

from config.config import *
from button import *

class Message:
    def __init__(self, x, y, width, height, fontsize, speaker, message, prev_text="Prev", next_text="Next"):
        self.font = pygame.font.SysFont('malgungothic', fontsize)
        self.speaker = speaker
        self.message = message

        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.bg = COLOR_WHITE
        self.fg = COLOR_BLACK

        self.image = pygame.Surface((self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.prev_button = Button(self.rect.x + 1, self.rect.y + self.height - 1, 80, 30, COLOR_WHITE, COLOR_BLACK, prev_text, 24)
        self.next_button = Button(self.rect.x + self.width - 80, self.rect.y + self.height - 1, 80, 30, COLOR_WHITE, COLOR_BLACK, next_text, 24)

    def draw(self, screen):
        self.image.fill(self.bg)
        speaker_text = self.font.render(self.speaker, True, self.fg)
        message_text = self.font.render(self.message, True, self.fg)

        self.image.blit(speaker_text, (10, 10))
        self.image.blit(message_text, (10, 50))
        screen.blit(self.image, self.rect.topleft)

        self.prev_button.draw(screen)
        self.next_button.draw(screen)

    def is_prev_pressed(self, pos, pressed):
        return self.prev_button.is_pressed(pos, pressed)

    def is_next_pressed(self, pos, pressed):
        return self.next_button.is_pressed(pos, pressed)
