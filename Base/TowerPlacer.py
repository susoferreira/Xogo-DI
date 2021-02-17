from typing import List
import var
import pygame
from pygame import mouse
from pygame.event import Event

from Base.EventHandler import MouseHandler
from Base.GameComponent import GameComponent
from Components.Tower import Tower


# from game import componentDrawer,mouse_handler,keyboard_handler
class TowerPlacer():
    def __init__(self, components: List[GameComponent]) -> None:
        self.tower: Tower
        self.components = components
        self.sub = "inicializada así"
        self.is_placing: bool = False

    def place_tower(self, tower):
        if self.is_placing: return False
        self.is_placing = True

        self.tower = tower
        self.components.append(self.tower)
        self.tower.sprite.rect.center = mouse.get_pos()
        var.component_drawer.addComponent(self.tower, 0)
        self.tower.selected = True
        print("suscripción antes de crearla:", self.sub)
        self.sub = var.mouse_handler.subscribe(None, self.move_tower_to_mouse, mode=pygame.MOUSEMOTION,
                                               button=None)  # cada vez que se mueva el ratón mover la torre al ratón
        print("suscripción creada:", self.sub)
        # sub = mouse_handler.subscribe(None,partial(self.move_tower_to_mouse,tower),mode=pygame.MOUSEMOTION,button=None) # cada vez que se mueva el ratón mover la torre al ratón
        var.keyboard_handler.subscribe(pygame.K_r, self.finish_placing, one_time=True)

        return True

    def finish_placing(self, event: Event):
        print("suscripción recibida:", self.sub)
        self.tower.selected = False
        var.mouse_handler.unsubscribe(self.sub)
        self.sub = "asdasd"
        self.is_placing = False

    def move_tower_to_mouse(self, event: Event):
        self.tower.rect.center = event.pos
