TILE_SIZE = 32
WINDOW_WIDTH = TILE_SIZE * 20
WINDOW_HEIGHT = TILE_SIZE * 20

MESSAGE_WIDTH = WINDOW_WIDTH - 40
MESSAGE_HEIGHT = WINDOW_HEIGHT/4 + 20
MESSAGE_SIZE = [MESSAGE_WIDTH, MESSAGE_HEIGHT]

MESSAGE_POS_X = 10
MESSAGE_POS_Y = WINDOW_HEIGHT - MESSAGE_HEIGHT - 30
MESSAGE_POS = [MESSAGE_POS_X, MESSAGE_POS_Y]

MESSAGE_FONT_SIZE = 24

MESSAGE_COUNT_0 = 2
MESSAGE_COUNT_1 = 2
MESSAGE_COUNT_2 = 2

MESSAGE_COUNT = [
    MESSAGE_COUNT_0,
    MESSAGE_COUNT_1,
    MESSAGE_COUNT_2,
]

MESSAGE_INIT_IDX_STAGE_0 = 0
MESSAGE_INIT_IDX_STAGE_1 = 2
MESSAGE_INIT_IDX_STAGE_2 = 4
MESSAGE_INIT_IDX_STAGE = [
    MESSAGE_INIT_IDX_STAGE_0, # stage 0
    MESSAGE_INIT_IDX_STAGE_1, # stage 1
    MESSAGE_INIT_IDX_STAGE_2, # stage 2
]

MESSAGE_LIST_1 = [
    ("???", "터덜터덜 출근을 한 밍쥬"),
    ("???", "자리에 앉기도 전 밍쥬를 부르는 대표님"),
    ("???", "대표님에게 가봐야 할 듯 하다."),
    ("???", "대표에게 가서 \"m\"을 누르시오"),
]
MESSAGE_LIST_2 = [
    ("민쥬", "아잇!"),
    ("민쥬", "퇴근해!"),
]
MESSAGE_LIST_3 = [
    ("Speaker1", "Welcome to the first stage!"),
    ("Speaker2", "Good luck!"),
]
MESSAGE_LIST_4 = [
    ("Speaker1", "Now it's getting harder!"),
    ("Speaker2", "Stay focused!"),
]

MESSAGE_LIST = [
    MESSAGE_LIST_1,
    MESSAGE_LIST_2,
    MESSAGE_LIST_3,
    MESSAGE_LIST_4,
]
