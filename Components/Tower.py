import pygame
import pygame.event
from pygame import Surface
from pygame.color import Color
from pygame.font import Font

import Base.GameComponent
import game
import var
from Base.AnimatedSprite import AnimatedSprite
from Components.Menu import Menu
from utils import merge_surfaces_centered, render_text


class Tower(Base.GameComponent.GameComponent):


    def __init__(self, power: float):# base class
        """clase abstracta para todas las torres

        Args:
            power(float): cantidad de "recursos" que tiene un edificio
        """
        self.sprite:AnimatedSprite = AnimatedSprite("assets/test_sprite/desc.json", animation_delay=9,
                                pos=(var.WIDTH // 1, var.HEIGTH // 2), scale=5) # test sprite
        self.image = self.sprite.image
        self.power = power
        self.rect = self.sprite.rect
        self.menu = Menu(self,self.rect.x,self.rect.y, var.menu_bg, [2000, "MAX"])
        self.selected:bool = False # decide si mostrar o no el menú
        self.menu.add_btn(var.menu_button,"upgrade")
        self.damage:int
        self.subSelect = var.mouse_handler.subscribe(self.rect,self.select) # cuando se pulse dentro del Rectangulo de la torre se ejecutará la función self.clicked(event)
        self.subUnselect =var.keyboard_handler.subscribe(pygame.K_ESCAPE,self.unselect)
    
    def shoot(self):
        pass

    def select(self,event: pygame.event):
        self.selected = True
    def unselect(self,event):
        self.selected=False
    def render_text_on_top(self) -> Surface:
        font_surface = self.render_power()
        obj = merge_surfaces_centered(font_surface, self.sprite.image)
        return obj

    def render_power(self) -> Surface:
        txt = f"Power: {self.power}"
        font: Font = pygame.font.SysFont("Cantarell", 20)
        color = Color("#FFFFFF")
        return render_text(txt, font, color)

    def update(self):
        self.sprite.update()
        if self.selected:
            self.menu.update()
            self.image = self.sprite.image
        else:
            self.image = self.render_text_on_top()# si está seleccionado no renderizar el texto
            
        super().update()

class Projectile(): #base class for all projectiles
    def __init__(self,sprite,vel):
        self.sprite:AnimatedSprite
        self.image = self.sprite.image 
        self.vel:float 
    def shoot(self):
        pass

    def update(self):
        pass

# class towerccccc:
#     """
#     Abstract class for towers
#     """
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#         self.width = 0
#         self.height = 0
#         self.sell_price = [0,0,0]
#         self.price = [0,0,0]
#         self.level = 1
#         self.selected = False
#         # define menu and buttons
#         self.menu = Menu(self, self.x, self.y, menu_bg, [2000, "MAX"])
#         self.menu.add_btn(upgrade_btn, "Upgrade")

#         self.tower_imgs = []
#         self.damage = 1

#         self.place_color = (0,0,255, 100)

#     def draw(self, win):
#         """
#         draws the tower
#         :param win: surface
#         :return: None
#         """
#         img = self.tower_imgs[self.level - 1]
#         win.blit(img, (self.x-img.get_width()//2, self.y-img.get_height()//2))

#         # draw menu
#         if self.selected:
#             self.menu.draw(win)

#     def draw_radius(self,win):
#         if self.selected:
#             # draw range circle
#             surface = pygame.Surface((self.range * 4, self.range * 4), pygame.SRCALPHA, 32)
#             pygame.draw.circle(surface, (128, 128, 128, 100), (self.range, self.range), self.range, 0)

#             win.blit(surface, (self.x - self.range, self.y - self.range))

#     def draw_placement(self,win):
#         # draw range circle
#         surface = pygame.Surface((self.range * 4, self.range * 4), pygame.SRCALPHA, 32)
#         pygame.draw.circle(surface, self.place_color, (50,50), 50, 0)

#         win.blit(surface, (self.x - 50, self.y - 50))

#     def click(self, X, Y):



#     def upgrade(self):
#         """
#         upgrades the tower for a given cost
#         :return: None
#         """
#         if self.level < len(self.tower_imgs):
#             self.level += 1
#             self.damage += 1

#     def get_upgrade_cost(self):
#         """
#         returns the upgrade cost, if 0 then can't upgrade anymore
#         :return: int
#         """
#         return self.price[self.level-1]
