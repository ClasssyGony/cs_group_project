import pygame
from support.button import KEYPAD
from support.managingWord import *

pygame.init()
pygame.font.init()
width = 1280
height = 720
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True
font = pygame.font.Font("freesansbold.ttf", 32)
#Test Button
keypad = KEYPAD(screen)


while running:
    # showing the coded word
    displayWord(screen,font)


    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    userInput = keypad.update(screen,pygame.mouse)

    codeWord, correct, win = checkInput(userInput, chosenWord)
    #Update button                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              AA
    keypad.update(screen,pygame.mouse)
    #button1.update(screen,pygame.mouse)

    clock.tick(120)
    
    #Refrest the screen every tick
    pygame.display.update()

pygame.quit()
