# pyright: reportMissingTypeStubs=true
#https://opengameart.org/content/tower-defense-300-tilessprites

from typing import List

import pygame

import Base
import Base.ComponentDrawer
import Base.TowerPlacer
import var
from Base.GameComponent import GameComponent
import Components.Tower

#TODO Mapeado
#TODO enemigos
#TODO tower shooting, 
#TODO pathing
#TODO Sistema de colisiones
#TODO hacer que solo se pueda seleccionar una torre de cada vez y que haya más feedback (cambio de color, mostrar radio....) Clase Player(?)

#####
##### HECHOS
#####

#TODO terminar placement de torres y refactorizar a su propia clase
#TODO hacer una clase que dibuje una lista de todos los game_component
#TODO tileset
class Game():

    def __init__(self):

        pygame.init()
        pygame.font.init()
        self.components : List[GameComponent] =[]
        self.window:pygame.Surface = pygame.display.set_mode((var.WIDTH, var.HEIGTH))
        self.setupEvents()
        self.placing:GameComponent # variable en la que se guarda la torre que se está colocando en ese momento
        self.tower_placer = Base.TowerPlacer.TowerPlacer(self.components)
        
        
    def game_loop(self):

        done=False
        clock = pygame.time.Clock()
        #self.tower.rect.move_ip(var.HEIGTH/2,var.WIDTH/2)
        while not done:
            clock.tick(60)
            self.update()
            self.window.fill("#000000")
            #self.window.blit(self.tower.image,self.tower.rect)
            var.component_drawer.draw(self.window)
            pygame.display.flip()

    def update(self):
        for component in self.components:
            component.update()
        var.event_handler.update()
        
   
        
    def setupEvents(self):
        var.event_handler.subscribe(pygame.QUIT,self.exit_game)
        var.keyboard_handler.subscribe(pygame.K_q,self.place_tower)
        
    def place_tower(self,event):
        if(self.tower_placer.place_tower(Components.Tower.Tower(10))):
            print("colocando torre")
        else:
            print("no se puede colocar más de una torre a la vez")
    
    def exit_game(self,event):
        exit()        

if __name__ =="__main__":
    
    

    x = Game()
    x.game_loop()
