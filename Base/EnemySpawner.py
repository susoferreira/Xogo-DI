import pygame
from Base.AnimatedSprite import AnimatedSprite
from typing import List
from Components.Enemy import Enemy
from Components.Notification import Notification
import threading
import var
import time
class EnemySpawner(): # genera rondas aleatoriamente
    def __init__(self):
        self.enemies :List[Enemy] =[]       
        self.current_round=0
        self.last_spawn_time = 0
        self.wave_delay = [4000,3000,2000,1500,1200,1000,700,500,500]# aparecen más rapido
        self.enemy_count = [1,3,5,10,20,33,65,100,300,900]
        self.speed_bonus=[1,1.1,1.2,1.2,1.2,1.3,1.4,1.4,1.5] # son más rapidos
        self.rewards_bonus=[1,1.1,1.2,1.2,1.2,1.3,2,3,4] # dan más dinero
        self.hp_bonus=[1,1,1,1,1.1,1.2,1.3,1.4,1.5]
        var.keyboard_handler.subscribe(pygame.K_SPACE,self.start_new_round)
    
    def update(self):
        for enemy in self.enemies: # eliminar referencias a enemigos muertos
            if enemy.is_deleted:
                self.enemies.remove(enemy)
                return
            enemy.update()

    def start_new_round(self,event):
        if self.current_round == len(self.wave_delay):
            Notification("¡Has completado la última ronda, felicidades!")
            var.game_finished = True
            return
        if len(self.enemies) != 0 : # si no hay enemigos vivos retornar
            Notification("la ronda actual aún no ha acabado")
            return
        Notification("empezando ronda "+str(self.current_round+1))
        self.current_round +=1
        spawner = threading.Thread(target=self.spawn_enemies)
        spawner.start()
      
    def spawn_enemies(self): # se lanza en un hilo distinto
        for i in range(self.enemy_count[self.current_round]):
            self.spawn_enemy()
            time.sleep(self.wave_delay[self.current_round]/1000)
    
    def spawn_enemy(self):
        hp = 100* self.hp_bonus[self.current_round]
        speed = 100*self.speed_bonus[self.current_round]
        rewards = 5*self.rewards_bonus[self.current_round]
        enemigo = Enemy(hp,speed,var.mapa.path,
            AnimatedSprite(
                "assets/sprite_enemigo_1/desc.json",animate=False
            ),rewards)
        self.enemies.append(enemigo)
        var.collision_handler.add_item_to_group(enemigo,"enemigos")


        
        