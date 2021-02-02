from Base.EventHandler import EventHandler, KeyboardHandler

FRAMERATE = 60
WIDTH = 700
HEIGTH = 600
POPULATION_RESOURCE_COST = 0.099
event_handler = EventHandler()
keyboard_handler = KeyboardHandler(eventHandler=event_handler)
