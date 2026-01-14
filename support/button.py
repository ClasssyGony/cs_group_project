import pygame

class Button:
    def __init__(self,surface, width, height, colour):
        self.width = width
        self.height = height
        self.colour = colour
        self.pos =  [500,500]
        self.pressed = False

        self.button = pygame.draw.rect(surface,colour,(self.pos[0],self.pos[1],self.width, self.height))

    def checkMouseClick(self,mouse):
        mouseGetPressed = mouse.get_pressed()[0]
        mousePos = mouse.get_pos()
        
        if self.pressed == False and mouseGetPressed == True and mousePos[0] > self.pos[0] and mousePos[0] < self.pos[0] + self.width and mousePos[1] > self.pos[1] and mousePos[1] < self.pos[1] + self.height:
            self.pressed = True
            return True

        if mouseGetPressed == False:
            self.pressed = False

    def update(self,surface,mouse):
        self.button = pygame.draw.rect(surface,self.colour,(500,500,self.width, self.height))

        if self.checkMouseClick(mouse) and self.pressed != False:
            print("Click")