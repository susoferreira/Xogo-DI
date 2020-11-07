import pygame

from graphical_item import graphical_item


class Game():
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((400, 300))
        self.all_sprites = pygame.sprite.Group()
        player = graphical_item("./placeholder1.png")
        self.all_sprites.add(player)

    def game_loop(self):
        done=False
        while not done:
            
            self.event_handler(pygame.event.get())
            self.all_sprites.draw(self.window)
            #self.update()
        pygame.display.flip()

    def update(self):
        print("updating")
        self.all_sprites.update()

    def handle_gamestate(self,gameState): # gamestate tiene setup() y ondestroy()
        pass

    def event_handler(self,events):
        for event in events:
            
            if event.type == pygame.QUIT:
                exit()

if __name__ =="__main__":
    x = Game()
    x.game_loop()
