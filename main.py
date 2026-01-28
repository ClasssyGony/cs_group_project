import pygame
from support.button import KEYPAD
from support.managingWord import *
from support.homepage import Home, Endpage, Settings

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

while running:
    
    # showing the coded word
    screen.fill("WHITE")

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
   
    if game_state == "game":
        
        displayWord(screen,font,chosenWord)
        userInput, pressed = keypad.update(screen,pygame.mouse,pressed)
        correct = False
        codeWord, correct, win = checkInput(userInput, chosenWord)

        if win:
            game_state = "end"
            pressed = False
            endPage.newWord(chosenWord)

        #Update button
        #button1.update(screen,pygame.mouse)

    if game_state == "home":
        state = homepage.update(screen,pygame.mouse,pressed)
        if state == "Start":
            pressed = False
            game_state = "game"
        if state == "setts":
            pressed = False
            game_state = "settings"


    if game_state == "end":
        pressed = False
        endPage.displayWord(font, chosenWord, screen)
        state = endPage.update(screen, pygame.mouse,pressed)

        if state == "game":
            codedWord, chosenWord = pickWord(wordList)
            pressed = False
            game_state = "game"
        if state == "home":
            pressed = False
            game_state = "home"
            codedWord, chosenWord = pickWord(wordList)

    if game_state == "settings":
        pressed = False
        if settingsPage.update(screen, pygame.mouse,pressed) == "home":
            game_state = "home"



    clock.tick(120)
    
    #Refrest the screen every tick
    pygame.display.update()

pygame.quit()
