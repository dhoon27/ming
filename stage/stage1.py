import pygame
from config.config import *
from spriteSheet import *
from ground import *
from wall import *
from player import *
from portal import *
from enemy import *
from npc import *

class Stage1:
    def __init__(self, gameManager, stageManager):
        self.gameManager = gameManager
        self.stageManager = stageManager
        self.running = True
        self.stageIsCleared = False
        self.gameOver = False

        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.walls = pygame.sprite.LayeredUpdates()
        self.player = pygame.sprite.LayeredUpdates()
        self.npcs = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.portals = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.LayeredUpdates()

        self.loading()  # loading the map
        self.createMap()  # Create the map

    def run(self):
        while self.running == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return -1
            self.update()
            self.draw()
            self.stageIsCleared = True
        if self.gameOver == True:
            self.stageManager.stageIdx = -1
        return self.stageManager.stageIdx

    def loading(self):
        self.gameManager.screen.fill(COLOR_BLACK)
        pygame.display.update()

    def createMap(self):
        for i, row in enumerate(TILE_MAP[self.stageManager.stageIdx]):
            for j, col in enumerate(row):
                if col == "W": # Wall
                    Wall(self, j, i, 0)
                elif col == "P": # player
                    self.stageManager.player.setStage(j, i, self)
                elif col == "E": # enemies
                    Enemy(self, j, i)

                if col == "a": # npcs
                    Npc(self, j, i, 0)
                elif col == "b": # npcs
                    Npc(self, j, i, 1)

                if col == ">": # forward portal
                    Portal(self, j, i, 1)
                elif col == "<": # backward portal
                    Portal(self, j, i, -1)

                if col == ".": # Ground
                    Ground(self, j, i, 0)
                else:
                    Ground(self, j, i, 0)

    def update(self):
        self.gameManager.clock.tick(200) # set FPS
        self.all_sprites.update()

    def draw(self):
        self.gameManager.screen.fill(COLOR_BLACK)
        self.all_sprites.draw(self.gameManager.screen)
        pygame.display.update()