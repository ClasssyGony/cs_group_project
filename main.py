import pygame
from support.button import Button
from support.managingWord import pickWord, checkInput, wordList, display_surface, displayedCodedWord, codedWordRect, displayRealWord

pygame.init()
width = 1280
height = 720
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True

#codedWord, chosenWord = pickWord(wordList)

while running:
    # showing the coded word
    display_surface.fill((255, 255, 255))
    display_surface.blit(displayedCodedWord, codedWordRect)

    # showing the real word
    display_surface.blit(displayRealWord)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #codeWord, correct, win = checkInput(userInput, chosenWord)
    #Update button                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              AA
    #button1.update(screen,pygame.mouse)

    clock.tick(120)
    
    #Refrest the screen every tick
    pygame.display.update()

pygame.quit()
