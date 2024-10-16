import pygame
import ctypes

pygame.init()
class Input():
    def __init__(self, x, y,width, height,fg=(255,255,255),pg=(255,0,0), font="SimHei", font_size=16) -> None:
        self.code = ""
        self.fg = fg
        self.pg = pg
        self.rc = pygame.rect.Rect(x, y, width, height)
        self.font = pygame.font.SysFont(font, font_size)
        self.text = self.font.render(self.code, True, (255, 255, 255))
        self.tr = self.text.get_rect()
        self.tr.x = x
        self.tr.y = y
        
    def draw(self, surface) -> None:
        self.text = self.font.render(self.code, True, self.fg)
        self.bc = pygame.draw.rect(surface, self.fg, (self.rc.x, self.rc.y, self.rc.width, self.rc.height), 3)
        pos = pygame.mouse.get_pos()
        if self.bc.collidepoint(pos):
            self.bc = pygame.draw.rect(surface, self.pg, (self.rc.x, self.rc.y, self.rc.width, self.rc.height), 3)
        surface.blit(self.text, (self.rc.x+2, self.tr.y+self.rc.height/2-self.tr.height/2))
        
    def start(self, event) -> None:
        self.pos = pygame.mouse.get_pos()
        if self.bc.collidepoint(self.pos):
                print(ctypes.windll.user32.GetKeyState(0x14) & 0xFFFF != 0)
                if (event.key >= 33 and event.key <= 64) or (event.key >= 91 and event.key <= 126) and not ctypes.windll.user32.GetKeyState(0x14) & 0xFFFF != 0:
                    self.code += pygame.key.name(event.key)
                elif (event.key >= 33 and event.key <= 64) or (event.key >= 91 and event.key <= 126) and ctypes.windll.user32.GetKeyState(0x14) & 0xFFFF != 0:
                    self.code += pygame.key.name(event.key).upper()
                elif event.key == 32:
                    self.code += " "
                elif event.key == 8:
                    self.code = self.code[:-1]

    def get_values(self) -> str:
        return self.code