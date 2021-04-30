import pygame
from pygame.sprite import spritecollide
from settings import *
from sprites.coinSprite import CoinSprite
from sprites.playerSprite import PlayerSprite
from sprites.platformSprite import PlatformSprite
from random import randint


class Player(object):
    def __init__(self):
        self.centerOfScreen = (SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2)
        self.velocity_X = 0
        self.velocity_Y = 0
        self.acc_x = 0
        self.acc_y = 0

        self.points = 0

        self.iteration = 0

        #Setting up sprites
        self.playerSprite = PlayerSprite()
        self.playerSpriteGroup = pygame.sprite.Group()
        self.playerSpriteGroup.add(self.playerSprite)

        self.rectangle = self.playerSprite.rect

        self.platformSpriteGroup = pygame.sprite.Group()
        for platform in PLATFORMS:
            self.platformSpriteGroup.add(PlatformSprite(*platform))
            # * - spread operator

        self.coinSpriteGroup = pygame.sprite.Group()
        self.coinSpriteGroup.add(CoinSprite(self.centerOfScreen[0]+100,self.centerOfScreen[1]+150))
        self.coinSpriteGroup.add(CoinSprite(self.centerOfScreen[0]-200,self.centerOfScreen[1]))

        self.myFont = pygame.font.SysFont("Times New Roman", 18)
        self.infoLabel = self.myFont.render('Points: 0',1,WHITE)
        self.infoLabelRect = self.infoLabel.get_rect()
        self.infoLabelRect.topleft = (0,SCREEN_HEIGHT)

        self.musicPlayer = pygame.mixer.init()
        self.coinSound = pygame.mixer.Sound('sounds/1.mp3')

        self.platformCollision = []


    def move(self, keys):
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
            self.playerSprite.rect.y += 1
            hits = self.playerSprite.rect.midbottom[1] > SCREEN_HEIGHT
            self.playerSprite.rect.y -= 1
            if hits or self.platformCollision:
                self.velocity_Y = -30




        self.velocity_X += self.acc_x
        self.velocity_Y += self.acc_y

        if abs(self.velocity_X) > 0.5:
            if self.velocity_X > 0:
                self.velocity_X -= self.velocity_X * FRICTION
            elif self.velocity_X < 0:
                self.velocity_X += abs(self.velocity_X) * FRICTION

            if self.velocity_X > 0 or (self.velocity_X < 0 and  self.rectangle.left + self.velocity_X > 0):
                self.rectangle.x += self.velocity_X
                platformXCollide = spritecollide(self.playerSprite,self.platformSpriteGroup,False)
                if platformXCollide and self.velocity_X > 0: # Ruch w prawo
                    self.velocity_X = 0
                    self.playerSprite.rect.right = platformXCollide[0].rect.left-1

                elif platformXCollide and self.velocity_X < 0: #Ruch w lewo
                    self.velocity_X = 0
                    self.playerSprite.rect.left = platformXCollide[0].rect.right+1


                if self.velocity_X > 0 and self.rectangle.left > SCREEN_WIDTH:
                    self.rectangle.right = 0

        if abs(self.velocity_Y) > 0.5:
            if self.velocity_Y > 0:
                self.velocity_Y -= self.velocity_Y * FRICTION
            elif self.velocity_Y < 0:
                self.velocity_Y += abs(self.velocity_Y) * FRICTION

            self.rectangle.y += self.velocity_Y
            collidePlatformY = spritecollide(self.playerSprite,self.platformSpriteGroup,False)
            if collidePlatformY and self.velocity_Y < 0:
                self.velocity_Y = 0
                self.playerSprite.rect.top = collidePlatformY[0].rect.bottom+1

    def detectCoinCollision(self):
        collision = spritecollide(self.playerSprite,self.coinSpriteGroup,True)
        if collision:
            self.points += 1
            self.infoLabel = self.myFont.render('Points: '+ str(self.points), 1,WHITE)
            # self.coinSound.play()

    def detectPlatformCollision(self):
        self.platformCollision = spritecollide(self.playerSprite,self.platformSpriteGroup,False)
        if self.platformCollision and self.velocity_Y>0:
            self.acc_y = 0
            self.velocity_Y = 0
            self.onPlatform = True
            self.rectangle.bottom = self.platformCollision[0].rect.top


    def display(self, display: pygame.Surface):
        # self.iteration += 1
        # if self.iteration > 50:
        #     self.iteration = 0

        display.blit(self.infoLabel,self.infoLabelRect)
        #
        # allSprites = self.platformSpriteGroup.sprites()
        # for x in allSprites:
        #     x.rect.y += 2
        #
        # if self.iteration == 50:
        #     self.platformSpriteGroup.add(PlatformSprite(randint(150,550),285))
        #

        self.platformSpriteGroup.update()
        self.platformSpriteGroup.draw(display)

        self.coinSpriteGroup.update()
        self.coinSpriteGroup.draw(display)

        self.playerSpriteGroup.update()
        self.playerSpriteGroup.draw(display)

        self.detectPlatformCollision()

        self.detectCoinCollision()






