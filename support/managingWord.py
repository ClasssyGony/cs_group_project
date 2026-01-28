import random
import pygame
import time

#word list
wordList = []
with open("wordlist.txt", 'r') as file:
    words = file.read().splitlines()
    for word in words:
        wordList.append(word.lower())

    


#picking the word
def pickWord(wordList):
    global codedWord
    chosenWord = random.choice(wordList)
    codedWord = ""
   # print(chosenWord)
    for i in range(len(chosenWord)):
        codedWord = codedWord + "_"
    return codedWord, chosenWord

#checking user input
def checkInput(userInput, chosenWord):
    global codedWord
    correct = False
    wrong = False
    for i in range(len(chosenWord)):
        if userInput == chosenWord[i]:
            temp = codedWord[:i] + userInput + codedWord[i+1:]
            codedWord = temp
            correct = True
    
    if userInput != " " and correct == False:
        wrong = True

    #Checking weather the user has won the game
    count = 0
    finished = False
    for i in range(len(chosenWord)):
        if chosenWord[i] == codedWord[i]:
            count = count + 1
    
    if count == len(chosenWord):
        finished = True

    return codedWord, correct, finished, wrong

codedWord, chosenWord = pickWord(wordList)
    

def displayWord(screen,font):
    #setting up code word for display
    displayedCodedWord = font.render(' '.join(codedWord), True, (0, 0, 0), (255, 255, 255))
    codedWordRect = displayedCodedWord.get_rect()
    codedWordRect.center = (750, 125)

    #showing the real word to make it easier
    displayRealWord = font.render(chosenWord, True, (0, 0, 0), (255, 255, 255))
    displayReadWordRect = displayRealWord.get_rect()
    displayReadWordRect.center = (30, 30)

    screen.fill((255, 255, 255))
    screen.blit(displayedCodedWord, codedWordRect)
    screen.blit(displayRealWord)
