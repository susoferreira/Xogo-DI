from Components.Building import Building
from Base import AnimatedSprite
   
import var

from pygame.time import Clock

class ShootingBuilding(GameComponent):


    def __init__(self, owner: str, power: float):# base class
        """edificio que dispara proyectiles en la dirección del ratón

        Args:
            owner (str): id del jugador que controla el edificio
            power(float): cantidad de "recursos" que tiene un edificio
        """
        self.sprite:AnimatedSprite = AnimatedSprite("assets/test_sprite/desc.json", animation_delay=9,
                                pos=(var.WIDTH // 1, var.HEIGTH // 2), scale=5)
        self.rect = self.sprite.rect

    def shoot():
        pass
    def moveTowards(self,x,y):
        dx, dy = (bx - ax, by - ay)
        stepx, stepy = (dx / 24., dy / 25.)



    def update(self):

        self.sprite.update()
        self.image = self.render_text_on_top()
        self.grow_population(1/var.FRAMERATE)
        super().update()

class Projectile(object): #base class for all projectiles
    def __init__(self,sprite,vel):
        self.sprite:animatedSprite
        self.image = self.sprite.image
        self.vel:float 
    def shoot(self):
        pass

    def update():
        pass
