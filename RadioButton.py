import pygame
import time
# 复选框
class RadioButton():
    def __init__(self,Text,x,y,bg=(255,255,255),fg=(0, 0, 0),pg=(255,0,0),fonts="SimHei",font_size=16,border=2,scale=1) -> None:
        self.Text = Text
        self.bg = bg
        self.fg = fg
        self.pg = pg
        font = pygame.font.SysFont(fonts, font_size)
        self.image = font.render(Text, True, bg)
        width = self.image.get_width()
        height = self.image.get_height()
        self.image = pygame.transform.scale(self.image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.bgr = pygame.rect.Rect(0,0,height*scale,height*scale)
        self.fgr = pygame.rect.Rect(0, 0, height*scale-border, height*scale-border)
        self.bgr.topleft = (x,y)
        self.fgr.center = self.bgr.center
        self.p = pygame.rect.Rect(0,0,self.fgr.width-2,self.fgr.width-2)
        self.p.center = self.fgr.center
        self.clicked = [False,True, False]
        self.index = 0
    def draw(self, screen) -> None:
        pos = pygame.mouse.get_pos()
        pygame.draw.rect(screen, self.bg, self.bgr)
        if self.bgr.collidepoint(pos):
            pygame.draw.rect(screen, self.pg, self.bgr)
            if pygame.mouse.get_pressed()[0]:
                self.index += 1
                if self.index > 1:
                    self.index = 0
                time.sleep(0.2)
        pygame.draw.rect(screen, self.fg, self.fgr)
        if self.clicked[self.index]:
            pygame.draw.rect(screen, self.pg, self.p)
        screen.blit(self.image, (self.rect.x+self.bgr.width, self.rect.y))

    def get_values(self) -> bool:
        return self.clicked[self.index]


