import pygame

class HangmanStates:
    def __init__(self):
        self.lives = 0
        self.HangmanStates = []
        for x in range(8,23):
            self.HangmanStates.append(pygame.image.load(f"HangmanStates/{x}.png").convert_alpha())
    def update(self,screen,lives):
        for state in range(lives):
            screen.blit(self.HangmanStates[state], (0, 0))