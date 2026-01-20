import pygame
import sys

pygame.init

screen_width, screen_height = 1280,720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Example")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

class HangmanStates:
    def __init__(self):

        life1 = pygame.image.load("HangmanStates/1.png")

        life2 = pygame.image.load("HangmanStates/2.png")

        life3 = pygame.image.load("HangmanStates/3.png")

        life4 = pygame.image.load("HangmanStates/4.png")

        life5 = pygame.image.load("HangmanStates/5.png")

        life6 = pygame.image.load("HangmanStates/6.png")

        self.HangmanStates = [life1, life2, life3, life4, life5, life6]

    def update(self):
        for state in self.HangmanStates:
            screen.blit(state, (50, 85))
            

clock = pygame.time.Clock()
hangman = HangmanStates()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(WHITE)

    #drawing our hangmans starting state
    pygame.draw.rect(screen, BLACK, (500, 25, 25, 400))

    pygame.draw.rect(screen, BLACK, (160, 25, 365, 25))

    pygame.draw.rect(screen, BLACK, (160, 25, 20, 100))
    
    hangman.update()

    pygame.display.flip()

clock.tick(60)

pygame.quit
sys.exit
