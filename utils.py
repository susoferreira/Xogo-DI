from pygame import Rect, Surface
import pygame
from pygame.font import Font
from pygame.color import Color


def render_text(text: str, font: Font, color: Color) -> Surface:
    return font.render(text, True, color)


def merge_surfaces_centered(top: Surface, bottom: Surface) -> Surface: #TODO arreglar centrado

    size1 = top.get_size()
    size2 = bottom.get_rect().size
    final_size = (size1[0] + size2[0],size1[1]+size2[1])
    obj = pygame.Surface(final_size)
    obj.fill(Color(255,255,255))
    obj.blit(bottom, (0,0))
    obj.blit(top, (0,0))
    return obj
