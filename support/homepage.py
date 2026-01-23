import pygame
from support.button import Button

width = 1280
height = 720
screen = pygame.display.set_mode((width, height))


class Home:
    def __init__(self,font):
        self.startButtonPos = [490, 322]
        self.startButtonW = 300
        self.startButtonH = 76
        self.startButton = Button(screen, self.startButtonW, self.startButtonH, (0, 0, 0), self.startButtonPos, "          START",font)


    def update(self,screen,mouse):
        if self.startButton.update(screen,mouse):
            return "Start"
        

class Endpage:
    def __init__(self, font, word):
        self.endButtonPos = [490,300]
        self.endButtonW = 400
        self.endButtonH = 80
        self.endButton = Button(screen, self.endButtonW, self.endButtonH, (0, 0, 0), self.endButtonPos, "Next word", font)
    
    def displayWord(self, font, word):
        self.chosenWord = word

        word = font.render(self.chosenWord, True, (0, 0, 0), (255, 255, 255))
        wordRect = word.get_rect()
        wordRect.center = (490, 200)
        screen.blit(word,wordRect)   

    def update(self, screen, mouse):
        if self.endButton.update(screen, mouse):
            return "next"
    
    def newWord(self, word):
        self.chosenWord = word