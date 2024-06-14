import pygame

from config.config import *

class Image:
    def __init__(self):
        self.intro_background = pygame.image.load(INTRO_IMAGE)
        self.outro_background = pygame.image.load(OUTRO_IMAGE)