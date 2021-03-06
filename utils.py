from Base.GameComponent import GameComponent
from pygame import Rect, Surface
import pygame
from pygame.font import Font
from pygame.color import Color
from pygame.math import Vector2


def render_text(text: str, font: Font, color: Color,background_color:Color=None) -> Surface:
    if background_color:
        return font.render(text, True, color,background_color)
    else:
        return font.render(text, True, color)

def load_image_without_empty_space(path:str) ->Surface:
    image = pygame.image.load(path)
    return image.subsurface(image.get_bounding_rect())


def merge_surfaces_centered(top: Surface, bottom: Surface) -> Surface:

    size1 = top.get_size()
    size2 = bottom.get_rect().size
    final_size = (max(size1[0],size2[0]),size1[1]+size2[1])
    obj = pygame.Surface(final_size,flags=pygame.SRCALPHA)
    rect_top = top.get_rect()
    rect_top.centerx = final_size[0]//2
    obj.blit(bottom,bottom.get_rect())
    obj.blit(top,rect_top.topleft)
    return obj

def inverse_lerp(value_min:float,value_max:float,value_current:float) -> float:
    return ( value_current - value_min ) /(value_max -value_min)
