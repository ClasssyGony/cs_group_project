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
        
