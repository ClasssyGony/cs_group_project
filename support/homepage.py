import pygame
from support.button import Button


class Home:
    def __init__(self,font, screen):
        self.startButtonPos = [490, 322]
        self.startButtonW = 300
        self.startButtonH = 76
        self.startButton = Button(screen, self.startButtonW, self.startButtonH, (0, 0, 0), self.startButtonPos, "          START",font)

        self.settingButtonPos = [515, 500]
        self.settingButtonW = 250
        self.settingButtonH = 70
        self.settingButton = Button(screen, self.settingButtonW, self.settingButtonH, (0, 0, 0), self.settingButtonPos, "    SETTINGS", font)


    def update(self,screen,mouse,pressed):
        if self.startButton.update(screen, mouse, pressed)[0]:
            return "Start"
        
        if self.settingButton.update(screen, mouse, pressed)[0]:
            return 'setts'
        

class Endpage:
    def __init__(self, font, word, screen):
        self.endButtonPos = [490,300]
        self.endButtonW = 400
        self.endButtonH = 80
        self.endButton = Button(screen, self.endButtonW, self.endButtonH, (0, 0, 0), self.endButtonPos, "Next word", font)
    
    def displayWord(self, font, word, screen):
        self.chosenWord = word

        word = font.render(self.chosenWord, True, (0, 0, 0), (255, 255, 255))
        wordRect = word.get_rect()
        wordRect.center = (490, 200)
        screen.blit(word,wordRect)   

    def update(self, screen, mouse,pressed):
        if self.endButton.update(screen, mouse, pressed)[0]:
            return "game"
        
    def newWord(self, word):
        self.chosenWord = word


class Settings:
    def __init__(self, font, screen):
        self.backButtonPos = [10, 10]
        self.backButtonH = 49
        self.backButtonW = 100
        self.backButton = Button(screen, self.backButtonW, self.backButtonH, (0, 0, 0), self.backButtonPos, "Back", font)
    
    def update(self, screen, mouse, pressed):
        if self.backButton.update(screen, mouse, pressed)[0]:
            return "home"