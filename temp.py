import random

wordList = []
with open("wordlist.txt", 'r') as file:
    wordList = file.read().splitlines()


def pickWord(wordList):
    chosenWord = random.choice(wordList)
    codedWord = ""
    for i in range(len(chosenWord)):
        codedWord = codedWord + "_ "
    return codedWord, chosenWord

def checkInput(userInput, chosenWord, codedWord):
    correct = False
    for i in range(0, len(chosenWord), 1):
        if userInput == chosenWord[i]:
            temp = codedWord[:i] + userInput + codedWord[i+1:]
            codedWord = temp
            correct = True
    
    return codedWord, correct

codedWord, chosenWord = pickWord(wordList)

print(codedWord, chosenWord)
userInput = input()

codedWord, correct = checkInput(userInput, chosenWord, codedWord)

print(f"the coded word is\n{codedWord}\nand you got that letter {correct}")