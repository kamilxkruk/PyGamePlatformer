import pygame
from settings import *
from pygame.sprite import Sprite

class MonsterSprite(Sprite):

    AMPLITUDE = 20

    def __init__(self,x:float,y:float):
        Sprite.__init__(self)
        self.image = TERRAIN_GRAPHICS[T_MONSTER[0]]
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.respawnPoint = self.rect.topleft
        self.lives = 3
        self.direction = -1

    def move(self):
        #Tutaj opiszemy logike poruszania się naszego potwora
        if self.respawnPoint[1] - self.rect.topleft[1] > 20:
            self.direction *= -1
        elif self.rect.topleft[1] >= self.respawnPoint[1]:
            self.direction *= -1
            self.rect.topleft = self.respawnPoint

        self.rect.y += self.direction
