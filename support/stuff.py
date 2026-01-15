#making the word lise
wordList = []
with open("wordlist.txt", 'r') as file:
    wordList = file.read().splitlines()