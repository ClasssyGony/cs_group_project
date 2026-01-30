import pygame
from support.button import Button
from support.reputation import Reputation


class Home:
    def __init__(self,font, screen):
        self.startButtonPos = [490, 275]
        self.startButtonW = 300
        self.startButtonH = 76
        self.startButton = Button(screen, self.startButtonW, self.startButtonH, (0, 0, 0), self.startButtonPos, "          START",font)

        self.settingButtonPos = [515, 375]
        self.settingButtonW = 250
        self.settingButtonH = 70
        self.settingButton = Button(screen, self.settingButtonW, self.settingButtonH, (0, 0, 0), self.settingButtonPos, "    SETTINGS", font)

        self.quitButtonPos = [547, 465]
        self.quitButtonW = 175
        self.quitButtonH = 60
        self.quitButton = Button(screen, self.quitButtonW, self.quitButtonH, (0, 0, 0), self.quitButtonPos, "     QUIT", font)


    def update(self,screen,mouse,mousePos,pressed):
        if self.startButton.update(screen, mouse,mousePos, pressed):
            return "Start"
        
        if self.settingButton.update(screen, mouse,mousePos, pressed):
            return 'setts'
        
        if self.quitButton.update(screen, mouse,mousePos, pressed):
            return "quit"
        

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
    
    def displayWord(self, font, word, screen, rep, totalRepp): #This changed
        self.chosenWord = word
        self.reputation = rep                   #This changed
        

        word = font.render(self.chosenWord, True, (0, 0, 0), (255, 255, 255))
        wordRect = word.get_rect()
        wordRect.center = (490, 200)
        screen.blit(word,wordRect)# it says this changed but idk why

        #new from here
        d = "Reputation gained: " + str(rep)
        
        t = "Total reputation:  " + str(totalRepp)
        reputation = font.render(d, True, (0, 0, 0), (255, 255, 255))
        reputationRect = reputation.get_rect()
        reputationRect.center = (200, 200)
        screen.blit(reputation, reputationRect)

        totalRep = font.render(t, True, (0, 0, 0), (255, 255, 255))
        totalRepRect = totalRep.get_rect()
        totalRepRect.center = (300, 300)
        screen.blit(totalRep, totalRepRect)
        #to here

        

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
        
#New from here

class GameOver:
    def __init__(self, font, word, screen):
        self.homeButtonPos = [10, 10]
        self.homeButtonW = 100
        self.homeButtonH = 30

        self.homeButton = Button(screen, self.homeButtonW, self.endButtonH, (0, 0, 0), self.homeButtonPos, "Home", font)
    

    def displayWord(self, font, word, screen, rep, totalRepp):
        self.chosenWord = word
        self.reputation = rep
        
        word = font.render(self.chosenWord, True, (0, 0, 0), (255, 255, 255))
        wordRect = word.get_rect()
        wordRect.center = (490, 200)
        screen.blit(word,wordRect)
#
        d = "Reputation gained: " + str(rep)
        
        t = "Total reputation:  " + str(totalRepp)
        reputation = font.render(d, True, (0, 0, 0), (255, 255, 255))
        reputationRect = reputation.get_rect()
        reputationRect.center = (200, 200)
        screen.blit(reputation, reputationRect)

        totalRep = font.render(t, True, (0, 0, 0), (255, 255, 255))
        totalRepRect = totalRep.get_rect()
        totalRepRect.center = (300, 300)
        screen.blit(totalRep, totalRepRect)
        #to here

        

    def update(self, screen, mouse,mousePos,pressed):
        if self.homeButton.update(screen, mouse,mousePos, pressed):
            return( "home")