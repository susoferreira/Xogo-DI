import pygame
import var
from Base.AnimatedSprite import AnimatedSprite
from pygame import Surface
from pygame.color import Color
from pygame.font import Font
from pygame.time import Clock
from utils import merge_surfaces_centered, render_text


class ShootingBuilding(GameComponent):


    def __init__(self, owner: str, power: float):# base class
        """clase "base para todos los edificios que disparan proyectiles"

        Args:
            owner (str): id del jugador que controla el edificio
            power(float): cantidad de "recursos" que tiene un edificio
        """
        self.sprite:AnimatedSprite = AnimatedSprite("assets/test_sprite/desc.json", animation_delay=9,
                                pos=(var.WIDTH // 1, var.HEIGTH // 2), scale=5)
        self.rect = self.sprite.rect

    def shoot():
        pass
        

    def render_text_on_top(self) -> Surface:
        font_surface = self.render_po   wer()
        obj = merge_surfaces_centered(font_surface, self.sprite.image)
        return obj

    def render_power(self) -> Surface:
        txt = f"pop: {int(self.population)}, Power: {self.power}"
        font: Font = pygame.font.SysFont("Cantarell", 20)
        color = Color("#FFFFFF")
        return render_text(txt, font, color)


    def update(self):

        self.sprite.update()
        self.image = 
        self.grow_population(1/var.FRAMERATE)
        super().update()

class Projectile(): #base class for all projectiles
    def __init__(self,sprite,vel):
        self.sprite:AnimatedSprite
        self.image = self.sprite.image 
        self.vel:float 
    def shoot(self):
        pass

    def update():
        pass
