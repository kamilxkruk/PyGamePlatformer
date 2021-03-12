import pygame
from settings import *

class CoinSprite(pygame.sprite.Sprite):

    def __init__(self,centerX:float,centerY:float):
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.Surface((30, 30))
       self.image.fill(YELLOW)
       self.rect = self.image.get_rect()
       self.rect.center = (centerX,centerY)