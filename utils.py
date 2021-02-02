from pygame import Surface
import pygame
from pygame.font import Font
from pygame.color import Color


def render_text(text: str, font: Font, color: Color) -> Surface:
    return font.render(text, True, color)


def merge_surfaces_centered(top: Surface, bottom: Surface) -> Surface:

    size1 = top.get_size()
    size2 = bottom.get_rect().size
    final_size = (size1[0] + size2[0], size2[1])
    obj = pygame.Surface(final_size)
    obj.blit(top, (final_size[0]/2, 0))
    obj.blit(bottom, size1)
    return obj
