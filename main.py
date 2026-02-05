import pygame, random, time
from support.button import KEYPAD
from support.managingWord import *
from support.homepage import Home, Endpage, Settings, GameOver
from support.reputation import Reputation, repPick
from support.hangmanstates import HangmanStates

pygame.init()
pygame.font.init()
width = 1280
height = 720
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True
font = pygame.font.Font("freesansbold.ttf", 32)
keypad = KEYPAD(screen,font)

game_state = "home"

reputation = Reputation(0)

codedWord, chosenWord = pickWord(wordList, reputation.reputation)

homepage = Home(font, screen)
endPage = Endpage(font, chosenWord, screen)
settingsPage = Settings(font, screen)
gameOverPage = GameOver(font, "none", screen)

pressed = False
show_jumpscare = False
hangman = HangmanStates()
lives = 15
cum = pygame.image.load("HangmanStates/7.png").convert_alpha()
level1 = pygame.image.load("support/assets/levels/1.png").convert_alpha()
scream1= pygame.mixer.Sound("support/assets/jumpscare/scream1.mp3")
jump1 = [pygame.image.load("support/assets/jumpscare/jump1.png").convert_alpha(),pygame.image.load("support/assets/jumpscare/4.png").convert_alpha(),pygame.image.load("support/assets/jumpscare/5.png").convert_alpha()]

while running:
    
    screen.fill("WHITE")
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
   
    mousePos, pressed = getMouseClick(pressed)

    if game_state == "game":
        screen.blit(level1,(0,0))
        displayWord(screen,font,chosenWord)
        userInput = keypad.update(screen,pygame.mouse,mousePos,pressed)
        correct = False
        codeWord, correct, win, wrong = checkInput(userInput, chosenWord)
        screen.blit(cum, (0,0))        

        if wrong == True:
            lives -= 1 
            #if random.randint(1) == 2:
            scream1.play()
            show_jumpscare = True
            jumpscare_start_time = pygame.time.get_ticks()

        # Show jumpscare
        if show_jumpscare:
            screen.blit(random.choice(jump1), (0, 0))
            # Check time passed
            if pygame.time.get_ticks() - jumpscare_start_time > 60:
                show_jumpscare = False
                

        
        if lives <= 0:
            w = chosenWord
            codedWord, chosenWord = pickWord(wordList, reputation.reputation)
            keypad.reset()
            lives = 15
            game_state = "game Over"


        hangman.update(screen, lives)

        if win:
            lives = 15
            game_state = "end"
            rep = repPick(chosenWord)
            reputation.addRep(rep)
            endPage.newWord(chosenWord)

    if game_state == "home":
        state = homepage.update(screen,pygame.mouse,mousePos,pressed)
        if state == "Start":
            game_state = "game"
        elif state == "setts":
            game_state = "settings"
        elif state == "quit":
            running = False
        

    if game_state == "end":
        
        endPage.displayWord(font, chosenWord, screen, rep, reputation.reputation)    #this is different
        state = endPage.update(screen, pygame.mouse,mousePos,pressed)
        keypad.reset()

        if state == "game":
            codedWord, chosenWord = pickWord(wordList, reputation.reputation)
            
            game_state = "game"
        elif state == "home":
            game_state = "home"
            codedWord, chosenWord = pickWord(wordList, reputation.reputation)

    if game_state == "settings":
        if settingsPage.update(screen, pygame.mouse,mousePos,pressed) == "home":
            game_state = "home"
    
    if game_state == "game Over":
        gameOverPage.displayWord(font, w, screen, reputation.reputation)
        state = gameOverPage.update(screen, pygame.mouse, mousePos, pressed)
        keypad.reset()
        if state == "home":
            game_state = "home"
            codedWord, chosenWord = pickWord(wordList, reputation.reputation)
            reputation.reputation = 0


    clock.tick(120)
    
    #Refrest the screen every tick
    pygame.display.update()

pygame.quit()