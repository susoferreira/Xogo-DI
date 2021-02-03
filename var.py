from Base.EventHandler import *

FRAMERATE = 60
WIDTH = 800
HEIGTH = 600
POPULATION_RESOURCE_COST = 0.099
event_handler = EventHandler()
keyboard_handler = KeyboardHandler(eventHandler=event_handler)
mouse_handler = MouseHandler(eventHandler=event_handler)
