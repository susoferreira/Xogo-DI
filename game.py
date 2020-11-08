import pygame

from graphical_item import graphical_item

WIDTH = 400
HEIGTH = 300
class Game():
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIDTH, HEIGTH))
        self.all_sprites = pygame.sprite.Group()
        self.player = graphical_item("./assets/test_sprite/desc.json",50,True,10)
        self.all_sprites.add(self.player)
        
    def game_loop(self):
        done=False
        clock = pygame.time.Clock()
        while not done:
            clock.tick(60)
            self.update()
            self.window.fill((0,0,0))
            self.event_handler(pygame.event.get())
            self.all_sprites.draw(self.window) 
            pygame.display.flip()

    def update(self):
        self.all_sprites.update()

    def handle_gamestate(self,game_state): # gamestate tiene setup() y ondestroy()
        pass

    def event_handler(self,events: pygame.event.Event):
        for event in events:
            print(type(event))
            if event.type == pygame.QUIT:
                exit()

if __name__ =="__main__":
    x = Game()
    x.game_loop()
