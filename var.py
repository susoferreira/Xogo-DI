from Mapping.TiledParser import TileMap
from pygame import Color, Surface
import pygame
from pygame.font import Font
from Base.EventHandler import event_handler,keyboard_handler,mouse_handler,collision_handler
from Base.ComponentDrawer import component_drawer
pygame.display.init()
pygame.font.init()
FRAMERATE = 60
WIDTH = 1440
HEIGTH = 960
SCREEN_SIZE = (WIDTH,HEIGTH)
POWER_FONT: Font = pygame.font.SysFont("Arial", 20)
COLOR_BLACK = Color("#000000")
DEBUG=False
alpha_frame = Surface((WIDTH,HEIGTH),flags=pygame.SRCALPHA)
sprite_debug = "assets/test_sprite/desc.json"
mapa:TileMap
