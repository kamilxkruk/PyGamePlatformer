import pygame, sys
from player import Player
from levelEditor import LevelEditor
from files import FileManagement
from settings import *


class GameObject(object):

    def __init__(self):
        pygame.init()

        self.windowSize = (WINDOW_WIDTH+1, WINDOW_HEIGHT+1) #Tuple
        self.display = pygame.display.set_mode(self.windowSize)
        self.display_rect = self.display.get_rect()
        pygame.display.set_caption('First PyGame App')
        self.pyClock = pygame.time.Clock()
        self.gameMode = GAMEMODE_MENU #0 - menu, 1 - gra, 2 - edycja poziomu
        self.player = Player()
        self.levelEditor = LevelEditor()
        self.gravity = True

        #Menu buttons
        self.gameMenuRectangle = pygame.Rect(self.display_rect.centerx-100,self.display_rect.top+170,200,50)
        self.editMenuRectangle = pygame.Rect(self.display_rect.centerx-100,self.display_rect.top+270,200,50)
        self.exitMenuRectangle = pygame.Rect(self.display_rect.centerx-100,self.display_rect.top+370,200,50)

        #Menu labels
        self.myMenuFont = pygame.font.SysFont("Times New Roman", 25)
        self.gameLabel = self.myMenuFont.render('Play', 1, WHITE)
        self.gameLabelRect = self.gameLabel.get_rect()
        self.gameLabelRect.center = self.gameMenuRectangle.center
        self.editLabel = self.myMenuFont.render('Level editor', 1, WHITE)
        self.editLabelRect = self.editLabel.get_rect()
        self.editLabelRect.center = self.editMenuRectangle.center
        self.exitLabel = self.myMenuFont.render('Exit', 1, WHITE)
        self.exitLabelRect = self.exitLabel.get_rect()
        self.exitLabelRect.center = self.exitMenuRectangle.center

        #Level editor buttons
        self.saveEditorRectangle = pygame.Rect(175,SCREEN_HEIGHT+20,200,50)
        self.loadEditorRectangle = pygame.Rect(425,SCREEN_HEIGHT+20,200,50)

        self.saveEditorButtonLabel = self.myMenuFont.render('Save', 1, WHITE)
        self.saveEditorButtonLabelRect = self.saveEditorButtonLabel.get_rect()
        self.saveEditorButtonLabelRect.center = self.saveEditorRectangle.center
        self.loadEditorButtonLabel = self.myMenuFont.render('Load', 1, WHITE)
        self.loadEditorButtonLabelRect = self.loadEditorButtonLabel.get_rect()
        self.loadEditorButtonLabelRect.center = self.loadEditorRectangle.center

        #Level editor labels

        self.levelEditorData = [0]*EDITOR_ROWS
        for row in range(len(self.levelEditorData)):
            self.levelEditorData[row] = [0]*EDITOR_COLUMNS


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
                self.gameMode = GAMEMODE_MENU
            elif self.gameMode == GAMEMODE_LEVEL_EDITOR and event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                self.saveLevelEditorDataToFile()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mousePosition = pygame.mouse.get_pos()

                if self.gameMode == GAMEMODE_MENU:
                    if self.gameMenuRectangle.collidepoint(mousePosition):
                        self.gameMode = GAMEMODE_GAME
                        self.player = Player()
                    elif self.editMenuRectangle.collidepoint(mousePosition):
                        self.gameMode = GAMEMODE_LEVEL_EDITOR
                    elif self.exitMenuRectangle.collidepoint(mousePosition):
                        sys.exit(0)

                elif self.gameMode == GAMEMODE_LEVEL_EDITOR:

                    if (mousePosition[0] > 0 and
                        mousePosition[0] < SCREEN_WIDTH and
                        mousePosition[1] > 0 and
                        mousePosition[1] < SCREEN_HEIGHT):

                        xId = mousePosition[0]//TILE_SIZE
                        yId = mousePosition[1]//TILE_SIZE

                        pressedMouseButtons = pygame.mouse.get_pressed(3)

                        if pressedMouseButtons[0]:
                            self.levelEditorData[yId][xId] = (self.levelEditorData[yId][xId] + 1) % (len(TERRAIN_TYPES)+1)
                        elif pressedMouseButtons[2]:
                            self.levelEditorData[yId][xId] = 0

                    elif self.saveEditorRectangle.collidepoint(mousePosition):
                        self.saveLevelEditorDataToFile()

                    elif self.loadEditorRectangle.collidepoint(mousePosition):
                        self.loadLevelEditorDataFromFile()

            elif event.type == pygame.MOUSEWHEEL and self.gameMode == GAMEMODE_LEVEL_EDITOR:
                print('x: ',event.x,'y:',event.y)
                self.levelEditorData[yId][xId] = (self.levelEditorData[yId][xId] + event.y)
                if self.levelEditorData[yId][xId] > len(TERRAIN_TYPES):
                    self.levelEditorData[yId][xId] = 0
                elif self.levelEditorData[yId][xId] < 0:
                    self.levelEditorData[yId][xId] = len(TERRAIN_TYPES)

    # read keyboard
    def read_keyboard(self):
        keys = pygame.key.get_pressed()

        if self.gameMode == GAMEMODE_GAME:
            self.player.move(keys)

    def print(self):
        self.display.fill(BLACK)

        if self.gameMode == GAMEMODE_MENU:
            self.print_menu()
        elif self.gameMode == GAMEMODE_GAME:
            self.print_game()
        elif self.gameMode == GAMEMODE_LEVEL_EDITOR:
            self.print_editor()


        pygame.display.flip()

    def print_game(self):
        self.player.display(self.display)
        pygame.draw.rect(self.display,WHITE,pygame.rect.Rect((0,0),(SCREEN_WIDTH,SCREEN_HEIGHT)),1)

    def print_menu(self):
        pygame.draw.rect(self.display,GRAY,self.gameMenuRectangle)
        pygame.draw.rect(self.display,GRAY,self.editMenuRectangle)
        pygame.draw.rect(self.display,GRAY,self.exitMenuRectangle)
        self.display.blit(self.gameLabel,self.gameLabelRect)
        self.display.blit(self.editLabel,self.editLabelRect)
        self.display.blit(self.exitLabel,self.exitLabelRect)

    def print_editor(self):

        #Draw grid
        for row in range(EDITOR_ROWS+1):
            pygame.draw.line(self.display,WHITE,(0,row*TILE_SIZE),(SCREEN_WIDTH,row*TILE_SIZE))
        for column in range(EDITOR_COLUMNS+1):
            pygame.draw.line(self.display,WHITE,(column*TILE_SIZE,0),(column*TILE_SIZE,SCREEN_HEIGHT))

        #Draw level tiles
        for rowId in range(len(self.levelEditorData)):
            for columnId in range(len(self.levelEditorData[rowId])):
                if self.levelEditorData[rowId][columnId] != 0:
                    self.drawLevelEditorTile(columnId,rowId,self.levelEditorData[rowId][columnId])

        #Draw editor buttons
        pygame.draw.rect(self.display,GRAY,self.saveEditorRectangle)
        pygame.draw.rect(self.display,GRAY,self.loadEditorRectangle)
        self.display.blit(self.saveEditorButtonLabel,self.saveEditorButtonLabelRect)
        self.display.blit(self.loadEditorButtonLabel, self.loadEditorButtonLabelRect)


    def drawLevelEditorTile(self,columnId,rowId,terrainImageId):
        self.display.blit(TERRAIN_GRAPHICS[terrainImageId],(columnId * TILE_SIZE, rowId * TILE_SIZE))

    def saveLevelEditorDataToFile(self):
        fileService = FileManagement()
        fileService.WriteLevelToFile('level1.txt', self.levelEditorData)
        print("Saved!")

    def loadLevelEditorDataFromFile(self):
        fileService = FileManagement()
        self.levelEditorData = fileService.ReadLevelFromFile('level1.txt')
        print('Loaded!')

#Rzeczy do zrobienia:
# 1. Narysować siatkę (grid)
# 2. Stworzyć listę zawierającą status naszych pól na mapie
# 3. Dodać mechanizm podmieniana rodzaju pola po kliknięciu
# 4. Wyświetlanie odpowiednich pól po kliknięciu
# 5. Zapis stanu poziomu do pliku
# 6. Odczyt stanu poziomu z pliku
# 7. Zamiana poziomu w grze na ten z edytora

