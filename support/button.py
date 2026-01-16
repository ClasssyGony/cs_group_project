import pygame

class Button:
    def __init__(self,surface, width, height, colour, pos, value):

        # Setting up Button variables
        self.width = width
        self.height = height
        self.colour = colour
        self.pos =  pos
        self.pressed = False
        self.value = value

        # New instance of Rect with (left, top, width, height)
        self.rect = pygame.Rect(self.pos[0],self.pos[1],self.width,self.height)

        # Drawing the self.rectObject onto the surface with the colour and settings of self.rect
        self.button = pygame.draw.rect(surface,colour,self.rect)

    def checkMouseClick(self,mouse):
        mouseGetPressed = mouse.get_pressed()[0]
        mousePos = mouse.get_pos()
        
        # This is to check if the mouse button was inactive and is now active in the correct defined regions
        if self.pressed == False and mouseGetPressed == True and mousePos[0] > self.pos[0] and mousePos[0] < self.pos[0] + self.width and mousePos[1] > self.pos[1] and mousePos[1] < self.pos[1] + self.height:
            self.pressed = True
            return True

        # This to check if the mouse has moved to inactivity
        if mouseGetPressed == False:
            self.pressed = False

    def update(self,surface,mouse):
        self.button = pygame.draw.rect(surface,self.colour,self.rect)

        # Check if mouse clicked condition has been achived
        if self.checkMouseClick(mouse) and self.pressed != False:
            # Present Output
            return True
        

""" KEYPAD CLASS """
class KEYPAD:
    def __init__(self,surface):
        self.pos = [100,100]
        self.layout = [["Q","W","E","R","T","Y","U","I","O","P"],["A","S","D","F","G","H","J","K","L"],["Z","X","C","V","B","N","M"]]
        self.buttonsize = [50,65]
        self.keypad_rect = [545,205] # [width, height]

        self.buttons = []

        for index, rows in enumerate(self.layout):
            startingPos = [self.pos[0],self.pos[1]+index*(self.buttonsize[1]+5)]
            for index1, letter in enumerate(rows):
                button = Button(surface,self.buttonsize[0],self.buttonsize[1],"Black",(startingPos[0]+index1*(self.buttonsize[0]+5),startingPos[1]),letter)

                self.buttons.append(button)

    def update(self,surface,mouse):
        value = " "
        for button in self.buttons:
            if button.update(surface,mouse):
                if value == " ":
                    value = button.value.lower()
        

        return value


#Changes 14/01/26
# Added comments to explain the class

#Changes 15/1/26
# Added keypad class