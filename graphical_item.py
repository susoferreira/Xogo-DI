import pygame


class graphical_item(pygame.sprite.Sprite):
    def __init__(self,sprite_route):
        pygame.sprite.Sprite.__init__(self)
        self.image =  pygame.image.load(sprite_route)
        self.rect=self.image.get_rect()
 
    def printasd(self):
        print("asdasadd funciona")
    def update(self):
        self.rect.x+=30
