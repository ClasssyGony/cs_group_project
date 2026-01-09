import pygame

class Button:
    def __init__(self,surface, width, height, colour):
        self.width = width
        self.height = height

        self.button = pygame.draw.rect(surface,colour,(self.width, self.height))

    def update(self,surface):
        surface.blit(self.button)