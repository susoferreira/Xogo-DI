from abc import abstractmethod
from typing import Any, List, Dict, Tuple
from utils import render_text
from pygame.font import Font
import pygame
from pygame.color import Color
from pygame.surface import Surface
from pygame.transform import scale

import var
from Base.AnimatedSprite import AnimatedSprite
from Base.GameComponent import GameComponent



class Building(GameComponent):  # superclase de todos los tipos de zona del juego

    OWNER_PLAYER = "Player"
    OWNER_GAIA = "Gaia"

    def __init__(self, owner: str, population:int, max_population: int,power:float, GROWTH_RATIO: float =0.2): 
        """es la clase base para los distintos edificios del juego

        Args:
        w
            owner (str): id del jugador que controla ese edificio, si es Null es un edificio neutral

            population (int): cantidad de personas que hay en el edificio, posiblemente en el futuro se añadan varios tipos de población:
                mágica: no se pueden reproducir y no generan recursos pero ayudan a conseguir mejoras mágicas
                científica: se pueden reproducir y ayudan a conseguir mejoras científicas, las mejoras científicas son peores que las mágicas pero más consistentes

            power(float): cantidad de "recursos" que tiene un edificio, posiblemente en el futuro se añadan distintos tipos de recursos y la opción de que un edificio se especialice en un recurso en concreto

            max_population (int): cantidad máxima de población en un determinado edificio, con recursos ilimitados

            GROWTH_RATIO (float, optional): ratio de crecimiento de la población cuando hay recursos ilimitados. Defaults to 0.3.
        """

        GameComponent.__init__(self)
        self.power = power
        self.img: pygame.Surface  ## añadir en subclases
        self.GROWTH_RATIO: float = GROWTH_RATIO  # velocidad de crecimiento
        self.population_bonus: float = 1  # bonus a la cantidad máxima de población de una zona
        self.owner = owner  # player/gaia/enemy
        self.population = population  # conjunto de distintos tipos de personas
        self.max_population = int(
            max_population * self.population_bonus)  # máximo de población, usado para calcular el ratio de crecimiento
        self.attack_bonus: float
    
    def update(self):
        pass
        
    """
    @abstractmethod
    def deffend(self):
        # deffend from attack
        pass
    """

    """ modela crecimiento de población real con recursos ilimitados
    def grow_population(self,
                        time_step: float):  # derivada de la ecuación de crecimiento logístico (para modelar el crecimiento de poblaciones)

        for key in self.population.persons:
            count = self.population.persons[key]
            inc = self.GROWTH_RATIO * count * (1 - (count / self.max_population)) * time_step
            
            self.population.persons[key]+= inc
        print("población:",self.population.get_count())
        """
    def grow_population(self, # modela crecimiento de población real con recursos limitados
                    time_step: float):  # derivada de la ecuación de crecimiento logístico (para modelar el crecimiento de poblaciones)

            count = self.population
            time_bias=10 #para hacer el crecimiento más lento
            low_pop_bias=0.001 # para aumentar el crecimiento cuando hay poca población
            max_admisible_pop = self.power/var.POPULATION_RESOURCE_COST
            print(max_admisible_pop,self.population)
            inc = self.GROWTH_RATIO * count * (1 - (count / max_admisible_pop)) * time_step /time_bias +low_pop_bias
            self.population += inc


class BuildingCity(Building):  # Zona de "civiles" TODO terminar
    POP_BONUS = 1.2  # las ciudades tienen más población máxima

    def __init__(self, owner: str, population:int , max_population: int,power:float):
        """edificio que solo puede generar recursos y población

        Args:
            owner (str): id del jugador que controla el edificio
            population (int): población actual de la zona
            max_population (int): población máxima de la zona, con recursos ilimitados y antes de aplicar el bonus de población (BuildingCity.POP_BONUS en este caso)
            power(float): cantidad de "recursos" que tiene un edificio, posiblemente en el futuro se añadan distintos tipos de recursos y la opción de que un edificio se especialice en un recurso en concreto

        """        
        self.population_bonus = BuildingCity.POP_BONUS
        super().__init__(owner, population,int( max_population*BuildingCity.POP_BONUS),power, GROWTH_RATIO=0.5)
        
        self.sprite: AnimatedSprite = AnimatedSprite("assets/test_sprite/desc.json", animation_delay=10,
                                                     pos=(var.WIDTH // 2, var.HEIGTH // 2),scale=5)
        self.rect = self.sprite.rect
        self.image: pygame.Surface = self.get_surface()
        
    def render_population(self) -> Surface:
        txt = f"pop: {int(self.population)}, Power: {self.power}"
        font:Font = pygame.font.SysFont("Cantarell", 20)
        color = Color("#FFFFFF")
        return render_text(txt,font,color)

    def get_surface(self) -> pygame.Surface: # renderiza la población encima del sprites
        font_surface = self.render_population()
        size1 = font_surface.get_size()
        size2 = self.sprite.image.get_rect().size
        final_size = (size1[0] +size2[0],size2[1])
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

    def __init__(self,id:str) -> None:
        self.buildings:List[Building] =[]
        self.id = id
    def own_Building(self,building:Building):
        self.buildings.append(building)
        building.owner=self
