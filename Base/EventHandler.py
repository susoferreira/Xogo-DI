from typing import Any, List

import pygame
import pygame.constants as const
import pygame.event as event


class EventHandler():# handler para eventos, puede asociar un evento con una función arbitraria

    class Subscription():
        def __init__(self,event:int,func:Any):
            self.event:int = event
            self.func:Any = func


    def __init__(self):
        self.subs:List[EventHandler.Subscription] =[]

    def subscribe(self,event:int,func:"Any") -> 'EventHandler.Subscription':
        #retorna la subscripción para usar self.unsubscribe
        sub = self.Subscription(event,func)
        self.subs.append(sub)
        return sub
        
    def unsubscribe (self,sub:"EventHandler.Subscription"):
        self.subs.remove(sub)

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
        def __init__(self,key:int,func:Any,keydown:bool =True,mod:int = None,one_time=False):
            self.key:int = key
            self.func:Any = func
            self.keydown=keydown
            self.mod = mod
            self.one_time =one_time
    def __init__(self,eventHandler:EventHandler):
        eventHandler.subscribe(const.KEYUP,self.handleKeyUp)
        eventHandler.subscribe(const.KEYDOWN,self.handleKeyDown)
        self.subs:List[KeyboardHandler.Subscription] = []

    def subscribe(self,key:int,func:Any,keydown:bool =True,mod:int = None,one_time=False) ->'KeyboardHandler.Subscription':
        sub = self.Subscription(key,func,keydown,mod)
        self.subs.append(sub)
        return sub
    
    def unsubscribe (self,sub:"KeyboardHandler.Subscription"):
        self.subs.remove(sub)

    def handleKeyUp(self,event:event.Event):
        self.HandleKey(event)

    def handleKeyDown(self,event:event.Event):
        self.HandleKey(event)

    def HandleKey(self,event:event.Event):

        for sub in self.subs:
            if sub.key == event.key: # si coincide la tecla con el evento
                if event.type == const.KEYDOWN and sub.keydown or event.type == const.KEYUP and not sub.keydown:# si coincide el tipo de evento (keydown o keyup)
                    if sub.mod is None:
                        sub.func(event)
                        if sub.one_time: # si one_time es True la subscripción  se elimina después del primer uso
                            self.subs.remove(sub)
                    elif sub.mod is not None and sub.mod == event.mod:
                        sub.func(event)
                        if sub.one_time: # si one_time es True la subscripción  se elimina después del primer uso
                            self.subs.remove(sub)

                    
class MouseHandler():# handler para eventos, puede asociar un evento con una función arbitraria

    class Subscription():
        MODE_MOUSEBUTTONDOWN = pygame.MOUSEBUTTONDOWN  # las constantes son las mismas que las de pygame pero están redefinidas para mejor claridad
        MODE_MOUSEBUTTONUP = pygame.MOUSEBUTTONUP
        MODE_MOUSEMOTION = pygame.MOUSEMOTION
        def __init__(self,rect:pygame.Rect,func:Any,mode:int = pygame.MOUSEBUTTONDOWN,button:int=pygame.BUTTON_LEFT,one_time=False):
            self.button=button
            self.mode = mode
            self.rect = rect
            self.func:Any = func
            self.one_time=one_time

    def __init__(self,eventHandler: EventHandler):
        self.subs:List[MouseHandler.Subscription] = []
        eventHandler.subscribe(const.MOUSEBUTTONDOWN,self.handleMouseClick)
        eventHandler.subscribe(const.MOUSEBUTTONUP,self.handleMouseClick)
        eventHandler.subscribe(const.MOUSEMOTION,self.handleMouseMotion)

    def subscribe(self,rect:pygame.Rect,func:"Any",mode:int = pygame.MOUSEBUTTONDOWN, button:int = pygame.BUTTON_LEFT,one_time=False) ->'MouseHandler.Subscription':
       sub = self.Subscription(rect,func,mode,button,one_time)
       self.subs.append(sub)
       return sub
        
    def unsubscribe (self,sub:"MouseHandler.Subscription"):
        if sub in self.subs:
            print("está")
        else:
            print(sub)
            print(self.subs)
        self.subs.remove(sub)

    def handleMouseClick(self,event:event.Event):#event es MOUSEBUTTONDOWN,MOUSEBUTTONUP
        #si es el tipo de evento buscado Y colisiona con el ratón Y es el botón correcto ejecutar función
        mouse=event.pos       
        for sub in self.subs:
            if sub.mode == event.type: # los valores de sub.mode se corresponden con los valores de event.type
                if sub.rect.collidepoint(mouse):
                    if sub.button == event.button:
                        sub.func(event)
                    if sub.one_time: # si one_time es True la subscripción  se elimina después del primer uso
                        self.subs.remove(sub)
    def handleMouseMotion(self,event:event.Event):
        #si es el tipo de evento buscado Y colisiona con el ratón ejecutar función
        mouse=event.pos       
        for sub in self.subs:
            if sub.mode == event.type: # los valores de sub.mode se corresponden con los valores de event.type
                
                if  sub.rect is None or sub.rect.collidepoint(mouse):
                        sub.func(event)
                        
                        

event_handler = EventHandler()
keyboard_handler= KeyboardHandler(eventHandler=event_handler)
mouse_handler = MouseHandler(eventHandler=event_handler)
