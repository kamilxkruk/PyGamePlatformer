import pygame
from settings import *

class PlatformSprite(pygame.sprite.Sprite):

    def __init__(self,centerX:float,centerY:float, width:int=150, height:int=30):
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.Surface((width, height))
       self.image.fill(BROWN)
       self.rect = self.image.get_rect()
       self.rect.center = (centerX,centerY)