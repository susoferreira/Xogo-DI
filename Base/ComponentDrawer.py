from typing import List

from pygame import Surface

from Base.GameComponent import GameComponent


class ComponentDrawer():
    
    class Subscription():
        def __init__(self,component:GameComponent,priority:int):
            self.component: GameComponent =component
            self.priority:int = priority
    
    def __init__(self):
        self.subs: List['ComponentDrawer.Subscription'] = []

    def addComponent(self,component:GameComponent,priority:int):
        sub = self.Subscription(component,priority)
        for subscription in self.subs:
            if sub.component == subscription.component: ## eliminar duplicados
                break;
        else: # si no ha habido ningún break en todo el bucle
            self.subs.append(sub)
            self.subs.sort(key=lambda sub: sub.priority) # sort by priority
        return sub # retornamos la subcripción para poder eliminarla después
    
    def draw(self,screen:Surface):
        for sub in self.subs:
            screen.blit(sub.component.image,sub.component.rect)


    def removeSubscription(self,sub:'ComponentDrawer.Subscription'):
        self.subs.remove(sub)

    def removeComponent(self,component:GameComponent):
        for i, comp in enumerate(self.subs):
            if comp == component:
                self.subs.pop(i)

component_drawer = ComponentDrawer()