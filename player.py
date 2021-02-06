import pygame
from settings import *


class Player(object):
    def __init__(self):
        self.centerOfScreen = (SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2)
        self.position = self.centerOfScreen
        self.velocity_X = 0
        self.velocity_Y = 0
        self.acc_x = 0
        self.acc_y = 0
        self.rectangle = pygame.Rect(0,0, BOX_SIZE, BOX_SIZE)
        self.rectangle.center = self.position

        self.myFont = pygame.font.SysFont("Times New Roman", 18)
        self.infoLabel = self.myFont.render('Test',1,WHITE)
        self.infoLabelRect = self.infoLabel.get_rect()
        # self.infoLabelRect.bottomright = (SCREEN_WIDTH,SCREEN_HEIGHT)


    def move(self, keys):
        self.infoLabel = self.myFont.render('A: '+str(keys[pygame.K_a])+' D: '+str(keys[pygame.K_d]) ,1,WHITE)

        self.velocity_X = 0

        if keys[pygame.K_d]:
            self.velocity_X = 5
        elif keys[pygame.K_a]:
            self.velocity_X = -5

        self.rectangle.x += self.velocity_X




    def display(self, display: pygame.Surface):
        display.blit(self.infoLabel,self.infoLabelRect)
        pygame.draw.circle(display,(3,252,40),(self.rectangle.x+15,self.rectangle.y+15),15)

