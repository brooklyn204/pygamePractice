import os, sys, pygame

pygame.init()
pygame.display.set_caption("Mountains Game")
canvas = pygame.display.set_mode((1000,500))
image = pygame.image.load("mountains.jpg")
image = pygame.transform.scale(image,(1000,500))
canvas.blit(image,[0,0])
pygame.display.update()
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True