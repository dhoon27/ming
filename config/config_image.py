IMAGE_PATH = "./img/"
PNG = ".png"
JPG = ".jpg"

INTRO_IMAGE_NAME = "intro"
INTRO_IMAGE = IMAGE_PATH + INTRO_IMAGE_NAME + PNG

OUTRO_IMAGE_NAME = "outro"
OUTRO_IMAGE = IMAGE_PATH + OUTRO_IMAGE_NAME + PNG

CHARACTER_IMAGE_NAME = "character"
CHARACTER_IMAGE = IMAGE_PATH + CHARACTER_IMAGE_NAME + PNG

ENEMY_IMAGE_NAME = "enemy"
ENEMY_IMAGE = IMAGE_PATH + ENEMY_IMAGE_NAME + PNG

PORTAL_IMAGE_NAME = "portal"
PORTAL_IMAGE = IMAGE_PATH + PORTAL_IMAGE_NAME + PNG

NPC_IMAGE_NAME = "npc"
NPC_IMAGE = IMAGE_PATH + NPC_IMAGE_NAME + PNG

ATTACK_IMAGE_NAME = "attack"
ATTACK_IMAGE = IMAGE_PATH + ATTACK_IMAGE_NAME + PNG

# attack.png
ANIMATE_ATTACK_DOWN_0 = [32 * 0, 32 * 1]
ANIMATE_ATTACK_DOWN_1 = [32 * 1, 32 * 1]
ANIMATE_ATTACK_DOWN_2 = [32 * 2, 32 * 1]
ANIMATE_ATTACK_DOWN_3 = [32 * 3, 32 * 1]
ANIMATE_ATTACK_DOWN_4 = [32 * 4, 32 * 1]

ANIMATE_ATTACK_UP_0 = [32 * 0, 32 * 0]
ANIMATE_ATTACK_UP_1 = [32 * 1, 32 * 0]
ANIMATE_ATTACK_UP_2 = [32 * 2, 32 * 0]
ANIMATE_ATTACK_UP_3 = [32 * 3, 32 * 0]
ANIMATE_ATTACK_UP_4 = [32 * 4, 32 * 0]

ANIMATE_ATTACK_LEFT_0 = [32 * 0, 32 * 3]
ANIMATE_ATTACK_LEFT_1 = [32 * 1, 32 * 3]
ANIMATE_ATTACK_LEFT_2 = [32 * 2, 32 * 3]
ANIMATE_ATTACK_LEFT_3 = [32 * 3, 32 * 3]
ANIMATE_ATTACK_LEFT_4 = [32 * 4, 32 * 3]

ANIMATE_ATTACK_RIGHT_0 = [32 * 0, 32 * 2]
ANIMATE_ATTACK_RIGHT_1 = [32 * 1, 32 * 2]
ANIMATE_ATTACK_RIGHT_2 = [32 * 2, 32 * 2]
ANIMATE_ATTACK_RIGHT_3 = [32 * 3, 32 * 2]
ANIMATE_ATTACK_RIGHT_4 = [32 * 4, 32 * 2]

# character.png
CHARACTER_PLAYER = [3, 2]
CHARACTER_PLAYER_DOWN = CHARACTER_PLAYER
CHARACTER_PLAYER_DOWN_1 = [35, 2]
CHARACTER_PLAYER_DOWN_2 = [68, 2]

CHARACTER_PLAYER_UP = [3, 34]
CHARACTER_PLAYER_UP_1 = [35, 34]
CHARACTER_PLAYER_UP_2 = [68, 34]

CHARACTER_PLAYER_LEFT = [3, 98]
CHARACTER_PLAYER_LEFT_1 = [35, 98]
CHARACTER_PLAYER_LEFT_2 = [68, 98]

CHARACTER_PLAYER_RIGHT = [3, 66]
CHARACTER_PLAYER_RIGHT_1 = [35, 66]
CHARACTER_PLAYER_RIGHT_2 = [68, 66]

CHARACTER_ENEMY = [3, 2]
CHARACTER_ENEMY_DOWN = CHARACTER_ENEMY
CHARACTER_ENEMY_DOWN_1 = [35, 2]
CHARACTER_ENEMY_DOWN_2 = [68, 2]

CHARACTER_ENEMY_UP = [3, 34]
CHARACTER_ENEMY_UP_1 = [35, 34]
CHARACTER_ENEMY_UP_2 = [68, 34]

CHARACTER_ENEMY_LEFT = [3, 98]
CHARACTER_ENEMY_LEFT_1 = [35, 98]
CHARACTER_ENEMY_LEFT_2 = [68, 98]

CHARACTER_ENEMY_RIGHT = [3, 66]
CHARACTER_ENEMY_RIGHT_1 = [35, 66]
CHARACTER_ENEMY_RIGHT_2 = [68, 66]

# npc.png
NPC_GRANDMOTHER_NAME = "grandmother"
NPC_GRANDMOTHER_IMAGE = IMAGE_PATH + NPC_GRANDMOTHER_NAME + PNG

NPC_GRANDFATHER_NAME = "grandfather"
NPC_GRANDFATHER_IMAGE = IMAGE_PATH + NPC_GRANDFATHER_NAME + PNG

NPC_IMAGE = [NPC_GRANDMOTHER_IMAGE, NPC_GRANDFATHER_IMAGE]


# background.png
BACKGROUND_IMAGE_NAME = "background"
BACKGROUND_IMAGE = IMAGE_PATH + BACKGROUND_IMAGE_NAME + PNG

BLOCK_ROCK = [32 * 30, 32 * 14]

BLOCK_IMAGE_LIST = [
    BLOCK_ROCK,
]

GROUND_GREEN_GRASS = [32 * 2, 32 * 11]
GROUND_COMPANY_TILE = [32 * 7, 32 * 13]
GROUND_COMPANY_BLOCK = [32 * 6, 32 * 13]

GROUND_IMAGE_LIST = [
    GROUND_GREEN_GRASS,
]