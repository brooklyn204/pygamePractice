import pygame

class Platforms:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.rects = []
        self.color = color
    def create(self):
        self.rects.append(pygame.Rect(0,400,400,40))
        self.rects.append(pygame.Rect(450,300,200,40))
        self.rects.append(pygame.Rect(700,320,100,40))
        self.rects.append(pygame.Rect(850,340,100,40))
        self.rects.append(pygame.Rect(1000,360,100,40))
        for i in self.rects:
            pygame.draw.rect(self.canvas,self.color,i)

        print("moving!")