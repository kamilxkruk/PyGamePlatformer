import pygame
import settings
from pygame import Surface
from pygame.sprite import Sprite

class BaseTerrainSprite(Sprite):

    def __init__(self,x:float,y:float):
       Sprite.__init__(self)
       self.image = Surface((8,8))
       self.rect = self.image.get_rect()
       self.rect.topleft = (x,y)