class game_component():

    def __init__(self):
        self.paused=False

    def toggle_pause(self):
        self.paused ^= True
    
    def update(self):
        pass

