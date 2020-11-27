from Base.game_component import GameComponent
from Base.graphical_item import graphical_item


class test_component(GameComponent):
    def __init__(self) -> None:
        self.player = graphical_item("./assets/test_sprite/desc.json",1,True,10)
    
