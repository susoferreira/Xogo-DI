

class game_state():
    """defines diferent gamestates like playing, menu, the map...
        has update and event methods, a gamestate can have multiple game components inside it
    """
    def __init__(self):
        self.done = False


    def setup(self):
        pass
    def on_destroy(self):
        pass
    def update(self):
        """method that gets called every game tick, override
        """
        pass
