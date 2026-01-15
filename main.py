import random
import pygame
from support.button import Button
from support.stuff import wordList
from support.managingWord import pickWord, checkInput

pygame.init()
width = 1280
height = 720
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True

#Test Button
button1 = Button(screen, 100,100, (255,255,255))

#I need to move all this to another file
# stuff for text
display_surface = pygame.display.set_mode((1280, 730))
codedWord, chosenWord = pickWord(wordList)
font = pygame.font.Font("freesansbold.ttf", 32)
black = 0, 0, 0
white = 255, 255, 255

#setting up code word for display
displayedCodedWord = font.render(' '.join(codedWord), True, black, white)
codedWordRect = displayedCodedWord.get_rect()
codedWordRect.center = (750, 125)

#showing the real word to make it easier
displayRealWord = font.render(chosenWord, True, black, white)
displayReadWordRect = displayRealWord.get_rect()
displayReadWordRect.center = (30, 30)


codedWord, chosenWord = pickWord(wordList)


while running:
    # showing the coded word
    display_surface.fill(white)
    display_surface.blit(displayedCodedWord, codedWordRect)

    # showing the real word
    display_surface.blit(displayRealWord)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    

    #codeWord, correct = checkInput(userInput, chosenWord)

    #Update button
    button1.update(screen)

    clock.tick(120)
    
    #Refrest the screen every tick
    pygame.display.update()

pygame.quit()