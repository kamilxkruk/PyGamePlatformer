import pygame
from settings import *

class PlayerSprite(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(0, 0, BOX_SIZE, BOX_SIZE)
        self.rect.center = (SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2)
        self.image = pygame.Surface((BOX_SIZE, BOX_SIZE))
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        self.playerColour = LIGHT_BLUE
        pygame.draw.circle(self.image, self.playerColour, (BOX_SIZE / 2, BOX_SIZE / 2), BOX_SIZE / 2)