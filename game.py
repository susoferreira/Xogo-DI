from graphical_item import graphical_item
import pygame

from game_state import game_state
from typing import List
WIDTH = 400
HEIGTH = 300
class Game():

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIDTH, HEIGTH))
        self.all_sprites = pygame.sprite.Group()
        self.player= graphical_item("assets/test_sprite/desc.json",animation_delay=7, pos=(100,100))
        
        self.all_sprites.add(self.player)
    def game_loop(self):
        done=False
        clock = pygame.time.Clock()
        while not done:
            clock.tick(60)
            self.update()
            self.window.fill((0,0,0))
            self.event_handler(pygame.event.get())
            self.all_sprites.draw(self.window) 
            pygame.display.flip()

    def update(self):

        self.player.scale_by(1.05)
        self.all_sprites.update()

    def handle_gamestate(self,game_state: game_state): # gamestate tiene setup() y ondestroy()
        pass

    def event_handler(self,events:List[ pygame.event.Event]):
        for event in events:
            if event.type == pygame.QUIT:
                exit()

if __name__ =="__main__":
    x = Game()
    x.game_loop()
