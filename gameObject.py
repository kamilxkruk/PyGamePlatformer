import pygame, sys
from player import Player


class GameObject(object):

    def __init__(self):
        pygame.init()

        self.screenSize = (800, 600) #Tuple

        self.display = pygame.display.set_mode(self.screenSize)
        pygame.display.set_caption('First PyGame App')
        self.pyClock = pygame.time.Clock()
        self.player = Player()

    # process game
    def process_game(self):
        while True:
            self.pyClock.tick(30)
            self.handle_events()
            self.read_keyboard()
            self.print()

    # handle events
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit(0)

    # read keyboard
    def read_keyboard(self):
        keys = pygame.key.get_pressed()
        self.player.move(keys)

    def print(self):
        self.display.fill((0, 0, 0))
        self.player.display(self.display)
        pygame.display.flip()