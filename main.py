import pygame
from support.button import KEYPAD
from support.managingWord import *
from support.homepage import Home, Endpage, Settings
from support.hangmanstates import HangmanStates

pygame.init()
pygame.font.init()
width = 1280
height = 720
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True
font = pygame.font.Font("freesansbold.ttf", 32)
keypad = KEYPAD(screen,font)

game_state = "home"

codedWord, chosenWord = pickWord(wordList)

homepage = Home(font, screen)
endPage = Endpage(font, chosenWord, screen)
settingsPage = Settings(font, screen)

pressed = False

hangman = HangmanStates()
lives = 6

while running:
    
    # showing the coded word
    screen.fill("WHITE")

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
   
    mousePos, pressed = getMouseClick(pressed)

    if game_state == "game":
        
        displayWord(screen,font,chosenWord)
        userInput = keypad.update(screen,pygame.mouse,mousePos,pressed)
        correct = False
        codeWord, correct, win, wrong = checkInput(userInput, chosenWord)

        pygame.draw.rect(screen, "black", (500, 25, 25, 400))

        pygame.draw.rect(screen, "black", (160, 25, 365, 25))

        pygame.draw.rect(screen, "black", (160, 25, 20, 100))

        if wrong == True:
            lives -= 1

        if lives <= 0:
            lives = 6
            game_state = "home"

        hangman.update(screen, lives)

        if win:
            lives = 6
            game_state = "end"
            endPage.newWord(chosenWord)

    if game_state == "home":
        state = homepage.update(screen,pygame.mouse,mousePos,pressed)
        if state == "Start":
            game_state = "game"
        if state == "setts":
            game_state = "settings"
        if state == "quit":
            running = False


    if game_state == "end":
        endPage.displayWord(font, chosenWord, screen)
        state = endPage.update(screen, pygame.mouse,mousePos,pressed)

        if state == "game":
            codedWord, chosenWord = pickWord(wordList)
            game_state = "game"
        if state == "home":
            game_state = "home"
            codedWord, chosenWord = pickWord(wordList)

    if game_state == "settings":
        if settingsPage.update(screen, pygame.mouse,mousePos,pressed) == "home":
            game_state = "home"



    clock.tick(120)
    
    #Refrest the screen every tick
    pygame.display.update()

pygame.quit()
