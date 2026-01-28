import pygame
from support.button import KEYPAD
from support.hangmanstates import BLACK, HangmanStates
from support.managingWord import *
from support.homepage import Home


pygame.init()
pygame.font.init()
width = 1280
height = 720
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True
font = pygame.font.Font("freesansbold.ttf", 32)
keypad = KEYPAD(screen,font)

homepage = Home(font)
hangman = HangmanStates()
game_state = "home"
lives = 6
while running:
    # showing the coded word
    screen.fill("WHITE")

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if game_state == "game":
        displayWord(screen,font)
        userInput = keypad.update(screen,pygame.mouse)

        pygame.draw.rect(screen, BLACK, (500, 25, 25, 400))

        pygame.draw.rect(screen, BLACK, (160, 25, 365, 25))

        pygame.draw.rect(screen, BLACK, (160, 25, 20, 100))

        
        

        codeWord, correct, win, wrong = checkInput(userInput, chosenWord)
        if wrong:
            lives -=1 
        hangman.update(screen, lives)
        #Update button                      
        keypad.update(screen,pygame.mouse)
        #button1.update(screen,pygame.mouse)

        if lives <= 0:
            game_state = "home"

    if game_state == "home":
        if homepage.update(screen,pygame.mouse) == "Start":
            game_state = "game"

    clock.tick(120)
    
    #Refrest the screen every tick
    pygame.display.update()

pygame.quit()
