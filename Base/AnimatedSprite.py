import json
from typing import Any, Dict, Tuple 
from Base import AnimatedSprite 
import pygame
import pygame.transform
import var

class AnimatedSprite():

    def __init__(self, sprite_route: str, animation_delay: int = 1, animate: bool = True, scale: float = 1, pos:  Tuple[int, int] = (0, 0),rotation:float = 0):
        """

        Args:
            sprite_route (str): [route to the sprite descriptor]
            animation_delay (int): [number of frames between each animation step]
            animate (bool): [wheter to animate the sprite or not]
            scale ([float]): [scaling of the sprite ]
        """

        pygame.sprite.Sprite.__init__(self)
        self.frames = []
        self.original_scaling = scale
        self.current_scaling: float = scale
        self.animate = animate
        self.sprite_route = sprite_route
        self.rotation = rotation
        self.descriptor = Dict[str, Any]
        self.descriptor = self.get_descriptor()
        self.image: pygame.Surface = pygame.image.load(
            self.get_descriptor()["default_image"])
        self.rect = self.image.get_rect()
        self.size = self.image.get_bounding_rect().size
        self.set_position(pos)

        # animation
        if self.animate:

            self.animation_type = self.get_descriptor()["default_animation"]
            self.animation_counter = 0
            self.animation_frame = 0
            self.animation_delay = animation_delay
            self.load_animation(self.original_scaling)

    def load_animation(self, scale: float):

        imgs = []
        for animation in self.get_descriptor()["animations"]:
            if animation["name"] == self.animation_type:
                for frame in animation["frames"]:
                    img = pygame.image.load(frame)
                    # aplicar escalado
                    img = pygame.transform.scale(
                        img, (int(self.image.get_width()*scale), int(self.image.get_height() * scale)))
                    #aplicar rotación
                    img = pygame.transform.rotate(img,self.rotation)
                    imgs.append(img)
                self.rect = imgs[0].get_rect()
        self.frames = imgs

    def set_rotation(self,rotation:float):
        self.rotation = rotation # cambiando atributo para que se aplique al cambiar de animación
        self.frames = [pygame.transform.rotate(img,self.rotation) for img in self.frames] # aplicando el cambio de rotación a la animación actual
    def get_descriptor(self) -> Dict[str, Any]:

        with open(self.sprite_route) as descriptor:
            return json.loads(descriptor.read())

    def update(self):

        if self.animate:
            self.animation_counter += 1
            self.animation_counter %= self.animation_delay
            if self.animation_counter == 0:
                self.animation_frame %= len(self.frames)-1
                self.animation_frame += 1
                self.image = self.frames[self.animation_frame]

    def set_position(self, pos: Tuple[int, int]):
        self.rect.center = (pos[0], pos[1])

    def scale_to(self, scale: float):
        self.load_animation(scale)

    def reset_scale(self):
        self.frames = [pygame.transform.scale(frame, self.original_scaling) for frame in self.frames]

    def scale_by(self, scale: float):
        self.current_scaling *= scale
        #print("Escalado:", self.current_scaling)
        self.load_animation(scale)

    def set_animation(self, animation: str):
        self.animation_type = animation
        self.load_animation(self.original_scaling)
