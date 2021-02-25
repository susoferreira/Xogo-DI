
from pygame import Surface
import pygame
from Base.EventHandler import event_handler,keyboard_handler,mouse_handler,collision_handler
from Base.ComponentDrawer import component_drawer
FRAMERATE = 60
WIDTH = 800
HEIGTH = 600
POPULATION_RESOURCE_COST = 0.099

menu_bg:Surface = Surface((20,20))
menu_bg.fill("#b6bff7")

menu_button = Surface((5,5))
menu_button.fill("#630d22")

alpha_frame = Surface((WIDTH,HEIGTH),flags=pygame.SRCALPHA)
