from typing import Dict
from game_component import game_component

class game_state():
    """defines diferent gamestates like playing, menu, the map...
        has update and event methods, a gamestate can have multiple game components inside it
    """
    def __init__(self, components: Dict[str,game_component]):
        self.components = components

    def add_component(self,comp: Dict[str,game_component]):
        self.components.update(comp)

    def update(self):
        """method that gets called every game tick, override
        """
        pass
    def update_components(self):
        """updates every subcomponent of this class
        """
        for name in self.components:
            self.components[name].update()