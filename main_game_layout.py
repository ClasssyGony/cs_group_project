import pygame
import sys

#initialize pygame
pygame.init

#set up the screen
screen_width, screen_height = 1280,720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Example")

#set up the colours
WHITE = (255, 255, 255)
RED = (255, 0, 0)

#set up the clock
clock = pygame.time.Clock()

#main game loop
running = True
while running:
    #handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #clear the screen
    screen.fill(WHITE)

    #draw a red rectangle
    pygame.draw.rect(screen, RED, (25, 25, 550, 400))

    pygame.draw.rect(screen, RED, (650, 125, 320, 120))

    pygame.draw.rect(screen, RED, (100, 500, 1080, 150))

    pygame.draw.rect(screen, RED, (1100, 50, 180, 400))

    #update the display
    pygame.display.flip()

    #cap the frame rate
    clock.tick(60)

#quit pygame
pygame.quit()
sys.exit()
