import random
import pygame


wordList = []
with open("wordlist.txt", 'r') as file:
    words = file.read().splitlines()
    for word in words:
        wordList.append(word.lower())


#picking the word
def pickWord(wordList, reputation):
    global codedWord
    chosenWord = random.choice(wordList)
    #how reputation affects the game
    if reputation <= 25:
        while len(chosenWord) >= 7:
            chosenWord = random.choice(wordList)
    elif reputation <= 75 and reputation > 25:
        while len(chosenWord) > 10 or len(chosenWord) < 6:
            chosenWord = random.choice(wordList)
    elif reputation <= 150 and reputation > 75:
        while len(chosenWord) > 12 or len(chosenWord) < 8:
            chosenWord = random.choice(wordList)
    elif reputation <= 250 and reputation > 150:
        while len(chosenWord) >= 15 or len(chosenWord) < 10:
            chosenWord = random.choice(wordList)
    elif reputation > 250:
        while len(chosenWord) <= 12:
            chosenWord = random.choice(wordList)
    codedWord = ""
    for i in range(len(chosenWord)):
        codedWord = codedWord + "_"
    return codedWord, chosenWord

#checking user input
def checkInput(userInput, chosenWord):
    global codedWordS
    correct = False
    wrong = False
    for i in range(len(chosenWord)):
        if userInput == chosenWord[i]:
            temp = codedWord[:i] + userInput + codedWord[i+1:]
            codedWord = temp
            correct = True

    if userInput != " " and correct == False:
        wrong = True
    
    
    count = 0
    finished = False
    for i in range(len(chosenWord)):
        if chosenWord[i] == codedWord[i]:
            count = count + 1
    
    if count == len(chosenWord):
        finished = True
    return codedWord, correct, finished, wrong

    

def displayWord(screen,font,chosenWord):
    #setting up code word for display
    displayedCodedWord = font.render(' '.join(codedWord), True, (255, 255, 255))
    codedWordRect = displayedCodedWord.get_rect()
    codedWordRect.center = (750, 125)

    #showing the real word to make it easierS
    #displayRealWord = font.render(chosenWord, True, (0, 0, 0), (255, 255, 255))
    #displayReadWordRect = displayRealWord.get_rect()
    #displayReadWordRect.center = (30, 30)

    #screen.fill((255, 255, 255))
    screen.blit(displayedCodedWord, codedWordRect)
   # screen.blit(displayRealWord)

def getMouseClick(pressed):
    if pygame.mouse.get_pressed()[0] and pressed == False:
        pressed = True
        mousePos = pygame.mouse.get_pos()
        return mousePos, pressed

    if pygame.mouse.get_pressed()[0] == False:
        pressed = False
        return (0,0),pressed
    
    return (0,0), pressed
