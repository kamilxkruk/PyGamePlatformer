import pygame
from pygame.sprite import spritecollide
from settings import *
from sprites.coinSprite import CoinSprite
from sprites.lavaBottomSprite import LavaBottomSprite
from sprites.lavaTopSprite import LavaTopSprite
from sprites.playerSprite import PlayerSprite
from sprites.platformSprite import PlatformSprite
from sprites.monsterSprite import MonsterSprite
from sprites.bulletSprite import BulletSprite
from files import FileManagement
from random import randint


class Player(object):

    def __init__(self):

        self.centerOfScreen = (SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2)
        self.velocity_X = 0
        self.velocity_Y = 0
        self.acc_x = 0
        self.acc_y = 0

        self.directionX = DIRECTION_RIGHT

        self.points = 0

        self.iteration = 0

        #Setting up sprites
        self.playerSprite = PlayerSprite()
        self.playerSpriteGroup = pygame.sprite.Group()
        self.playerSpriteGroup.add(self.playerSprite)

        self.rectangle = self.playerSprite.rect

        self.platformSpriteGroup = pygame.sprite.Group()
        self.coinSpriteGroup = pygame.sprite.Group()
        self.lavaSpriteGroup = pygame.sprite.Group()
        self.monsterSpriteGroup = pygame.sprite.Group()
        self.bulletSpriteGroup = pygame.sprite.Group()


        #Prepare level sprites
        platformsFromFile = FileManagement().ReadLevelFromFile('level1.txt')
        for rowId in range(len(platformsFromFile)):
            for columnId in range(len(platformsFromFile[rowId])):
                tileValue = platformsFromFile[rowId][columnId]
                if tileValue != T_EMPTY[0]:
                    if tileValue in [T_GRASS[0],T_GRASS1[0],T_GRASS2[0],T_DIRT[0],T_STONE[0],T_SAND[0]]:
                        self.platformSpriteGroup.add(PlatformSprite(columnId * TILE_SIZE, rowId * TILE_SIZE,TERRAIN_GRAPHICS[tileValue]))
                    elif tileValue == T_COIN[0]:
                        self.coinSpriteGroup.add(CoinSprite(columnId * TILE_SIZE, rowId * TILE_SIZE))
                    elif tileValue == T_LAVA_TOP[0]:
                        self.lavaSpriteGroup.add(LavaTopSprite(columnId * TILE_SIZE, rowId * TILE_SIZE))
                    elif tileValue == T_LAVA_DEEP[0]:
                        self.lavaSpriteGroup.add(LavaBottomSprite(columnId * TILE_SIZE, rowId * TILE_SIZE))
                    elif tileValue == T_MONSTER[0]:
                        self.monsterSpriteGroup.add(MonsterSprite(columnId * TILE_SIZE, rowId * TILE_SIZE))


        self.myFont = pygame.font.SysFont("Times New Roman", 18)
        self.infoLabel = self.myFont.render('Points: 0',1,WHITE)
        self.infoLabelRect = self.infoLabel.get_rect()
        self.infoLabelRect.topleft = (0,SCREEN_HEIGHT)

        self.endGameFont = pygame.font.SysFont(None,100,bold=True)
        self.endGameLabel = self.endGameFont.render('KONIEC GRY',1,RED)
        self.endGameLabelRect = self.endGameLabel.get_rect()
        self.endGameLabelRect.center = self.centerOfScreen

        self.showEndGameLabel = False


        self.musicPlayer = pygame.mixer.init()
        self.coinSound = pygame.mixer.Sound('../pyGameProject1/sounds/1.mp3')

        self.platformCollision = []


    def move(self, keys):
        self.acc_x = 0
        if self.rectangle.bottom + self.velocity_Y < SCREEN_HEIGHT:
            self.acc_y = GRAVITY
        else:
            self.velocity_Y = 0
            self.acc_y = 0
            self.rectangle.bottom = SCREEN_HEIGHT

        if keys[pygame.K_d]:
            self.acc_x = 1.5
            self.directionX = DIRECTION_RIGHT
        elif keys[pygame.K_a]:
            self.acc_x = -1.5
            self.directionX = DIRECTION_LEFT

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

        for bullet in self.bulletSpriteGroup:
            bullet.updateBullet()

    def shoot(self):
        self.bulletSpriteGroup.add(BulletSprite(self.directionX,self.playerSprite.rect))

    def moveMonsters(self):
        for monster in self.monsterSpriteGroup:
            monster.move()


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

    def detectLavaCollision(self):
        playerWithLavaCollision = spritecollide(self.playerSprite,self.lavaSpriteGroup,False)
        if playerWithLavaCollision:
            self.playerSprite.kill()

            self.showEndGameLabel = True

    def detectBulletCollision(self):
        for monster in self.monsterSpriteGroup:
            if pygame.sprite.spritecollide(monster,self.bulletSpriteGroup,True):
                if monster.lives > 1:
                    monster.lives -= 1
                else:
                    self.monsterSpriteGroup.remove(monster)



    def display(self, display: pygame.Surface):
        display.blit(self.infoLabel,self.infoLabelRect)
        if self.showEndGameLabel:
            display.blit(self.endGameLabel,self.endGameLabelRect)

        if not self.showEndGameLabel:
            self.platformSpriteGroup.update()
            self.platformSpriteGroup.draw(display)

            self.coinSpriteGroup.update()
            self.coinSpriteGroup.draw(display)

            self.lavaSpriteGroup.update()
            self.lavaSpriteGroup.draw(display)

            self.playerSpriteGroup.update()
            self.playerSpriteGroup.draw(display)

            self.monsterSpriteGroup.update()
            self.monsterSpriteGroup.draw(display)

            self.bulletSpriteGroup.update()
            self.bulletSpriteGroup.draw(display)

            self.detectPlatformCollision()
            self.detectCoinCollision()
            self.detectLavaCollision()
            self.detectBulletCollision()







