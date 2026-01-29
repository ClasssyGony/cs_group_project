import pygame

pygame.init

class HangmanStates:
    def __init__(self):

        life1 = pygame.image.load("HangmanStates/1.png")

        life2 = pygame.image.load("HangmanStates/2.png")

        life3 = pygame.image.load("HangmanStates/3.png")

        life4 = pygame.image.load("HangmanStates/4.png")
        
        life5 = pygame.image.load("HangmanStates/5.png")

        life6 = pygame.image.load("HangmanStates/6.png")

        self.HangmanStates = [life1, life2, life3, life4, life5, life6]

    def update(self,screen,lives):
        for state in range(lives):
            screen.blit(self.HangmanStates[state], (50, 85))