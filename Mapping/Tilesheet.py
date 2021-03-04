#https://python-forum.io/Thread-PyGame-Loading-images-transparency-handling-spritesheets-part-2

from typing import Tuple
import pygame as pg
  



class Tilesheet():
    def __init__(self,image:str,size:Tuple[int,int],rows:int,columns:int,start:Tuple[int,int]):
        """lee una imagen de un tilesheet y separa todas las tiles

        Args:
            image (str): ruta de la imagen
            size (Tuple[int,int]): tamaño de cada tile
            rows (int): [description]
            columns (int): [description]
            start (Tuple[int,int]): [description]
        """
        self.image = pg.image.load(image)
        self.start = start
        self.size = size
        self.colums = columns
        self.rows = rows
        self.frames=[]
        self.strip_from_sheet()
    def strip_from_sheet(self):

        for j in range(self.rows):
            for i in range(self.colums):
                location = (self.start[0]+self.size[0]*i, self.start[1]+self.size[1]*j)
                self.frames.append(self.image.subsurface(pg.Rect(location, self.size)))
    def get_tile(self,x,y):
        location = x+self.colums*y
        return self.frames[location]
        



if __name__ =="__main__":
    #Código para probar la extracción del tilesheet
    pg.init()
        
    screen = pg.display.set_mode((800,600))
    screen_rect = screen.get_rect()
    done = False
    
    sheet = Tilesheet("assets/opengameart_kenney/Tilesheet/towerDefense_tilesheet.png",(64,64),12,23,(0,0))
    x=0
    y=0
    while not done:
        for event in pg.event.get(): 
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.KEYDOWN:
                if event.key ==pg.K_LEFT:
                    x-=1
                if event.key == pg.K_RIGHT:
                    x+=1
                if event.key == pg.K_UP:
                    y-=1
                if event.key == pg.K_DOWN:
                    y+=1
        screen.blit(sheet.get_tile(x,y), screen_rect.center)
        pg.display.update()


tileset = Tilesheet("assets/opengameart_kenney/Tilesheet/towerDefense_tilesheet.png",(64,64),12,23,(0,0))
