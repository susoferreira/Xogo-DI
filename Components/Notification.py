import Base.GameComponent
import var
import pygame.font
import utils
class Notification(Base.GameComponent.GameComponent):
    def __init__(self,text:str,duration = 3):
        super().__init__()
        self.text = text
        self.duration = duration
        self.frame_counter = 0
        self.draw_text()
        var.component_drawer.addComponent(self,self.rect,10)
        var.notifications.append(self)

    def update(self):
        if self.frame_counter == self.duration*var.FRAMERATE:
            self.kill()
        self.frame_counter+=1
        self.draw_text()

    def draw_text(self):
        img = var.NOTIFICATION_FONT.render(self.text,1,"#ffffff","#000000")

        img.set_alpha(
            utils.inverse_lerp(self.duration*var.FRAMERATE,0,self.frame_counter) * 255
        )
        self.rect = img.get_rect()
        self.image = img
        self.rect.center = (var.WIDTH/2, var.HEIGTH*0.9)

    def kill(self):
        self.is_deleted=True
