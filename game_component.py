
from typing import Dict
class game_component():

    def __init__(self):
        self.paused = False
        
        self.event_action = Dict[int,function]
    def toggle_pause(self):
        self.paused ^= True
    
    def update(self):
        pass

    def events(self):
        pass