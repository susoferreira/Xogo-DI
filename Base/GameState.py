

from abc import abstractmethod


class GameState():
    """defines diferent gamestates like playing, menu, the map...
        has update and event methods, a gamestate can have multiple game components inside it
    """
    def __init__(self):
        self.done = False

    @abstractmethod
    def setup(self):
        pass
    @abstractmethod
    def on_destroy(self):
        pass
    @abstractmethod
    def update(self):
        """method that gets called every game tick, override
        """
        pass
