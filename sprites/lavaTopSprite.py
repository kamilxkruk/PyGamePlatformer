import pygame
from settings import *
from sprites.baseTerrainSprite import BaseTerrainSprite


class LavaTopSprite(BaseTerrainSprite):

    def __init__(self,x:float,y:float):
       BaseTerrainSprite.__init__(self,x,y)
       self.image = TERRAIN_GRAPHICS[T_LAVA_TOP[0]]
