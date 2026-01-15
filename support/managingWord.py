import random
import pygame

#word list
wordList = []
with open("wordlist.txt", 'r') as file:
    wordList = file.read().splitlines()

#picking the word
def pickWord(wordList):
    global codedWord
    chosenWord = random.choice(wordList)
    codedWord = ""
    print(chosenWord)
    for i in range(len(chosenWord)):
        codedWord = codedWord + "_"
    return codedWord, chosenWord

#checking user input
def checkInput(userInput, chosenWord):
    global codedWord
    correct = False
    for i in range(len(chosenWord)):
        if userInput == chosenWord[i]:
            temp = codedWord[:i] + userInput + codedWord[i+1:]
            codedWord = temp
            correct = True
    
    return codedWord, correct

#displaying the coded word
# stuff for text
pygame.font.init()





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