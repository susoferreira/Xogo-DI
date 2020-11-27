
from abc import abstractmethod
from typing import Dict
class game_component():

    def __init__(self):
        self.paused = False
        
        self.event_action = Dict[int,function]
    
    def toggle_pause(self):
        self.paused ^= True
    @abstractmethod
    def update(self):
        pass
    @abstractmethod
    def events(self):
        pass