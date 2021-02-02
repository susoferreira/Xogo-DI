from abc import abstractmethod
from typing import Dict


class GameComponent():

    def __init__(self):
        self.paused = False


    
    def toggle_pause(self):
        self.paused ^= True
    @abstractmethod
    def update(self):
        pass
