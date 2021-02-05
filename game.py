# pyright: reportMissingTypeStubs=true
#https://opengameart.org/content/tower-defense-300-tilessprites
from typing import List
#TODO hacer una clase que dibuje una lista de todos los game_component
#TODO place tower, tower shooting, 
import pygame
from pygame import Rect, event
from pygame.constants import K_DOWN, K_LEFT, K_UP
from pygame.surfarray import blit_array
import Components.Building as Building
import var
from Components.Tower import Tower
from Base.GameState import GameState


class Game():

    def __init__(self):
        pygame.init()
        pygame.font.init() 
        self.window:pygame.Surface = pygame.display.set_mode((var.WIDTH, var.HEIGTH))
        self.tower = Tower(10000)
        self.setupEvents()
    def game_loop(self):

        done=False
        clock = pygame.time.Clock()
        self.tower.rect.move_ip(var.HEIGTH/2,var.WIDTH/2)

        while not done:
            clock.tick(60)
            self.update()
            self.window.fill("#000000")
            self.event_handler()
            self.window.blit(self.tower.image,self.tower.rect)
            pygame.display.flip()

    def update(self):
        self.tower.update()
 

    def setupEvents(self):
        var.event_handler.subscribe(pygame.QUIT,exit)
        var.mouse_handler.subscribe(Rect(0,0,var.WIDTH,var.HEIGTH),self.move_tower_to_mouse,mode=pygame.MOUSEMOTION)
        var.keyboard_handler.subscribe(pygame.K_UP,self.addpower)

    def addpower(self,event):
        self.tower.power+=1
    def move_tower_to_mouse(self,event):
        self.tower.rect.center=event.pos


    def event_handler(self):
        var.event_handler.update()

if __name__ =="__main__":
    x = Game()
    x.game_loop()
