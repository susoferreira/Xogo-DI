from pygame import Surface
from pygame.font import Font
from pygame.color import Color
def render_text(text:str,font:Font,color: Color) -> Surface:
       return font.render(text,True,color)

