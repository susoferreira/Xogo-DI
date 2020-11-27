from Base.game_component import game_component
from Base.graphical_item import graphical_item


class test_component(game_component):
    def __init__(self) -> None:
        self.player = graphical_item("./assets/test_sprite/desc.json",1,True,10)
    
