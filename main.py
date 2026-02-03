import pygame
from support.button import KEYPAD
from support.managingWord import *
from support.homepage import Home, Endpage, Settings, GameOver
from support.reputation import Reputation
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

reputation = Reputation(0)

codedWord, chosenWord = pickWord(wordList, reputation.reputation)

homepage = Home(font, screen)
endPage = Endpage(font, chosenWord, screen)
settingsPage = Settings(font, screen)
gameOverPage = GameOver(font, "none", screen)

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
            codedWord, chosenWord = pickWord(wordList, reputation.reputation)
            keypad.reset()
            lives = 6
            game_state = "game Over"

        hangman.update(screen, lives)

        if win:
            lives = 6
            game_state = "end"
            #Need to pick how much reputatin you get for the word
            rep = 6
            reputation.addRep(rep)
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
        rep = 0 #this is new
        endPage.displayWord(font, chosenWord, screen, rep, reputation.reputation)    #this is different
        state = endPage.update(screen, pygame.mouse,mousePos,pressed)
        keypad.reset()

        if state == "game":
            codedWord, chosenWord = pickWord(wordList, reputation.reputation)
            
            game_state = "game"
        if state == "home":
            game_state = "home"
            codedWord, chosenWord = pickWord(wordList, reputation.reputation)

    if game_state == "settings":
        if settingsPage.update(screen, pygame.mouse,mousePos,pressed) == "home":
            game_state = "home"
    
    if game_state == "game Over":
        gameOverPage.displayWord(font, chosenWord, screen, rep, reputation.reputation)
        state = gameOverPage.update(screen, pygame.mouse, mousePos, pressed)
        keypad.reset()
        if state == "home":
            game_state = "home"
            codedWord, chosenWord = pickWord(wordList, reputation.reputation)
            reputation.reputation = 0





    clock.tick(120)
    
    #Refrest the screen every tick
    pygame.display.update()

pygame.quit()
