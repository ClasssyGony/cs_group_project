import pygame
from support.button import Button

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
    
    #Update button                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              AA
    button1.update(screen,pygame.mouse)

    clock.tick(120)
    
    #Refrest the screen every tick
    pygame.display.update()

pygame.quit()