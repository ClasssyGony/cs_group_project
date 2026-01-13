import pygame
from support.button import Button

# Makeing the word list
wordList = []
with open("wordlist.txt", 'r') as file:
    input = file.read().splitlines()

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

#Test Button
button1 = Button(screen, 100,100, (255,255,255))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #Update button
    button1.update(screen)

    clock.tick(120)
    
    #Refrest the screen every tick
    pygame.display.update()

pygame.quit()