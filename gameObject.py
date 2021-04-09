import pygame, sys
from player import Player
from settings import *


class GameObject(object):

    def __init__(self):
        pygame.init()

        self.screenSize = (SCREEN_WIDTH, SCREEN_HEIGHT) #Tuple
        self.display = pygame.display.set_mode(self.screenSize)
        self.display_rect = self.display.get_rect()
        pygame.display.set_caption('First PyGame App')
        self.pyClock = pygame.time.Clock()
        self.gameMode = 0 #0 - menu, 1 - gra, 2 - edit mode
        self.player = Player()
        self.gravity = True

        self.gameMenuRectangle = pygame.Rect(self.display_rect.centerx-100,self.display_rect.top+120,200,50)
        self.editMenuRectangle = pygame.Rect(self.display_rect.centerx-100,self.display_rect.top+220,200,50)
        self.exitMenuRectangle = pygame.Rect(self.display_rect.centerx-100,self.display_rect.top+320,200,50)

    # process game
    def process_game(self):
        while True:
            self.pyClock.tick(FPS)
            self.handle_events()
            self.read_keyboard()
            self.print()

    # handle events
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pass
            elif event.type == pygame.MOUSEBUTTONUP:
                mousePosition = pygame.mouse.get_pos()
                if self.gameMenuRectangle.collidepoint(mousePosition):
                    self.gameMode = 1

                #Jeżeli rectangleGraj koliduje -> gameMode = 1
                #Jeżeli rectangleEdytujPoziom koliduje -> gameMode = 2
                #Jeżeli rectangleWyjdź -> sys.exit(0)


    # read keyboard
    def read_keyboard(self):
        keys = pygame.key.get_pressed()

        if self.gameMode == 1:
            self.player.move(keys)

    def print(self):
        self.display.fill(BLACK)

        if self.gameMode == 0:
            self.print_menu()
        elif self.gameMode == 1:
            self.print_game()

        pygame.display.flip()

    def print_game(self):
        self.player.display(self.display)

    def print_menu(self):
        pygame.draw.rect(self.display,GREY,self.gameMenuRectangle)
        pygame.draw.rect(self.display,GREY,self.editMenuRectangle)
        pygame.draw.rect(self.display,GREY,self.exitMenuRectangle)
