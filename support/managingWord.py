import random
import pygame
from support.stuff import wordList

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

