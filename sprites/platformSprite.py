import pygame
from settings import *

class PlatformSprite(pygame.sprite.Sprite):

    def __init__(self, x:float,y:float, tileImage: pygame.Surface, width:int=50, height:int=50):
       pygame.sprite.Sprite.__init__(self)
       self.image = tileImage
       self.rect = self.image.get_rect()
       self.rect.topleft = (x,y)