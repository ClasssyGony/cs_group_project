import pygame
from support.managingWord import getMouseClick

class Button:
    def __init__(self,surface, width, height, colour, pos, value, font):

        # Setting up Button variables
        self.width = width
        self.height = height
        self.colour = colour
        self.pos =  pos
        self.value = value
        self.font = font

        # New instance of Rect with (left, top, width, height)
        self.rect = pygame.Rect(self.pos[0],self.pos[1],self.width,self.height)
        self.text = font.render(f"{value}", True, (255, 255, 255))
        self.textRect = self.text.get_rect()
        self.textRect.center = self.rect.center

        # Drawing the self.rectObject onto the surface with the colour and settings of self.rect
        self.button = pygame.draw.rect(surface,colour,self.rect)

    def checkMouseClick(self,mouse,mousePos,pressed):
        
        # This is to check if the mouse button was inactive and is now active in the correct defined regions
        if pressed != False and mouse.get_just_pressed()[0] == True and mousePos[0] > self.pos[0] and mousePos[0] < self.pos[0] + self.width and mousePos[1] > self.pos[1] and mousePos[1] < self.pos[1] + self.height:
            return True

        return False

    def update(self,surface,mouse,mousePos,pressed):
        self.button = pygame.draw.rect(surface,self.colour,self.rect)
        surface.blit(self.text, (self.textRect))
        
        # Check if mouse clicked condition has been achived
        i = self.checkMouseClick(mouse,mousePos,pressed)
        if i and pressed != False:
            # Present Output
            return True
        return False
    

""" KEYPAD CLASS """
class KEYPAD:
    def __init__(self,surface,font):
        self.pos = [367,500]
        self.layout = [["Q","W","E","R","T","Y","U","I","O","P"],["A","S","D","F","G","H","J","K","L"],["Z","X","C","V","B","N","M"]]
        self.buttonsize = [50,65]
        self.keypad_rect = [545,205] # [width, height]
        self.font = font
        self.colour = "black"
        self.buttons = []
        self.unavalible = []

        for index, rows in enumerate(self.layout):
            startingPos = [self.pos[0],self.pos[1]+index*(self.buttonsize[1]+5)]
            for index1, letter in enumerate(rows):
                xpos = startingPos[0]+index1*(self.buttonsize[0]+5)
                if index == 1:
                    xpos = startingPos[0]+index1*(self.buttonsize[0]+5)+30
                if index == 2:
                    xpos = startingPos[0]+index1*(self.buttonsize[0]+5) + 85
                button = Button(surface,
                                self.buttonsize[0],
                                self.buttonsize[1],
                                self.colour,
                                (xpos,startingPos[1]),
                                letter,
                                font)

                self.buttons.append(button)

    def reset(self):
        for button in self.buttons:
            button.colour = "black"
        self.unavalible = []

    def update(self,surface,mouse,mousePos,pressed):
        value = " "
        for button in self.buttons:
            valid = True
            i = button.update(surface,mouse,mousePos,pressed)
            for letter in self.unavalible:
                
                if letter == button.value:
                    button.colour = "grey"
                    valid = False
        
            if i and valid:
                if value == " ":
                    value = button.value.lower()
                    self.unavalible.append(value.upper())

        return value


#Changes 14/01/26
# Added comments to explain the class

#Changes 15/1/26
# Added keypad class