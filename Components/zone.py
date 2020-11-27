from abc import abstractmethod
from Base.GameComponent import GameComponent
from typing import List,Tuple

class Resources(): # almacena Recursos


    def __init__(self,food_count:int,building_mat_count:int,reasearch_pts: int):
        self.food_count = food_count
        self.building_mat_count = building_mat_count
        self.research_pts = reasearch_pts
        self.type = type

    def add(self,resources: "Resources") -> "Resources":

        return Resources(self.food_count+resources.food_count,
                        self.building_mat_count+resources.building_mat_count,
                        self.research_pts+resources.research_pts)
        

class Person(): #zones are populated by persons
    
    def __init__(self,attack_power:int, deffense_power:int,count:int):
        self.attack_power = attack_power
        self.deffense_power = deffense_power

        self.count = count
    @abstractmethod
    def getResources(self) -> List["Resource"]:
        pass


class Worker(Person):# tipo de persona que genera recursos
    BASE_WORKER_POWER = 1
    BASE_WORKER_DEFFENSE = 1

    def __init__(self,attack_multiplier,deffense_multiplier):
        self.attack_power = self.BASE_WORKER_POWER * attack_multiplier
        self.deffense_power = self.BASE_WORKER_DEFFENSE * deffense_multiplier


class Zone(GameComponent): # superclase de todos los tipos de zona del juego

    def __init__(self,owner:Player,population:List[Person]):
        self.owner=owner #player/gaia/enemy
        self.population = population

    @abstractmethod
    def deffend(self): 
        #deffend from attack
        pass
    
    @abstractmethod
    def grow(self):
        #grow population
        pass


class ZoneCity(Zone): # Zona de "civiles"

    def __init__(self):
        super().__init__(self)
    

    def grow(self):
        
