# pyright: reportMissingTypeStubs=true
# https://opengameart.org/content/tower-defense-300-tilessprites

from Components.Notification import Notification
from Components.Interfaz import Interfaz
from Base.EnemySpawner import EnemySpawner
from Base.AnimatedSprite import AnimatedSprite
from Components.Enemy import Enemy
from Mapping.TiledParser import TileMap
from pygame import Color, Rect, mouse
from typing import List

import pygame
from pygame.event import Event


import Base
import Base.ComponentDrawer
import Base.TowerPlacer
import var
from Base.GameComponent import GameComponent
import Components.Tower as Tower

# TODO enemigos
# TODO tower shooting,
# TODO pathing

#####
# HECHOS
#####

# TODO hacer que solo se pueda seleccionar una torre de cada vez y que haya más feedback (cambio de color, mostrar radio....) Clase Player(?)
# TODO Mapeado
# TODO Sistema de colisiones
# TODO terminar placement de torres y refactorizar a su propia clase
# TODO hacer una clase que dibuje una lista de todos los game_component
# TODO tileset


class Player():
    def __init__(self, power: int) -> None:
        """ used for tower placing"""
        self.current_placing_tower: Tower.Tower = None
        self.is_placing = False
        self.sub_complete_placement = ""
        self.sub_cancel_placement = ""
        self.sub_finish_placement = ""
        var.keyboard_handler.subscribe(pygame.K_ESCAPE,self.unselect_tower)

        """used for tower placing, storing temporal variables"""

        self.tower_cost = 30
        self.towers: List[Tower.Tower] = []
        self.selected_tower: 'Tower.Tower|None' = None
        # cuando haya un click del ratón comprobar
        
        
    def select_tower(self, tower:Tower.Tower,event: Event):
        if self.is_placing:
            return
        if self.selected_tower is not None:  # deseleccionar la torre seleccionada antes de seleccionar otra
            self.selected_tower.is_selected = False
        tower.is_selected = True
        self.selected_tower = tower
        
    def unselect_tower(self,event):
        if self.selected_tower is not None:
            self.selected_tower.is_selected = False
            self.selected_tower = None
        
    def place_tower(self, tower):
        if var.dinero <self.tower_cost:
            Notification(f"No tienes dinero suficiente ({self.tower_cost})")
            return
        if self.is_placing:
            return False
        self.is_placing = True

        self.current_placing_tower = tower
        self.towers.append(self.current_placing_tower)
        self.current_placing_tower.is_placing = True
        self.current_placing_tower.sprite.rect.center = mouse.get_pos()

        self.current_placing_tower.is_selected = True
        self.sub_complete_placement = var.mouse_handler.subscribe(None, self._move_tower_to_mouse, mode=pygame.MOUSEMOTION,
                                                                  button=None)  # cada vez que se mueva el ratón mover la torre al ratón

        self.sub_cancel_placement = var.mouse_handler.subscribe(
            None, self._cancel_placing, mode=pygame.MOUSEBUTTONDOWN, button=pygame.BUTTON_RIGHT)  # click derecho para cancelar placement
        
        self.sub_finish_placement = var.keyboard_handler.subscribe(
            pygame.K_r, self.finish_placing)
        return True

    def finish_placing(self, event: Event):
        if var.collision_handler.is_colliding_with(self.current_placing_tower,"mapa"):
            return
        var.dinero -=self.tower_cost
        tower_tmp = self.current_placing_tower ## hay que usar tower_tmp porque self.current_placing_tower se redefine  y siempre se seleccionaría la ultima torre colocada
        var.mouse_handler.subscribe(self.current_placing_tower.sprite.rect, lambda event: self.select_tower(
            tower_tmp, event))  # cuando haya un click derecho en la torre, seleccionarla
        # (usa una función parcial)
        self.current_placing_tower.is_selected = False
        self._cleanup_placing()

    def _cancel_placing(self,event):
        self.current_placing_tower.kill()
        self._cleanup_placing()        
        self.towers.remove(self.current_placing_tower)
        del self.current_placing_tower

    def _cleanup_placing(self):
        self.is_placing = False
        self.current_placing_tower.is_placing = False
        var.mouse_handler.unsubscribe(self.sub_complete_placement)
        var.mouse_handler.unsubscribe(self.sub_cancel_placement)
        var.keyboard_handler.unsubscribe(self.sub_finish_placement)

    def _move_tower_to_mouse(self, event: Event):
        self.current_placing_tower.sprite.rect.center = event.pos
    def update(self):
        for tower in self.towers:
            tower.update()
            

class Game():

    def __init__(self):
        self.enemy_spawner = EnemySpawner()
        self.components: List[GameComponent] = []
        self.interfaz = Interfaz()
        self.components.append(self.interfaz)
        self.window: pygame.Surface = pygame.display.set_mode(
            (var.WIDTH, var.HEIGTH))
        self.setupEvents()
        self.player = Player(10)
        var.mapa = TileMap("assets/mapas/mapa3.tmx",(48,48))
        var.collision_handler.create_group("mapa")
        var.collision_handler.create_group("enemigos")
        #var.mapa = TileMap("assets/mapas/mapa3.tmx",(48,48)) 
        var.collision_handler.add_item_to_group(var.mapa,"mapa")
        var.component_drawer.addComponent(var.mapa,Rect(0,0,0,0),-10)


    def game_loop(self):

        done = False
        clock = pygame.time.Clock()
        # self.tower.rect.move_ip(var.HEIGTH/2,var.WIDTH/2)
        while not done:
            clock.tick(60)
            var.alpha_frame.fill(Color(0,0,0,0))
            self.update()
            self.window.fill("#30000f")
            var.component_drawer.draw(self.window)
            self.window.blit(var.alpha_frame,(0,0))
            pygame.display.flip()

            
    def update(self):
        for notification in var.notifications:
            if notification.is_deleted:
                var.notifications.remove(notification)
                break
            notification.update()
        if var.game_finished:
            return
        for component in self.components:
            if component.is_deleted:
                self.components.remove(component)
                break
            component.update()
        self.player.update()        
        var.event_handler.update()
        var.collision_handler.update()
        self.enemy_spawner.update()

    def setupEvents(self):
        var.event_handler.subscribe(pygame.QUIT, self.exit_game)
        var.keyboard_handler.subscribe(pygame.K_q, self.place_tower)


    def place_tower(self, event):
        tower = Tower.Tower(10,300,
        AnimatedSprite("assets/sprite_torre/desc.json",10,scale=3,animate=False)
        ,10
        )
        if(not self.player.place_tower(tower)):
            tower.kill()

    def exit_game(self, event):
        exit()


if __name__ == "__main__":

    x = Game()
    x.game_loop()
