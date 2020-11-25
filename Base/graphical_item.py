import json
from typing import Dict
from typing import Any,Tuple
import pygame
from pygame import Rect


class graphical_item(pygame.sprite.Sprite):

    def __init__(self,sprite_route: str, animation_delay:int = 1,animate:bool =True,scale: float = 1,pos:  Tuple[int, int] = (0,0)):
        """

        Args:
            sprite_route (str): [route to the sprite descriptor]
            animation_delay (int): [number of frames between each animation step]
            animate (bool): [wheter to animate the sprite or not]
            scale ([float]): [scaling of the sprite ]
        """
        pygame.sprite.Sprite.__init__(self)
        self.scale = scale
        self.animate = animate
        self.sprite_route = sprite_route
        self.descriptor =Dict[str,Any]
        self.descriptor = self.get_descriptor()
        self.image = pygame.image.load(self.get_descriptor()["default_image"])
        self.rect = self.image.get_rect()
        self.original_scale=self.image.get_bounding_rect().size
        print("escala original:",self.original_scale)

        self.set_position(pos)

        #animation
        if self.animate == True:
            self.animation_type = self.get_descriptor()["default_animation"]
            self.animation_counter = 0
            self.animation_frame = 0
            self.animation_delay = animation_delay
            self.frames = self.load_animation()

    def load_animation(self):
        imgs = []
        for animation in self.get_descriptor()["animations"]:
            if animation["name"] == self.animation_type:
                for frame in animation["frames"]:
                    img = pygame.image.load(frame)
                    img = pygame.transform.scale(img,(int(self.image.get_width()*self.scale),int(self.image.get_height()*self.scale)))
                    imgs.append(img)
                self.rect = imgs[0].get_rect()
        return imgs

    def get_descriptor(self) -> Dict[str,Any]:
        
        with open( self.sprite_route) as descriptor:
            return json.loads(descriptor.read())

    def update(self):

        if self.animate == True:
            self.animation_counter += 1
            self.animation_counter %= self.animation_delay
            if self.animation_counter == 0:
                self.animation_frame %= len(self.frames)-1
                self.animation_frame+=1
                self.image = self.frames[self.animation_frame]

    def set_position(self,pos:Tuple[int,int]):
        self.rect.move(pos[0],pos[1])

    def scale_to(self,scale:float):
        self.reset_scale()
        self.scale_by(scale)
    def reset_scale(self):
        self.frames =[pygame.transform.scale(frame,self.original_scale) for frame in self.frames]
    def scale_by(self,scale:float):
        self.scale = scale
        self.frames = self.load_animation()

    def set_animation(self,animation:str):
        self.animation_type=animation
        self.frames = self.load_animation()
