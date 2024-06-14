import pygame

from config.config import *

class Button:
    def __init__(self, x, y, width, height, fg, bg, content, fontsize):
        self.font = pygame.font.SysFont('malgungothic', fontsize)
        self.content = content

        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.fg = fg
        self.bg = bg

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.bg)
        self.rect = self.image.get_rect()

        self.rect.x = self.x
        self.rect.y = self.y

        self.text = self.font.render(self.content, True, self.fg)
        self.text_rect = self.text.get_rect(center=(self.width/2 , self.height/2))
        self.image.blit(self.text, self.text_rect)

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)

    def is_pressed(self, pos, pressed):
        if self.rect.collidepoint(pos) and pressed[0]:
            pygame.time.wait(150)
            return True
        return False