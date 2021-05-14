import pygame
from settings import *

class CoinSprite(pygame.sprite.Sprite):

    def __init__(self,x:float,y:float):
       pygame.sprite.Sprite.__init__(self)
       self.image = TERRAIN_GRAPHICS[T_COIN[0]]
       self.rect = self.image.get_rect()
       self.rect.topleft = (x,y)