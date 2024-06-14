import sys
import pygame

from config.config import *
from image import *
from button import *
from stage import *

INTRO_TEXT_CENTER_X = WINDOW_WIDTH // 2 + TILE_SIZE // 2
INTRO_TEXT_CENTER_Y = WINDOW_HEIGHT // 4
INTRO_TEXT_POS = [INTRO_TEXT_CENTER_X, INTRO_TEXT_CENTER_Y]

INTRO_BUTTON_WIDTH = TILE_SIZE * 9
INTRO_BUTTON_HEIGTH = TILE_SIZE * 2
INTRO_BUTTON_SIZE = [INTRO_BUTTON_WIDTH, INTRO_BUTTON_HEIGTH]
INTRO_BUTTON_X = TILE_SIZE * 6
INTRO_BUTTON_Y = TILE_SIZE * 8
INTRO_BUTTON_POS = [INTRO_BUTTON_X, INTRO_BUTTON_Y]

OUTRO_TEXT_CENTER_X = WINDOW_WIDTH // 2 + TILE_SIZE // 2
OUTRO_TEXT_CENTER_Y = WINDOW_HEIGHT // 4
OUTRO_TEXT_POS = [OUTRO_TEXT_CENTER_X, OUTRO_TEXT_CENTER_Y]

RESTART_BUTTON_WIDTH = TILE_SIZE * 9
RESTART_BUTTON_HEIGTH = TILE_SIZE * 2
RESTART_BUTTON_SIZE = [RESTART_BUTTON_WIDTH, RESTART_BUTTON_HEIGTH]
RESTART_BUTTON_X = TILE_SIZE * 6
RESTART_BUTTON_Y = TILE_SIZE * 8
RESTART_BUTTON_POS = [RESTART_BUTTON_X, RESTART_BUTTON_Y]

QUIT_BUTTON_WIDTH = TILE_SIZE * 9
QUIT_BUTTON_HEIGTH = TILE_SIZE * 2
QUIT_BUTTON_SIZE = [QUIT_BUTTON_WIDTH, QUIT_BUTTON_HEIGTH]
QUIT_BUTTON_X = TILE_SIZE * 6
QUIT_BUTTON_Y = TILE_SIZE * 12
QUIT_BUTTON_POS = [QUIT_BUTTON_X, QUIT_BUTTON_Y]

class GameManager:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(WINDOW_SIZE)
        pygame.display.set_caption("MING IN BYENGJUM")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('malgungothic', FONT_SIZE)

        self.running = True
        self.IsIntro = True
        self.IsPlay = False
        self.IsOutro = False

        self.stageIdx = 0
        self.stageIsCleared = [
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
        ]

    def intro(self):
        intro_text = self.font.render('Ming in ByengJum', True, COLOR_BLACK)
        intro_text_rect = intro_text.get_rect(center=INTRO_TEXT_POS)

        play_button = Button(*INTRO_BUTTON_POS, *INTRO_BUTTON_SIZE, COLOR_WHITE, COLOR_BLACK, 'Play', FONT_SIZE)
        intro_background = Image().intro_background

        while self.IsIntro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.IsIntro = False
                    self.IsPlay = False
                    self.IsOutro = False
                    self.running = False
                    return

            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            if play_button.is_pressed(mouse_pos, mouse_pressed):
                self.IsIntro = False
                self.IsPlay = True
                self.IsOutro = True # Todo: remove this line
                return

            self.screen.blit(intro_background, (0,0))
            self.screen.blit(intro_text, intro_text_rect)
            self.screen.blit(play_button.image, play_button.rect)
            self.clock.tick(CLOCK_FPS)
            pygame.display.update()

    def outro(self):
        outro_text = self.font.render('Game Over!', True, COLOR_WHITE)
        outro_text_rect = outro_text.get_rect(center=OUTRO_TEXT_POS)

        restart_button = Button(*RESTART_BUTTON_POS, *RESTART_BUTTON_SIZE, COLOR_WHITE, COLOR_BLACK, 'Restart', FONT_SIZE)
        quit_button = Button(*QUIT_BUTTON_POS, *QUIT_BUTTON_SIZE, COLOR_WHITE, COLOR_BLACK, 'Quit', FONT_SIZE)
        outro_background = Image().outro_background

        while self.IsOutro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    self.IsIntro = False
                    self.IsPlay = False
                    self.IsOutro = False
                    return

            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            if restart_button.is_pressed(mouse_pos, mouse_pressed):
                self.running = True
                self.IsIntro = True
                self.IsPlay = False
                self.IsOutro = False
                return

            if quit_button.is_pressed(mouse_pos, mouse_pressed):
                self.running = False
                self.IsIntro = False
                self.IsPlay = False
                self.IsOutro = False
                return

            self.screen.blit(outro_background, (0, 0))
            self.screen.blit(outro_text, outro_text_rect)
            self.screen.blit(restart_button.image, restart_button.rect)
            self.screen.blit(quit_button.image, quit_button.rect)
            self.clock.tick(CLOCK_FPS)
            pygame.display.update()

    def play(self):
        while self.IsPlay:
            print("main play")
            Stage(self)


if __name__ == "__main__":
    game_manager = GameManager()
    while game_manager.running:
        game_manager.intro()
        game_manager.play()
        game_manager.outro()

    pygame.quit()
    sys.exit()