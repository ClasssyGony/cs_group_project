import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Hanging man")
clock = pygame.time.Clock()
running = True

# button images
#start button
startButton = pygame.image.load("Untitled.jpg").convert_alpha()

#button class
class Button():
    def __init__(self, x, y, image, scale):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale( image, (int(width * scale), int(height * scale)))

    
    def draw(self):
        #draw button
        screen.blit(self.image, (self.rect.x, self.rect.y))

    
    #button instance
startButton = Button(100,100, startButton, 0.5)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    startButton.draw()
    

    clock.tick(120)
    pygame.display.update()

pygame.quit()