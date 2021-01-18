from abc import abstractmethod
from typing import Any, List, Dict, Tuple
from pygame.font import Font
import pygame
from pygame.color import Color
from pygame.surface import Surface
from pygame.transform import scale

import var
from Base.AnimatedSprite import AnimatedSprite
from Base.GameComponent import GameComponent


class Resources():  # almacena Recursos

    def __init__(self, food_count: int, building_mat_count: int, reasearch_pts: int):
        self.food_count = food_count
        self.building_mat_count = building_mat_count
        self.research_pts = reasearch_pts

    def add(self, resources: "Resources") -> "Resources":
        return Resources(self.food_count + resources.food_count,
                         self.building_mat_count + resources.building_mat_count,
                         self.research_pts + resources.research_pts)


class Person():  # zones are populated by persons

    def __init__(self, attack_power: int, deffense_power: int, count: float):
        self.attack_power = attack_power
        self.deffense_power = deffense_power
        self.count = count

    @abstractmethod
    def getResources(self) -> Resources:
        pass


class Worker(Person):  # tipo de persona que genera recursos
    BASE_WORKER_POWER = 1
    BASE_WORKER_DEFFENSE = 1

    def __init__(self, count):
        super().__init__(Worker.BASE_WORKER_POWER, Worker.BASE_WORKER_DEFFENSE, count)


class Population():
    POPULATION_TYPES: Dict[Any, float] = {
        Person: 0,
        Worker: 0,
    }

    def __init__(self, pop: List[Person]):
        self.persons = Population.POPULATION_TYPES
        self.add_population(pop)

    def add_population(self, pop: List[Person]):
        for i in pop:
            if type(i) in self.persons:
                self.persons[type(i)] += i.count

    def get_count(self)-> List[int]:
        return [int(j) for _,j in self.persons.items()]

class Zone(GameComponent):  # superclase de todos los tipos de zona del juego

    OWNER_PLAYER = "Player"
    OWNER_GAIA = "Gaia"

    def __init__(self, owner: str, population: Population, max_population: int, GROWTH_RATIO: float = 0.3):
        GameComponent.__init__(self)
        self.img: pygame.Surface  ## añadir en subclases
        self.GROWTH_RATIO: float = GROWTH_RATIO  # velocidad de crecimiento
        self.population_bonus: float = 1  # bonus a la cantidad máxima de población de una zona
        self.owner = owner  # player/gaia/enemy
        self.population = population  # conjunto de distintos tipos de personas
        self.max_population = int(
            max_population * self.population_bonus)  # máximo de población, usado para calcular el ratio de crecimiento
        self.attack_bonus: float
        

    @abstractmethod
    def deffend(self):
        # deffend from attack
        pass

    def grow_population(self,
                        time_step: float):  # derivada de la ecuación de crecimiento logístico (para modelar el crecimiento de poblaciones)

        for key in self.population.persons:
            count = self.population.persons[key]
            self.max_population = self.owner.resources.#el maximo de poblacion depende de los recursos disponibles
            inc = self.GROWTH_RATIO * count * (1 - (count / self.max_population)) * time_step
            
            self.population.persons[key]+= inc
        print("población:",self.population.get_count())
    def update(self):
        if not owner:
            owner=Player(Player.GAIA)
        pass


class ZoneCity(Zone):  # Zona de "civiles" TODO terminar
    POP_BONUS = 1.2  # la población crece más rápido en las Ciudades

    def __init__(self, owner: str, x1: Population, max_population: int):
        self.population_bonus = ZoneCity.POP_BONUS
        super().__init__(owner, population,int( max_population*ZoneCity.POP_BONUS), GROWTH_RATIO=0.7)
        
        self.sprite: AnimatedSprite = AnimatedSprite("assets/test_sprite/desc.json", animation_delay=10,
                                                     pos=(var.WIDTH // 2, var.HEIGTH // 2),scale=5)
        self.rect = self.sprite.rect
        self.image: pygame.Surface = self.get_surface()
        
    def render_text_info(self) -> Surface:
        txt = str(self.population.get_count())
        font:Font = pygame.font.SysFont("Cantarell", 12)
        color = Color("#FFFFFF")
        font_surface = font.render(txt,True,color)

        return font_surface

    def get_surface(self) -> pygame.Surface:
        font_surface = self.render_text_info()
        size1 = font_surface.get_size()
        size2 = self.sprite.image.get_rect().size
        final_size = (size1[0] + size2[0],size1[1]+size2[1])
        obj = pygame.Surface(final_size)
        obj.blit(font_surface,(final_size[0]/2,0))
        obj.blit(self.sprite.image,size1)
        return obj
    def update(self):

        self.sprite.update()
        self.image = self.get_surface()
        self.grow_population(1/var.FRAMERATE)
        super().update()

        
class Player():
    GAIA=1
    HUMAN=2
    def __init__(self,type:int) -> None:
        self.zones:List[Zone] =[]
        self.type=type
        self.resources:Resources 
    def own_zone(zone:Zone):
        self.zones.append(zone)
        zone.owner=self
