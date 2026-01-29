import pygame
from support.button import Button


class Home:
    def __init__(self,font, screen):
        self.startButtonPos = [1280/2-450/2, 275]
        self.startButtonW = 450
        self.startButtonH = 74
        self.startButton = Button(screen, self.startButtonW, self.startButtonH, (0, 0, 0), self.startButtonPos, "START",font)
        self.startImage = pygame.image.load("support/assets/mainmenu/3.png")
        self.startRect = self.startImage.get_rect()
        self.startRect.center = self.startButton.rect.center

        self.settingButtonPos = [1280/2-450/2, 375]
        self.settingButtonW = 450
        self.settingButtonH = 74
        self.settingButton = Button(screen, self.settingButtonW, self.settingButtonH, (0, 0, 0), self.settingButtonPos, "SETTINGS", font)
        self.settingImage = pygame.image.load("support/assets/mainmenu/4.png")
        self.settingRect = self.startImage.get_rect()
        self.settingRect.center = self.settingButton.rect.center

        self.quitButtonPos = [1280/2-450/2, 475]
        self.quitButtonW = 450
        self.quitButtonH = 74
        self.quitButton = Button(screen, self.quitButtonW, self.quitButtonH, (0, 0, 0), self.quitButtonPos, "QUIT", font)
        self.quitImage = pygame.image.load("support/assets/mainmenu/5.png")
        self.quitRect = self.quitImage.get_rect()
        self.quitRect.center = self.quitButton.rect.center

        self.homepageImage = pygame.image.load("support/assets/mainmenu/homepage.png")
        self.music = pygame.mixer.music
        self.music.load("support/assets/menuMusic.mp3")
        self.music.play(-1)





    def update(self,screen,mouse,mousePos,pressed):
        
        screen.blit(self.homepageImage,(0,0))
        
        if self.startButton.update(screen, mouse,mousePos, pressed):
            return "Start"
        
        if self.settingButton.update(screen, mouse,mousePos, pressed):
            return 'setts'
        
        if self.quitButton.update(screen, mouse,mousePos, pressed):
            return "quit"
        screen.blit(self.startImage,self.startRect)
        screen.blit(self.settingImage,self.settingRect)
        screen.blit(self.quitImage,self.quitRect)

class Endpage:
    def __init__(self, font, word, screen):
        self.endButtonPos = [490,300]
        self.endButtonW = 200
        self.endButtonH = 40
        self.endButton = Button(screen, self.endButtonW, self.endButtonH, (0, 0, 0), self.endButtonPos, "Next word", font)

        self.homeButtonPos = [10, 10]
        self.homeButtonW = 100
        self.homeButtonH = 30

        self.homeButton = Button(screen, self.homeButtonW, self.endButtonH, (0, 0, 0), self.homeButtonPos, "Home", font)
    
    def displayWord(self, font, word, screen):
        self.chosenWord = word

        word = font.render(self.chosenWord, True, (0, 0, 0), (255, 255, 255))
        wordRect = word.get_rect()
        wordRect.center = (490, 200)
        screen.blit(word,wordRect)   

    def update(self, screen, mouse,mousePos,pressed):
        if self.endButton.update(screen, mouse,mousePos, pressed):
            return "game"
        if self.homeButton.update(screen, mouse,mousePos, pressed):
            return( "home")
        
    def newWord(self, word):
        self.chosenWord = word


class Settings:
    def __init__(self, font, screen):
        self.backButtonPos = [10, 10]
        self.backButtonH = 49
        self.backButtonW = 100
        self.backButton = Button(screen, self.backButtonW, self.backButtonH, (0, 0, 0), self.backButtonPos, "Back", font)
    
    def update(self, screen, mouse,mousePos, pressed):
        if self.backButton.update(screen, mouse,mousePos, pressed):
            return "home"