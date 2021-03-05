from Components.Notification import Notification
from Components.Tower import Tower

from typing import List, Tuple
from pygame import Rect, Surface
import var
import pygame.math
import Base.GameComponent as GameComponent
import Base.AnimatedSprite as AnimatedSprite
class Enemy(GameComponent.GameComponent):

    def __init__(self,max_hp:int,speed:float,path:List[pygame.math.Vector2],sprite:AnimatedSprite.AnimatedSprite,rewards:float) -> None:
        super().__init__()
        self.img :Surface
        self.sprite = sprite
        self.image = self.sprite.image
        self.rect:Rect = self.sprite.rect
        self.max_hp = max_hp
        self.hp =self.max_hp
        self.speed = speed
        self.path = path
        self.current_point_index =0
        self.rect.center = self.path[0] # spawn at first point 
        self.drawer_sub = var.component_drawer.addComponent(self,self.rect,0)
        self.rotation = 0
        self.rewards = rewards
    def follow_path(self):
        
        v1 = pygame.math.Vector2(self.rect.center)
        try:
            v2 = self.path[self.current_point_index]
        except IndexError:
            self.end_of_path()
            
            return
        if v2.distance_squared_to(v1) <self.speed:
            self.current_point_index+=1
        movement = v2-v1
        movement.normalize_ip()
        movement =movement/var.FRAMERATE *self.speed
        if var.DEBUG:
            pygame.draw.line(var.alpha_frame,"#000000",self.rect.center,(v2.x,v2.y),width=3)
        angle = movement.angle_to(pygame.math.Vector2(0,1)) # angulo con el  eje 0X
        #if abs(angle - self.rotation) > 5: # solo actualizar la rotación cuando cambie el ángulo más de un grado
            
        self.rotation = angle
        self.rect.x += movement.x
        self.rect.y += movement.y
    def end_of_path(self):
        var.vidas-=1
        if var.vidas <=0:
            Notification("Has perdido el juego",duration=60)
            var.game_finished = True
        self.kill()

    def on_hit(self,hitter:Tower):
        self.hp-=hitter.damage
        if self.hp <=0:
            hitter.power +=self.rewards*0.3
            var.dinero +=self.rewards *0.7

        
    def draw_health(self):
        if self.hp <0:
            self.hp = 0
        r = min(255, 255 - (255 * ((self.hp - (self.max_hp - self.hp)) / self.max_hp)))
        g = min(255, 255 * (self.hp / (self.max_hp / 2)))
        color = (r, g, 0)
        width = int(self.rect.width * self.hp / self.max_hp)
        self.hp_bar = Rect(0, 0, width, 7)
        if self.hp < self.max_hp:
            pygame.draw.rect(self.image, color, self.hp_bar)    
    
    def kill(self):
        self.is_deleted = True
        del self
    def update(self):
        self.img = self.sprite.image 
        if self.hp <=0:
            self.kill()
        self.image = pygame.transform.rotate(self.img,self.rotation-90)
        self.draw_health()
        self.follow_path()
        self.sprite.update()


