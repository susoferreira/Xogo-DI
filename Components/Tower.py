import pygame
import pygame.event
from pygame import Surface
from pygame.color import Color
from pygame.font import Font

import Base.GameComponent
import var
from Base.AnimatedSprite import AnimatedSprite
from utils import merge_surfaces_centered, render_text


class Tower(Base.GameComponent.GameComponent):


    def __init__(self, power: float,radius:int):# base class
        """clase abstracta para todas las torres

        Args:
            power(float): cantidad de "recursos" que tiene un edificio
        """
        print("creando torre")
        self.sprite:AnimatedSprite = AnimatedSprite("assets/test_sprite/desc.json", animation_delay=9,
                                pos=(var.WIDTH // 1, var.HEIGTH // 2), scale=3) # test sprite
        self.rect = self.sprite.rect
        self.image = self.sprite.image
        self.drawer_sub = var.component_drawer.addComponent(self,self.rect,0) # se añade a si misma para dibujarse y guarda la suscripción para borrarse si es necesario
        self.power = power
        self.is_selected:bool = False # decide si mostrar o no el menú
        self.is_placing:bool = False
        self.damage:int
        self.radius:int = radius
    
    def shoot(self):
        pass

    def kill(self):
        var.component_drawer.removeSubscription(self.drawer_sub)

    def render_text_on_top(self) -> Surface:
        font_surface = self.render_power()
        font_surface.set_alpha(200)
        obj = merge_surfaces_centered(font_surface, self.sprite.image)
        return obj

    def render_power(self) -> Surface:
        txt = f"Power: {self.power}"
        font: Font = pygame.font.SysFont("Cantarell", 20)
        color = Color("#000000")
        background_color=Color(5,5,5)
        return render_text(txt, font, color,background_color)

    def update(self):

        self.sprite.update()
        if self.is_selected:
            self.image = self.sprite.image
            self.draw_radius()
        else:
            self.image = self.render_text_on_top()# si está seleccionado no renderizar el texto
            self.rect = self.image.get_bounding_rect()
        #debug
        #self.image.fill((255,255,255))
        #debug
        super().update()

    def draw_radius(self): # draws radius to alpha frame
        if self.is_placing and var.collision_handler.is_colliding_with(self,"mapa"):
            
            pygame.draw.circle(var.alpha_frame,(255,72,72,30),self.sprite.rect.center,self.radius) #rgba(255,72,72)
        else:
            pygame.draw.circle(var.alpha_frame,(255,255,255,30),self.sprite.rect.center,self.radius)#rgba(255,255,255)
            

class Projectile(): #base class for all projectiles
    def __init__(self,sprite,vel):
        self.sprite:AnimatedSprite
        self.image = self.sprite.image 
        self.vel:float 
    def shoot(self):
        pass

    def update(self):
        pass
