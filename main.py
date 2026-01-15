import random
import pygame
from support.button import Button

# Makeing the word list
wordList = []
with open("wordlist.txt", 'r') as file:
    wordList = file.read().splitlines()

pygame.init()
width = 1280
height = 720
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True

#Test Button
button1 = Button(screen, 100,100, (255,255,255))

#pick random word
def pickWord(wordList):
    global codedWord
    chosenWord = random.choice(wordList)
    codedWord = ""
    print(chosenWord)
    for i in range(len(chosenWord)):
        codedWord = codedWord + "_"
    return codedWord, chosenWord

# stuff for text
display_surface = pygame.display.set_mode((1280, 730))
codedWord, chosenWord = pickWord(wordList)
font = pygame.font.Font("freesansbold.ttf", 32)
black = 0, 0, 0
white = 255, 255, 255

#setting up code word for display
displayedCodedWord = font.render(' '.join(codedWord), True, black, white)
codedWordRect = displayedCodedWord.get_rect()
codedWordRect.center = (640, 300)

#showing the real word to make it easier
displayRealWord = font.render(chosenWord, True, black, white)
displayReadWordRect = displayRealWord.get_rect()
displayReadWordRect.center = (30, 30)

def checkInput(userInput, chosenWord):
    global codedWord
    correct = False
    for i in range(len(chosenWord)):
        if userInput == chosenWord[i]:
            temp = codedWord[:i] + userInput + codedWord[i+1:]
            codedWord = temp
            correct = True
    
    return codedWord, correct

codedWord, chosenWord = pickWord(wordList)

# codedWord, correct = checkInput(userInput, chosenWord, codedWord)


while running:
    # showing the coded word
    display_surface.fill(white)
    display_surface.blit(displayedCodedWord, codedWordRect)

    # showing the real word
    display_surface.blit(displayRealWord)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    userInput = input("Enter a letter: ")
    codeWord, correct = checkInput(userInput, chosenWord)
    print(' '.join(codeWord))

    #Update button
    button1.update(screen)

    clock.tick(120)
    
    #Refrest the screen every tick
    pygame.display.update()

pygame.quit()