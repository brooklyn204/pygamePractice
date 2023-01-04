import pygame, character, platforms

# Constants
WIDTH = 1000
HEIGHT = 500
BACKGROUND = "mountains.jpg"
PLATFORM_COLOR = (30,20,58)
CHARACTER = character.Character("character.png",60,30,0,370)

# Create clock
clock = pygame.time.Clock()

# Create window
pygame.init()
pygame.display.set_caption("Mountains Game")
canvas = pygame.display.set_mode((WIDTH, HEIGHT))

# Add background
background = pygame.image.load(BACKGROUND)
background = pygame.transform.scale(background,(WIDTH,HEIGHT))
canvas.blit(background,[0,0])
pygame.display.update()

# Create platforms
course = platforms.Platforms(canvas,PLATFORM_COLOR)
course.create()

# Add character
character = pygame.image.load(CHARACTER.file)
character = pygame.transform.scale(character,(CHARACTER.width,CHARACTER.height))
canvas.blit(character,[CHARACTER.xpos,CHARACTER.ypos])
pygame.display.update()

# Play game
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            raise SystemExit
    canvas.blit(background,[0,0])
    course.move(-1)
    canvas.blit(character,[CHARACTER.xpos,CHARACTER.ypos])
    pygame.display.flip()
    clock.tick(110)