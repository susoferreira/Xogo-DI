from abc import abstractmethod
from typing import List

from pygame import Surface, Rect


class GameComponent():

    def __init__(self):
        self.paused = False
        self.is_deleted = False
        self.image:Surface #esto se usará para dibujarlo
        self.rect:List[Rect] # colisión

    
    def toggle_pause(self):
        self.paused ^= True
    @abstractmethod
    def update(self):
        pass
