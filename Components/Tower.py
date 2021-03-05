import pygame
import pygame.event
from pygame import Rect, Surface
from pygame.color import Color
from pygame.font import Font
from pygame.math import Vector2

import math
import Base.GameComponent
import var
from Base.AnimatedSprite import AnimatedSprite
from utils import merge_surfaces_centered, render_text


class Tower(Base.GameComponent.GameComponent):


    def __init__(self, power: float,radius:int,sprite:AnimatedSprite,damage:int):# base class
        """clase abstracta para todas las torres

        Args:
            power(float): cantidad de "recursos" que tiene un edificio
        """
        super().__init__()
        self.img:Surface #variable temporal para guardar self.image sin transformaciones
        self.sprite:AnimatedSprite =sprite
        self.rect = self.sprite.rect
        self.image = self.sprite.image
        self.drawer_sub = var.component_drawer.addComponent(self,self.rect,0) # se añade a si misma para dibujarse y guarda la suscripción para borrarse si es necesario
        self.power = power
        self.is_selected:bool = False # decide si mostrar o no el menú
        self.is_placing:bool = False
        self.damage = damage
        self.radius:int = radius
        self.radius_squared = radius**2 # para calcular colisiones sin hacer la raíz cuadrada
        self.last_time_attacked = 0 # contador usado para añadir delay a los ataques
    def shoot(self):
        pass

    def kill(self):
        self.is_deleted = True

    def render_text_on_top(self) -> Surface:
        font_surface = self.render_power()
        font_surface.set_alpha(200)
        size1 = font_surface.get_size()
        size2=self.sprite.image.get_size()
        font_rect = font_surface.get_rect()
        font_rect.center = self.rect.center
        font_rect.centery = font_rect.centery-40

        var.alpha_frame.blit(font_surface,font_rect)

    def render_power(self) -> Surface:
        txt = f"Power: {int(self.power)}"
        
        background_color=Color("#f2ffff")
        return render_text(txt, var.POWER_FONT, var.COLOR_BLACK,background_color)

    def update(self):
        self.sprite.update()
        if not self.is_placing:
            self.img = self.sprite.image
            self.attack()
        if self.is_selected:
            self.draw_radius()
        else:
            self.render_text_on_top()# si está seleccionado no renderizar el texto

        super().update()

    def draw_radius(self): # draws radius to alpha frame
        newsurf = Surface((var.WIDTH,var.HEIGTH),flags=pygame.SRCALPHA) # cosas raras de pygame
        if self.is_placing and var.collision_handler.is_colliding_with(self,"mapa"):
            
            pygame.draw.circle(newsurf,(255,72,72,10),self.sprite.rect.center,self.radius) #rgba(255,72,72)
        else:
            pygame.draw.circle(newsurf,(255,255,255,30),self.sprite.rect.center,self.radius)#rgba(255,255,255)
        var.alpha_frame.blit(newsurf,(0,0))
    
    def attack(self):
        time = pygame.time.get_ticks()
        if not (time - self.last_time_attacked > 500): # un ataque cada 0.5 segundos
            return
        self.last_time_attacked = time
        center_vector = Vector2(self.rect.centerx,self.rect.centery)
        for grupo in var.collision_handler.groups:
            if grupo.name =="enemigos":
                for enemigo in grupo.items:
                    vec1 = Vector2(enemigo.rect.center)
                    if vec1.distance_squared_to(center_vector) < self.radius_squared:
                        enemigo.on_hit(self)
                        
                        x = enemigo.rect.centerx - self.rect.centerx
                        y = enemigo.rect.centery - self.rect.centery
                        angle = math.degrees(math.atan2(y, x))
                        self.image = pygame.transform.rotate(self.img,(-angle)-90)
                        return #solo ataca a un enemigo de cada vez
