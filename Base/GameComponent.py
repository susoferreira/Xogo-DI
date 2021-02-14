from abc import abstractmethod

from pygame import Surface, Rect


class GameComponent():

    def __init__(self):
        self.paused = False
        self.image:Surface #esto se usará para dibujarlo
        self.rect:Rect # colisión


    
    def toggle_pause(self):
        self.paused ^= True
    @abstractmethod
    def update(self):
        pass
