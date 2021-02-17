from game import Game
from typing import Any, List

import pygame
import pygame.constants as const
import pygame.event as event
import Base.GameComponent


class EventHandler():  # handler para eventos, puede asociar un evento con una función arbitraria

    class Subscription():
        def __init__(self, event: int, func: Any):
            self.event: int = event
            self.func: Any = func

    def __init__(self):
        self.subs: List[EventHandler.Subscription] = []

    def subscribe(self, event: int, func: "Any") -> 'EventHandler.Subscription':
        # retorna la subscripción para usar self.unsubscribe
        sub = self.Subscription(event, func)
        self.subs.append(sub)
        return sub

    def unsubscribe(self, sub: "EventHandler.Subscription"):
        self.subs.remove(sub)

    def update(self):
        events = event.get()
        eventTypes = [event.type for event in events]
        for sub in self.subs:
            try:
                sub.func(events[eventTypes.index(sub.event)])
            except ValueError:
                pass


class KeyboardHandler():
    """handler solo para los eventos de teclado, se subscribe a eventHandler y recibe solo los eventos de teclado"""

    class Subscription():
        def __init__(self, key: int, func: Any, keydown: bool = True, mod: int = None, one_time=False):
            self.key: int = key
            self.func: Any = func
            self.keydown = keydown
            self.mod = mod
            self.one_time = one_time

    def __init__(self, eventHandler: EventHandler):
        eventHandler.subscribe(const.KEYUP, self.handleKey)
        eventHandler.subscribe(const.KEYDOWN, self.handleKey)
        self.subs: List[KeyboardHandler.Subscription] = []

    def subscribe(self, key: int, func: Any, keydown: bool = True, mod: int = None, one_time=False) -> 'KeyboardHandler.Subscription':
        sub = self.Subscription(key, func, keydown, mod)
        self.subs.append(sub)
        return sub

    def unsubscribe(self, sub: "KeyboardHandler.Subscription"):
        self.subs.remove(sub)

    def handleKey(self, event: event.Event):

        for sub in self.subs:
            if sub.key == event.key:  # si coincide la tecla con el evento
                # si coincide el tipo de evento (keydown o keyup)
                if event.type == const.KEYDOWN and sub.keydown or event.type == const.KEYUP and not sub.keydown:
                    if sub.mod is None:
                        sub.func(event)
                        if sub.one_time:  # si one_time es True la subscripción  se elimina después del primer uso
                            self.subs.remove(sub)
                    elif sub.mod is not None and sub.mod == event.mod:
                        sub.func(event)
                        if sub.one_time:  # si one_time es True la subscripción  se elimina después del primer uso
                            self.subs.remove(sub)


class MouseHandler():
    """ handler para eventos, puede asociar un evento con una función arbitraria"""

    class Subscription():
        # las constantes son las mismas que las de pygame pero están redefinidas para mejor claridad
        MODE_MOUSEBUTTONDOWN = pygame.MOUSEBUTTONDOWN
        MODE_MOUSEBUTTONUP = pygame.MOUSEBUTTONUP
        MODE_MOUSEMOTION = pygame.MOUSEMOTION

        def __init__(self, rect: pygame.Rect, func: Any, mode: int = pygame.MOUSEBUTTONDOWN, button: int = pygame.BUTTON_LEFT, one_time=False):
            self.button = button
            self.mode = mode
            self.rect = rect
            self.func: Any = func
            self.one_time = one_time

    def __init__(self, eventHandler: EventHandler):
        self.subs: List[MouseHandler.Subscription] = []
        eventHandler.subscribe(const.MOUSEBUTTONDOWN, self.handleMouseClick)
        eventHandler.subscribe(const.MOUSEBUTTONUP, self.handleMouseClick)
        eventHandler.subscribe(const.MOUSEMOTION, self.handleMouseMotion)

    def subscribe(self, rect: pygame.Rect, func: "Any", mode: int = pygame.MOUSEBUTTONDOWN, button: int = pygame.BUTTON_LEFT, one_time=False) -> 'MouseHandler.Subscription':
        sub = self.Subscription(rect, func, mode, button, one_time)
        self.subs.append(sub)
        return sub

    def unsubscribe(self, sub: "MouseHandler.Subscription"):
        if sub in self.subs:
            print("está")
        else:
            print(sub)
            print(self.subs)
        self.subs.remove(sub)

    # event es MOUSEBUTTONDOWN,MOUSEBUTTONUP
    def handleMouseClick(self, event: event.Event):
        # si es el tipo de evento buscado Y colisiona con el ratón Y es el botón correcto ejecutar función
        mouse = event.pos
        for sub in self.subs:
            if sub.mode == event.type:  # los valores de sub.mode se corresponden con los valores de event.type
                if sub.rect.collidepoint(mouse):
                    if sub.button == event.button:
                        sub.func(event)
                    if sub.one_time:  # si one_time es True la subscripción  se elimina después del primer uso
                        self.subs.remove(sub)

    def handleMouseMotion(self, event: event.Event):
        # si es el tipo de evento buscado Y colisiona con el ratón ejecutar función
        mouse = event.pos
        for sub in self.subs:
            if sub.mode == event.type:  # los valores de sub.mode se corresponden con los valores de event.type

                if sub.rect is None or sub.rect.collidepoint(mouse):
                    sub.func(event)



# colisiones:
# torres ->mapa
# balas ->enemigos
# solución:
#   crear dos arrays de rects y comprobar si la torre colisiona con alguno
#
#   en update() de las balas comprobar si el proyectil colisiona con algún enemigo

class CollisionHandler():  # handler para eventos, puede asociar un evento con una función arbitraria
    """
        Objeto que guarda los distintos grupos de objetos y facilita comprobar colisiones entre grupos
    """    
    class Group():

        def __init__(self, name: str) -> None:
            """  
            IMPORTANTE: NO USAR EL CONSTRUCTOR DIRECTAMENTE, USAR EL MÉTODO CollisionHandler.create_group()

            Args:
                name (str): nombre del grupo
            """
            self.name = name
            self.items: List[Base.GameComponent.GameComponent]
            
    def __init__(self):
        self.groups: List[CollisionHandler.Group] = []

    def add_item_to_group(self, item: Base.GameComponent.GameComponent, group_name: str):
        """Añade un GameComponent a un  grupo de colisión

        Args:
            item (Base.GameComponent.GameComponent): objeto que queremos añadir
            group_name (str): Nombre del grupo al que lo queremos añadir

        Raises:
            Exception: Si el grupo al que lo queremos añadir no existe
        """
        group: CollisionHandler.Group
        for g in self.groups:
            if g.name == group_name:
                group = g
                break
        else:
            raise Exception("El Grupo "+group_name+" no existe")
        g.items.append(item)

    def is_colliding_with(self,component:Base.GameComponent.GameComponent,group_name:str) -> bool:
        """calcula si un componente está colisionando con un grupo de colisiones

        Args:
            component (Base.GameComponent.GameComponent): componente
            group_name (str): grupo para comprobar

        Returns:
            bool:
        """
        if self.collide_with(component,group_name) !=-1:
            return True
        return False
        
    def collide_with(self,component:Base.GameComponent.GameComponent,group_name:str) -> "Base.GameComponent.GameComponent | None":
        """calcula y retorna el primer componente de un grupo con el esté colisionando un componente 

        Args:
            component (Base.GameComponent.GameComponent): componente
            group_name (str): grupo para comprobar la colisión

        Returns:
            Base.GameComponent.GameComponent: el primer componente del grupo elegido con el que se detecte la colisión
        """
        group = self.find_group_by_name(group_name)
        if group:
            for item in group.items:
                for rect in component.rect:
                    rect.collidelist(item.rect)
                    return component
        return None
    def create_group(self, group_name: str):

        if self.find_group_by_name(group_name):
            raise Exception("El grupo "+group_name+" ya existe ")
        
        self.groups.append(self.Group(group_name))
        
    def find_group_by_name(self,group_name:str) ->'CollisionHandler.Group | None':
        for group in self.groups:
            if group.name == group_name:
                return group
        return None
    
    def remove_item(self, item: Base.GameComponent.GameComponent, group_name: str):
        group = self.find_group_by_name(group_name)
        group.items.remove(item)
        
    def remove_group(self,group_name:str):
        if self.find_group_by_name(group_name):
            self.groups.remove(self.find_group_by_name(group_name))
    def remove_all(self):
        self.groups=[]

event_handler = EventHandler()
keyboard_handler = KeyboardHandler(eventHandler=event_handler)
mouse_handler = MouseHandler(eventHandler=event_handler)

collision_handler = CollisionHandler()
