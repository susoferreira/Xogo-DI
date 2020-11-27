from abc import abstractmethod
from Base.game_component import game_component
from typing import List,Tuple

class Resource():
    #resource types
    FOOD = 1 # for maintaining a population number
    BUILDING_MATERIALS = 2 # for expanding zone population cap and upgrades
    RESEARCH_POINTS = 3 #I+D

    def __init__(self,count: int, type: int):
        self.count = count
        self.type = type

    @classmethod
    def add_resources(cls,res: List["Resource"],res2: List["Resource"]) -> Tuple["Resource","Resource","Resource"]:
        result=(
            Resource(0,Resource.FOOD),
            Resource(0,Resource.BUILDING_MATERIALS),
            Resource(0,Resource.RESEARCH_POINTS),
        )  
        res1_foodCount = sum(r.count for r in res if r.type == Resource.FOOD)
        res1_building = sum(r.count for r in res if r.type == Resource.BUILDING_MATERIALS)
        res1_research = sum(r.count for r in res if r.type == Resource.FOOD)

        res2_foodCount = sum(r.count for r in res2 if r.type == Resource.FOOD)
        res2_building = sum(r.count for r in res2 if r.type == Resource.BUILDING_MATERIALS)
        res2_research = sum(r.count for r in res2 if r.type == Resource.FOOD)

        result[0].count = res1_foodCount+res2_foodCount               
        result[1].count = res1_building+res2_building
        result[2].count = res1_research+res2_research

        return result


class person(): #zones are populated by persons
    
    def __init__(self,attack_power:int, deffense_power:int,count:int):
        self.attack_power = attack_power
        self.deffense_power = deffense_power

        self.count = count
    @abstractmethod
    def getResources(self) -> List["Resource"]:
        pass


class worker(person):
    BASE_WORKER_POWER = 1
    BASE_WORKER_DEFFENSE = 1

    def __init__(self,attack_multiplier,deffense_multiplier):
        self.attack_power = self.BASE_WORKER_POWER * attack_multiplier
        self.deffense_power = self.BASE_WORKER_DEFFENSE * deffense_multiplier


class zone(game_component):

    def __init__(self,owner:Player,population:List[person]):
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


class zone_city(zone):

    def __init__(self):
        super().__init__(self)
    

    def grow(self):
        
