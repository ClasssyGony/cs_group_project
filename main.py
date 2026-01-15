import pygame
from support.button import KEYPAD

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

#Test Button
keypad = KEYPAD(screen)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #Update button                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              AA
    keypad.update(screen,pygame.mouse)

    clock.tick(120)
    
    #Refrest the screen every tick
    pygame.display.update()

pygame.quit()