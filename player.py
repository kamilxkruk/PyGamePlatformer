import pygame
from settings import *


class Player(object):
    def __init__(self):
        self.centerOfScreen = (SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2)
        self.position = (self.centerOfScreen)
        self.velocity_X = 0
        self.velocity_Y = 0
        self.acc_x = 0
        self.acc_y = 0
        self.rectangle = pygame.Rect(0,0, BOX_SIZE, BOX_SIZE)
        self.rectangle.center = self.position

        self.playerSprite = pygame.sprite.Sprite()
        self.playerSprite.rect = self.rectangle
        #Setting sprite
        self.playerSprite.image = pygame.Surface((BOX_SIZE,BOX_SIZE))
        pygame.draw.circle(self.playerSprite.image,LIGHT_BLUE,(BOX_SIZE/2,BOX_SIZE/2),BOX_SIZE/2)


        self.playerSpriteGroup = pygame.sprite.Group()
        self.playerSpriteGroup.add(self.playerSprite)

        self.myFont = pygame.font.SysFont("Times New Roman", 18)
        self.infoLabel = self.myFont.render('Test',1,WHITE)
        self.infoLabelRect = self.infoLabel.get_rect()

        self.velocityLabel = self.myFont.render('0',1,WHITE)
        self.velocityLabelRect = self.velocityLabel.get_rect()
        self.velocityLabelRect.topleft = (0,30)
        # self.infoLabelRect.bottomright = (SCREEN_WIDTH,SCREEN_HEIGHT)



    def move(self, keys):
        self.infoLabel = self.myFont.render('A: '+str(keys[pygame.K_a])+' D: '+str(keys[pygame.K_d]) ,1,WHITE)
        self.acc_x = 0
        if self.rectangle.bottom < SCREEN_HEIGHT:
            self.acc_y = GRAVITY
        else:
            self.velocity_Y = 0
            self.acc_y = 0
            self.rectangle.bottom = SCREEN_HEIGHT

        if keys[pygame.K_d]:
            self.acc_x = 1.5
        elif keys[pygame.K_a]:
            self.acc_x = -1.5

        if keys[pygame.K_w]:
            self.acc_y = -3.5
        elif keys[pygame.K_s]:
            self.acc_y = 3.5


        self.velocity_X += self.acc_x
        self.velocity_Y += self.acc_y

        if abs(self.velocity_X) > 0.5:
            if self.velocity_X > 0:
                self.velocity_X -= self.velocity_X * FRICTION
            elif self.velocity_X < 0:
                self.velocity_X += abs(self.velocity_X) * FRICTION

            if self.velocity_X > 0 or (self.velocity_X < 0 and  self.rectangle.left + self.velocity_X > 0):
                self.rectangle.x += self.velocity_X
                if self.velocity_X > 0 and self.rectangle.left > SCREEN_WIDTH:
                    self.rectangle.left = 0

        if abs(self.velocity_Y) > 0.5:
            if self.velocity_Y > 0:
                self.velocity_Y -= self.velocity_Y * FRICTION
            elif self.velocity_Y < 0:
                self.velocity_Y += abs(self.velocity_Y) * FRICTION

            self.rectangle.y += self.velocity_Y

        self.velocityLabel = self.myFont.render('V: '+str(self.velocity_X),1,WHITE)


    def display(self, display: pygame.Surface):
        display.blit(self.infoLabel,self.infoLabelRect)
        display.blit(self.velocityLabel,self.velocityLabelRect)

        self.playerSpriteGroup.update()
        self.playerSpriteGroup.draw(display)

        # pygame.draw.circle(display,LIGHT_BLUE,self.rectangle.center,BOX_SIZE/2)
        # pygame.draw.rect(display,WHITE,self.rectangle)
