#parser para mapas creados con Tiled en modo csv 
from typing import List, Tuple

import pygame as pg
from pygame import Color, Rect, Surface, event
import pygame
from pygame.constants import SRCALPHA
from pytmx.util_pygame import load_pygame
import Base.GameComponent as gc
class TileMap(gc.GameComponent):
    
    class Tile():
        def __init__(self,image:Surface,collider:List[Rect],x:int,y:int):
            self.image = image
            self.collider = collider
            self.x = x
            self.y = y

    def __init__(self,file:str,size:Tuple[int,int]):
        self.rect = []
        
        
        self.debug =True # si debug es true dibuja las colisiones
        
        
        self.tmx_data = load_pygame(file)
        self.layers =self.tmx_data.visible_layers
        self.size = size
        self.tiles:List[TileMap.Tile] = []
        self.create_tiles()
        self.image:Surface =self.render_tiles()
        self.create_rect()
        
        
    def create_rect(self):
        for tile in self.tiles:
            self.rect +=tile.collider

    def render_tiles(self) ->Surface:
        image = Surface(
            (self.size[0]*self.tmx_data.width,
            self.size[1]*self.tmx_data.height),
            flags=pg.SRCALPHA
        )

        for tile in self.tiles:
            image.blit(tile.image,
                            (self.size[0]*tile.x,
                             self.size[1]*tile.y)
                            )
            if self.debug:
                for rect in tile.collider:
                    rect.topleft = self.size[0]*tile.x+rect.x,self.size[1]*tile.y+rect.y
                    pygame.draw.rect(image, Color(219,156,216,30), rect,2)
        return image
    
    def create_tiles(self):
        """Crea las tiles del mapa y las guarda con su colisión para poder renderizarla después
        """
        self.tiles =[]
        for layer in self.tmx_data.visible_layers:
                for x, y, gid, in layer:
                    collider_rects =[]
                    img:pg.Surface = self.tmx_data.get_tile_image_by_gid(gid) #conseguir imagen de tile
                    if img is not None:
                        scale = (
                            self.size[0]/img.get_size()[0],
                            self.size[1]/img.get_size()[1]
                                )
                        img = pygame.transform.scale(img,self.size) # escalar imágen al tamaño adecuado
                        props = (self.tmx_data.get_tile_properties_by_gid(gid)) # conseguir props de tile
                        if props:
                            try:
                                colliders = props["colliders"]# conseguir los colliders
                                if colliders:
                                    collider_rects = [Rect(collider.x*scale[0]
                                                        ,collider.y*scale[1]
                                                        ,collider.width*scale[0]
                                                        ,(collider.height+collider.y)*scale[1]-collider.y*scale[1]
                                    )
                                                    for collider in colliders] #pasar colliders a lista de Rect para pygame, ajustados al escalado
                            except KeyError:
                                print("no hay colliders")
                        self.tiles.append(TileMap.Tile(img,collider_rects,x,y))


    def draw_map_to_surface(self) ->Surface:
        """Renderiza el mapa a una superficie, solo guarda la superficie,usar si no se necesita nada adicional

        Returns:
            Surface: [description]
        """
        image = Surface(
            (self.size[0]*self.tmx_data.width,
            self.size[1]*self.tmx_data.height)
        )

        for layer in self.tmx_data.visible_layers:
                for x, y, gid, in layer:

                    img:pg.Surface = self.tmx_data.get_tile_image_by_gid(gid) #conseguir imagen de tile
                    
                    if img is not None:
                        img = pygame.transform.scale(img,self.size)

                        image.blit(img,
                                        (self.size[0]*x,
                                        self.size[1]*y)
                                    )

        return image
    def set_size(self,size:Tuple[int,int]):

        self.size = size
        self.create_tiles()
        self.image = self.render_tiles()
        
if __name__ =="__main__":
    pg.init()
    screen = pg.display.set_mode((1024,1024))
    done = False

    size=(64,64)
    mapa = TileMap("/run/media/suso/SHARE/Programación/Xogo-DI/assets/mapas/mapa1.tmx",size)
    while not done:
        
        #mapa.draw_map_to_surface()
        for event in pg.event.get(): 
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.KEYDOWN:

                if event.key == pg.K_UP:
                    mapa.set_size((mapa.size[0]+1,mapa.size[1]+1))
                if event.key == pg.K_DOWN:
                    mapa.set_size((mapa.size[0]-1,mapa.size[1]-1))
        screen.fill(Color(255,255,255))
        screen.blit(mapa.image,(0,0))
        pg.display.flip()
