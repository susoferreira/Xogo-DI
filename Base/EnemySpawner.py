import pygame
from Base.AnimatedSprite import AnimatedSprite
from typing import List
from Components.Enemy import Enemy
import threading
import var
import time
class EnemySpawner(): # genera rondas aleatoriamente
    def __init__(self):
        self.enemies :List[Enemy] =[]       
        self.current_round=-1
        self.last_spawn_time = 0
        self.wave_delay = [4000,3000,2000,1500,1200,1000,700,500,500,400]# aparecen más rapido
        self.enemy_count = [1,3,5,10,20,33,65,100,150,500] # cada ronda los enemigos tienen mas vida
        self.speed_bonus=[1,1.1,1.2,1.2,1.2,1.3,1.4,1.4,2,3] # son más rapidos
        self.hp_bonus=[1,1,1,1,1.1,1.2,1.3,1.5,1.6,2]
        var.keyboard_handler.subscribe(pygame.K_SPACE,self.start_new_round)
    
    def update(self):
        for enemy in self.enemies: # eliminar referencias a enemigos muertos
            if enemy.is_deleted:
                self.enemies.remove(enemy)
                return
            enemy.update()

    def start_new_round(self,event):
        if len(self.enemies) != 0 : # si no hay enemigos vivos retornar
            print("la ronda actual aún no ha acabado")
            return
        print("empezando ronda:",self.current_round)
        if self.current_round == len(self.enemy_count):
            print("¡Felicidades, Has acabado todas las rondas que existen por el momento!")
        self.current_round +=1
        spawner = threading.Thread(target=self.spawn_enemies)
        spawner.start()
      
    def spawn_enemies(self): # se lanza en un hilo distinto
        print("en esta ronda hay :",range(self.enemy_count[self.current_round]),"enemigos")
        for i in range(self.enemy_count[self.current_round]):
            self.spawn_enemy()
            time.sleep(self.wave_delay[self.current_round]/1000)
    
    def spawn_enemy(self):
        hp = 100* self.hp_bonus[self.current_round]
        speed = 100*self.speed_bonus[self.current_round]
        enemigo = Enemy(hp,speed,var.mapa.path,
            AnimatedSprite(
                "assets/sprite_enemigo_1/desc.json",animate=False
            ))
        self.enemies.append(enemigo)
        var.collision_handler.add_item_to_group(enemigo,"enemigos")


        
        