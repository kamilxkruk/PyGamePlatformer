import pygame
from settings import *


class Player(object):
    def __init__(self):
        self.position_x = SCREEN_WIDTH / 2 - BOX_SIZE
        self.position_y = SCREEN_HEIGHT / 2 - BOX_SIZE
        self.speed_x = 0
        self.speed_y = 0
        self.acc_x = 0
        self.acc_y = 0
        self.rectangle = pygame.Rect(self.position_x, self.position_y, BOX_SIZE, BOX_SIZE)


    def move(self, keys):
        self.acc_x = 0
        if self.rectangle.top <= SCREEN_HEIGHT - 2 * BOX_SIZE:
            self.acc_y = GRAVITY

        if keys[pygame.K_d]:
            self.acc_x += 0.5
        elif keys[pygame.K_a]:
            self.acc_x -= 0.5

        if keys[pygame.K_w]:
            self.acc_y -= 1

        self.acc_x -= self.speed_x * FRICTION
        self.speed_x += self.acc_x

        self.acc_y -= self.speed_y * FRICTION
        self.speed_y += self.acc_y

        self.rectangle.x += self.speed_x + 0.5 * self.acc_x

        if self.rectangle.top <= SCREEN_HEIGHT - 2 * BOX_SIZE:
            self.rectangle.y += self.speed_y + 0.5 * self.acc_y
        else:
            self.speed_y = 0
            self.acc_y = 0
            self.rectangle.top = SCREEN_HEIGHT - 2 * BOX_SIZE



        # if keys[pygame.K_a] and self.rectangle.left > 0:
        #     self.rectangle.x -= self.player_speed
        # elif keys[pygame.K_d] and self.rectangle.right < 800 - 15:
        #     self.rectangle.x += self.player_speed
        #
        # if keys[pygame.K_w] and self.rectangle.top > 0:
        #     self.rectangle.y -= self.player_speed
        # elif keys[pygame.K_s] and self.rectangle.top < 600 - 30:
        #     self.rectangle.y += self.player_speed

    def display(self, display):
        pygame.draw.circle(display,(3,252,40),(self.rectangle.x+15,self.rectangle.y+15),15)

