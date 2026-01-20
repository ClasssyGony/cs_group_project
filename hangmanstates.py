import pygame
import sys

pygame.init

screen_width, screen_height = 1280,720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Example")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(WHITE)

    #drawing our hangmans starting state
    pygame.draw.rect(screen, BLACK, (500, 25, 25, 400))

    pygame.draw.rect(screen, BLACK, (160, 25, 365, 25))

    pygame.draw.rect(screen, BLACK, (160, 25, 20, 100))

    #these are the states that will be added after each wrong guess
    #the first set of coordinates determine the centre then the next number determines the radius of the circle
    pygame.draw.circle(screen, RED, (170, 150), 50)

    pygame.draw.rect(screen, RED, (160, 150, 20, 175))

    #to draw a line you must determine start and then the end positions and the width at the end
    pygame.draw.line(screen, RED, (175, 315), (290, 425), 15)

    pygame.draw.line(screen, RED, (165, 315), (50, 425), 15)

    pygame.draw.line(screen, RED, (175, 210), (295, 250), 15)

    pygame.draw.line(screen, RED, (165, 210), (55, 250), 15)
    
    pygame.display.flip()

    clock.tick(60)

pygame.quit
sys.exit