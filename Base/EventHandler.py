from typing import Any, List, Tuple
import pygame.event as event
import pygame.constants as const

import pygame

class EventHandler():# handler para eventos, puede asociar un evento con una función arbitraria


    class Subscription():
        def __init__(self,event:int,func:Any):
            self.event:int = event
            self.func:Any = func


    def __init__(self):
        self.subs:List[EventHandler.Subscription] =[]

    def subscribe(self,event:int,func:"Any"):
        self.subs.append(self.Subscription(event,func))
    
    def update(self):
        events = event.get()
        eventTypes = [event.type for event in events]
        for sub in self.subs:
            try:
                sub.func(events[eventTypes.index(sub.event)])
            except ValueError:
                pass


class KeyboardHandler(): # handler solo para los eventos de teclado, se subscribe a eventHandler y recibe solo los eventos de teclado


    class Subscription():
        def __init__(self,key:int,func:Any,keydown:bool =True):
            self.key:int = key
            self.func:Any = func
            self.keydown=keydown
    def __init__(self,eventHandler:EventHandler):
        eventHandler.subscribe(const.KEYUP,self.handleKeyUp)
        eventHandler.subscribe(const.KEYDOWN,self.handleKeyDown)
        self.subs:List[KeyboardHandler.Subscription] = []

    def subscribe(self,key,func):
            self.subs.append(self.Subscription(key,func))

    def handleKeyUp(self,event:event.Event):
        self.HandleKey(event)

    def handleKeyDown(self,event:event.Event):
        self.HandleKey(event)

    def HandleKey(self,event:event.Event):

        for sub in self.subs:
            if sub.key == event.key: # di coincide la tecla con el evento
                if event.type == const.KEYDOWN and sub.keydown or event.type == const.KEYDOWN and not sub.keydown:# si coincide el tipo de evento (keydown o keyup)
                    sub.func(event)

