import pygame
from settings import *
from sprites.coinSprite import CoinSprite
from sprites.playerSprite import PlayerSprite
from sprites.platformSprite import PlatformSprite

class Player(object):
    def __init__(self):
        self.centerOfScreen = (SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2)
        self.velocity_X = 0
        self.velocity_Y = 0
        self.acc_x = 0
        self.acc_y = 0

        #Setting up sprites
        self.playerSprite = PlayerSprite()
        self.playerSpriteGroup = pygame.sprite.Group()
        self.playerSpriteGroup.add(self.playerSprite)

        self.rectangle = self.playerSprite.rect

        self.platformSpriteGroup = pygame.sprite.Group()
        self.platformSpriteGroup.add(PlatformSprite(self.centerOfScreen[0]-150,self.centerOfScreen[1]+200))

        self.coinSpriteGroup = pygame.sprite.Group()
        self.coinSpriteGroup.add(CoinSprite(self.centerOfScreen[0]+100,self.centerOfScreen[1]+150))
        self.coinSpriteGroup.add(CoinSprite(self.centerOfScreen[0]-200,self.centerOfScreen[1]))

        self.myFont = pygame.font.SysFont("Times New Roman", 18)
        self.infoLabel = self.myFont.render('Test',1,WHITE)
        self.infoLabelRect = self.infoLabel.get_rect()

        self.velocityLabel = self.myFont.render('0',1,WHITE)
        self.velocityLabelRect = self.velocityLabel.get_rect()
        self.velocityLabelRect.topleft = (0,30)
        # self.infoLabelRect.bottomright = (SCREEN_WIDTH,SCREEN_HEIGHT)

        self.musicPlayer = pygame.mixer.init()
        self.coinSound = pygame.mixer.Sound('sounds/1.mp3')



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
            self.playerSprite.rect.y += 1
            hits = self.playerSprite.rect.midbottom[1] > SCREEN_HEIGHT
            self.playerSprite.rect.y -= 1
            if hits:
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
                if self.velocity_X > 0 and self.rectangle.left > SCREEN_WIDTH:
                    self.rectangle.right = 0

        if abs(self.velocity_Y) > 0.5:
            if self.velocity_Y > 0:
                self.velocity_Y -= self.velocity_Y * FRICTION
            elif self.velocity_Y < 0:
                self.velocity_Y += abs(self.velocity_Y) * FRICTION

            self.rectangle.y += self.velocity_Y

        self.velocityLabel = self.myFont.render('V: '+str(self.velocity_X),1,WHITE)

    def detectCoinCollision(self):
        collision = pygame.sprite.spritecollide(self.playerSprite,self.coinSpriteGroup,True)
        if collision:
            pass
           #  Dodać punkty
           # self.coinSound.play()

    def detectPlatformCollision(self):
        platformCollision = pygame.sprite.spritecollide(self.playerSprite,self.platformSpriteGroup,False)
        if platformCollision and self.velocity_Y>0:
            self.acc_y = 0
            self.velocity_Y = 0
            self.rectangle.bottom = platformCollision[0].rect.top


    def display(self, display: pygame.Surface):
        display.blit(self.infoLabel,self.infoLabelRect)
        display.blit(self.velocityLabel,self.velocityLabelRect)

        self.platformSpriteGroup.update()
        self.platformSpriteGroup.draw(display)

        self.coinSpriteGroup.update()
        self.coinSpriteGroup.draw(display)

        self.playerSpriteGroup.update()
        self.playerSpriteGroup.draw(display)

        self.detectPlatformCollision()

        self.detectCoinCollision()





