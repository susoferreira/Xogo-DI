# pyright: reportMissingTypeStubs=true

from typing import List

import pygame
from pygame import event
from pygame.constants import K_DOWN, K_LEFT, K_UP
from pygame.surfarray import blit_array

import Components.Building as Building
import var
from Base.GameState import GameState


class Game():

    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.window:pygame.Surface = pygame.display.set_mode((var.WIDTH, var.HEIGTH))
        self.Building = Building.BuildingCity("jugador", 3,10000,1)
        self.setupEvents()

    def game_loop(self):
        done=False
        clock = pygame.time.Clock()
        while not done:
            clock.tick(60)
            self.update() 
            self.window.fill("#000000")
            self.event_handler()
            self.window.blit(self.Building.image,self.Building.rect)
            pygame.display.flip()

    def update(self):
        self.Building.update()

    def handle_gamestate(self,game_state: GameState): # gamestate tiene setup() y ondestroy()
        pass

    def setupEvents(self):
        var.keyboard_handler.subscribe(pygame.K_UP,self.printUp)
        var.event_handler.subscribe(pygame.QUIT,exit)

    def event_handler(self):
        var.event_handler.update()

        
        #var.keyboard_handler.sub
        """for event in events:
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key ==K_UP:
                    self.Building.power +=1
                    
            if event.type == pygame.KEYDOWN:
                if event.key ==K_DOWN:
                    self.Building.power -=1
                    if self.Building.max_population <= 0: self.Building.max_population = 1"""

if __name__ =="__main__":
    x = Game()
    x.game_loop()
