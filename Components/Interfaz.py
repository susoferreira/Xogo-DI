import Base.GameComponent
import var
import pygame.time

class Interfaz(Base.GameComponent.GameComponent):
    def __init__(self):
        super().__init__()
        self.draw_text()
        var.component_drawer.addComponent(self,self.rect,10)

    def update(self):
        self.draw_text()

    def draw_text(self):

        text = f"DINERO: {round(var.dinero,2)}    VIDAS: {var.vidas}"
        img = var.UI_FONT.render(text,1,"#ffffff","#000000")
        self.rect = img.get_rect()
        self.image = img
        self.rect.topleft = (var.WIDTH*0.01, var.HEIGTH*0.01)

    def kill(self):
        self.is_deleted=True
