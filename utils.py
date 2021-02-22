from pygame import Rect, Surface
import pygame
from pygame.font import Font
from pygame.color import Color


def render_text(text: str, font: Font, color: Color,background_color:Color=None) -> Surface:
    if background_color:
        return font.render(text, True, color,background_color)
    else:
        return font.render(text, True, color)


def merge_surfaces_centered(top: Surface, bottom: Surface) -> Surface:

    size1 = top.get_size()
    size2 = bottom.get_rect().size
    final_size = (max(size1[0],size2[0]),size1[1]+size2[1])
    obj = pygame.Surface(final_size,flags=pygame.SRCALPHA)
    rect_top = top.get_rect()
    rect_top.centerx = final_size[0]//2
    obj.blit(top,rect_top.topleft)
    obj.blit(bottom,bottom.get_rect())
    return obj
