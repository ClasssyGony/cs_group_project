import pygame
from support.button import KEYPAD
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

game_state = "home"


while running:
    # showing the coded word
    screen.fill("WHITE")

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if game_state == "game":
        
        displayWord(screen,font)
        userInput = keypad.update(screen,pygame.mouse)
        
        codeWord, correct, win = checkInput(userInput, chosenWord)
        #Update button                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              AA
        keypad.update(screen,pygame.mouse)
        #button1.update(screen,pygame.mouse)

    if game_state == "home":
        if homepage.update(screen,pygame.mouse) == "Start":
            game_state = "game"

    clock.tick(120)
    
    #Refrest the screen every tick
    pygame.display.update()

pygame.quit()
