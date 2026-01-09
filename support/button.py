import pygame

class Button:
    def __init__(self,surface, width, height, colour):
        self.width = width
        self.height = height
        self.colour = colour

        self.button = pygame.draw.rect(surface,colour,(500,500,self.width, self.height))

    def update(self,surface):
        self.button = pygame.draw.rect(surface,self.colour,(500,500,self.width, self.height))