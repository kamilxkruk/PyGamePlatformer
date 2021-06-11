import pygame
from pygame import Rect
from pygame.sprite import Sprite
from settings import *

class BulletSprite(Sprite):
    def __init__(self, bulletDirection, playerRect: Rect):
        Sprite.__init__(self)
        self.image = pygame.Surface((8,8))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.bulletDirection = bulletDirection
        if self.bulletDirection == DIRECTION_RIGHT:
            self.rect.midleft = playerRect.midright
        elif self.bulletDirection == DIRECTION_LEFT:
            self.rect.midright = playerRect.midleft

    def updateBullet(self):
        if self.bulletDirection == DIRECTION_RIGHT:
            self.rect.x += 5
        elif self.bulletDirection == DIRECTION_LEFT:
            self.rect.x -= 5