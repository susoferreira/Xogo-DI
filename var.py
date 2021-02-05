from Base.EventHandler import *
from pygame import Surface
FRAMERATE = 60
WIDTH = 800
HEIGTH = 600
POPULATION_RESOURCE_COST = 0.099
event_handler = EventHandler()
menu_bg:Surface = Surface((20,20))
menu_bg.fill("#b6bff7")
keyboard_handler = KeyboardHandler(eventHandler=event_handler)
mouse_handler = MouseHandler(eventHandler=event_handler)
menu_button = Surface((5,5))
menu_button.fill("#630d22")