import pygame
from config.config import *

from spriteSheet import *
from ground import *
from block import *
from player import *
from portal import *
from enemy import *
from npc import *

class Stage0:
    def __init__(self, GM):
        self.running = True
        self.game_manager = GM
        self.IsMessage = True
        self.messageIdx = 0
        self.IsMessageCleared = False
        self.IsStageCleared = False

        self.background_spriteSheet = SpriteSheet(BACKGROUND_IMAGE)
        self.character_spriteSheet = SpriteSheet(CHARACTER_IMAGE)
        self.enemy_spriteSheet = SpriteSheet(ENEMY_IMAGE)
        self.attack_spriteSheet = SpriteSheet(ATTACK_IMAGE)
        self.portal_image = pygame.image.load(PORTAL_IMAGE).convert_alpha()

        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.npcs = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.portals = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.LayeredUpdates()

    def loading(self):
        self.game_manager.screen.fill(COLOR_BLACK)
        self.game_manager.clock.tick(60)
        pygame.display.update()
        # pygame.time.wait(1000) # ToDo
        print("end loading!")

    def createMap(self):
        print("start createMap!")
        for i, row in enumerate(TILE_MAP[self.game_manager.stageIdx]):
            for j, col in enumerate(row):
                if col == "B": # blocks
                    Block(self, j, i, 0)
                elif col == "E": # enemies
                    Enemy(self, j, i)
                elif col == "P": # player
                    self.player = Player(self, j, i)

                if col == ">": # forward portal
                    print("forward portal")
                    Portal(self.game_manager, self, j, i, 1)
                elif col == "<": # backward portal
                    print("backward portal")
                    Portal(self.game_manager, self, j, i, -1)

                if col == "a": # npcs
                    Npc(self, j, i, 0)
                elif col == "b": # npcs
                    Npc(self, j, i, 1)


                if col == "0": # Ground
                    Ground(self, j, i, 0)
                else:
                    Ground(self, j, i, 0)

        print("end createMap!")

    def update(self):
        self.all_sprites.update()
        # print("end update!")

    def draw(self):
        self.game_manager.screen.fill(COLOR_BLACK)
        self.all_sprites.draw(self.game_manager.screen)
        self.game_manager.clock.tick(CLOCK_FPS)
        pygame.display.update()
        # print("end draw!")

    def message(self):
        while self.IsMessage:
            messageRest = MESSAGE_COUNT[self.messageIdx]
            messageCnt = 0

            print("message idx = %d" % self.messageIdx)
            print("messageCnt = %d" % messageCnt)

            while messageCnt < messageRest:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.IsMessage = False
                        self.running = False
                        self.game_manager.running = False
                        self.game_manager.IsIntro = False
                        self.game_manager.IsPlay = False
                        self.game_manager.IsOutro = False
                        return

                speaker, message = MESSAGE_LIST[self.messageIdx][messageCnt]
                messagebox = Message(*MESSAGE_POS, *MESSAGE_SIZE, MESSAGE_FONT_SIZE, speaker, message)

                mouse_pos = pygame.mouse.get_pos()
                mouse_pressed = pygame.mouse.get_pressed()

                messagebox.draw(self.game_manager.screen)
                self.game_manager.clock.tick(CLOCK_FPS)
                pygame.display.update()

                if messageCnt > 0 and messagebox.is_prev_pressed(mouse_pos, mouse_pressed):
                    messageCnt -= 1

                if messagebox.is_next_pressed(mouse_pos, mouse_pressed):
                    messageCnt += 1

            self.IsMessage = False
            self.messageIdx += 1
            if self.messageIdx == MESSAGE_INIT_IDX_STAGE[self.game_manager.stageIdx + 1]:
                self.IsMessageCleared = True

    def IsNpcAllCleared(self):
        for npc in self.npcs:
            if npc.isCleared == False:
                return False
        return True

    def run(self):
        self.loading()
        self.createMap()
        stage0Var = 0
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    self.game_manager.running = False
                    self.game_manager.IsIntro = False
                    self.game_manager.IsPlay = False
                    self.game_manager.IsOutro = False
                    return

            self.update()
            self.draw()
            self.message()
            if self.IsNpcAllCleared() and stage0Var == 0:
                self.player.moveCntEnable = True
                stage0Var = 1

            if self.player.moveCnt > 50:
                print("Over player moveCnt")
                self.IsMessage = True
                self.player.moveCntEnable = False
                self.player.moveCnt = 0

            if self.IsMessageCleared:
                self.IsStageCleared = True

            if self.IsStageCleared:
                self.game_manager.stageIsCleared[self.game_manager.stageIdx] = True

