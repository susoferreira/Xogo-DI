import pygame
from  graphical_item import graphical_item
pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False

all_sprites = pygame.sprite.Group()
player = graphical_item("./placeholder1.png")
all_sprites.add(player)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        
                # Add this somewhere after the event pumping and before the display.flip()
        all_sprites.draw(screen)
        pygame.display.flip()
    