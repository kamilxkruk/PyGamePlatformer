import pygame


class Player(object):
    def __init__(self):
        self.box_size = 15
        self.position_x = 0
        self.position_y = 0
        self.player_speed = 5.0
        self.rectangle = pygame.Rect(self.position_x, self.position_y, self.box_size, self.box_size)


    def move(self, keys):
        if keys[pygame.K_a] and self.rectangle.left > 0:
            self.rectangle.x -= self.player_speed
        elif keys[pygame.K_d] and self.rectangle.right < 800 - 15:
            self.rectangle.x += self.player_speed

        if keys[pygame.K_w] and self.rectangle.top > 0:
            self.rectangle.y -= self.player_speed
        elif keys[pygame.K_s] and self.rectangle.top < 600 - 30:
            self.rectangle.y += self.player_speed

    def display(self, display):
        # pygame.draw.rect(display, (3, 252, 40), self.rectangle)
        pygame.draw.circle(display,(3,252,40),(self.rectangle.x+15,self.rectangle.y+15),15)
