import pygame
from spriteSheet import *
from stage.stage0 import Stage0
from stage.stage1 import Stage1
from player import *
class StageManager:
    def __init__(self, gameManager):
        self.gameManager = gameManager
        self.stageIdx = 0
        self.stages = {
            0: lambda: Stage0(gameManager, self),  # Lazy initialization
            1: lambda: Stage1(gameManager, self),
        }
        self.cur_stage = None

        self.background_spriteSheet = SpriteSheet(BACKGROUND_IMAGE)
        self.character_spriteSheet = SpriteSheet(CHARACTER_IMAGE)
        self.enemy_spriteSheet = SpriteSheet(ENEMY_IMAGE)
        self.attack_spriteSheet = SpriteSheet(ATTACK_IMAGE)
        self.portal_image = pygame.image.load(PORTAL_IMAGE).convert_alpha()
        self.player = Player(self)  # Initialize player with the first stage

    def play(self):
        while self.stageIdx != -1:
            print(f"StageManager : Running stage {self.stageIdx}")
            self.cur_stage = self.stages[self.stageIdx]()
            next_stage = self.cur_stage.run()  # Run the current stage and get the next stage index
            if next_stage != -1:
                self.stageIdx = next_stage
            else:
                break
        print("StageManager : Game Over")

