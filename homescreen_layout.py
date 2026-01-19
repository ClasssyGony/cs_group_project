import pygame
import sys

pygame.init

screen_width, screen_height = 1280,720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Example")

WHITE = (255, 255, 255)
RED = (255, 0, 0)

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(WHITE)

    pygame.draw.rect(screen, RED, (200, 50, 880, 150))

    pygame.draw.rect(screen, RED, (350, 250, 580, 100))

    pygame.draw.rect(screen, RED, (350, 400, 580, 100))

    pygame.draw.rect(screen, RED, (450, 550, 380, 100))

    pygame.display.flip()

    clock.tick(60)

pygame.quit
sys.exit