from typing import List, Tuple
import pygame.event as event
import pygame.constants as const

import pygame

class EventHandler():# handler para eventos, puede asociar un evento con una función arbitraria


    class Subscription():
        def __init__(self,event:event,func:function):
            self.event:int = event
            self.func:function = func

    def subscribe(self,event,func):
        self.subs.append(self.Subscription(event,func))


    def __init__(self):
        self.subs:List[self.Subscription]
    
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
        def __init__(self,key:int,func:function,KEYDOWN=True):
            self.key:int = key
            self.func:function = func
            self.keydown=keydown

        def subscribe(self,key,func):
            self.subs.append(self.Subscription(key,func))

        
    def __init__(self,eventHandler:EventHandler):
        self.EventHandler.subscribe(const.KEYUP,self.HandleKeyUp)
        self.EventHandler.subscribe(const.KEYDOWN,self.HandleKeyDown)
        self.subs:List[self.Subscription]
    
    def handleKeyUp(self,event:event.Event):
        self.handleKey(event)

    def handleKeyDown(self,event:event.Event):
        self.handleKey(event)

    def HandleKey(self,event:event.Event):

        for sub in self.subs:
            if sub.key == event.key:
                ifsu
                sub.func(event)

