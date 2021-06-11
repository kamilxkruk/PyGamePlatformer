import pygame

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 700

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 30

FRICTION = 0.13
GRAVITY = 1.5

BOX_SIZE = 30

# colors
WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,255,0)
RED = (255,0,0)
YELLOW = (255,255,0)
LIGHT_BLUE = (3,244,252)
BROWN = (122, 119, 106)
GRAY = (128,138,138)

# platforms
PLATFORMS = [
    (250,550),
    (150,450),
    (500,200),
    (350,350),
    (550,285,50)
]

#Level editor settings
TILE_SIZE = 40
EDITOR_ROWS = SCREEN_HEIGHT//TILE_SIZE
EDITOR_COLUMNS = SCREEN_WIDTH//TILE_SIZE

T_EMPTY = (0,'')
T_GRASS = (1,'trawa1.png')
T_GRASS1 = (2,'trawa2.png')
T_GRASS2 = (3,'trawa3.png')
T_DIRT = (4,'ziemia.png')
T_STONE = (5,'kamien.png')
T_SAND = (6,'piasek.png')
T_COIN = (7,'coin.png')
T_LAVA_TOP = (8,'lava_top.png')
T_LAVA_DEEP = (9,'lava_deep.png')
T_MONSTER = (10,'monster.png')
TERRAIN_TYPES = [T_GRASS,T_GRASS1,T_GRASS2,T_DIRT,T_STONE,T_SAND,T_COIN,T_LAVA_TOP,T_LAVA_DEEP,T_MONSTER]

TERRAIN_GRAPHICS = {}
for terrain in TERRAIN_TYPES:
    image = pygame.image.load('assets/'+terrain[1])
    image = pygame.transform.scale(image,(TILE_SIZE,TILE_SIZE))
    TERRAIN_GRAPHICS[terrain[0]] = image

#Game mode consts
GAMEMODE_MENU = 0
GAMEMODE_GAME = 1
GAMEMODE_LEVEL_EDITOR = 2

#Direction consts
DIRECTION_LEFT = 0
DIRECTION_RIGHT = 1
