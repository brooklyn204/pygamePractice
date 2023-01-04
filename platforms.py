import pygame

class Platforms:
    # Constructor - sets canvas, color, and empty array of rects (platforms)
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.rects = []
        self.color = color

    # Creates the platforms, adds them to the list of rects, and draws them
    def create(self):
        self.rects.append(pygame.Rect(0,400,400,40))
        self.rects.append(pygame.Rect(450,300,200,40))
        self.rects.append(pygame.Rect(700,320,100,40))
        self.rects.append(pygame.Rect(850,340,100,40))
        self.rects.append(pygame.Rect(1000,360,100,40))
        for i in self.rects:
            pygame.draw.rect(self.canvas, self.color, i)

    # Moves each platform in rects forward by the specified amount 
    def move(self, amount):
        for i in self.rects:
            i.move_ip(amount,0)

    # Draw each platform    
    def draw(self):
        for i in self.rects:
            pygame.draw.rect(self.canvas, self.color, i)