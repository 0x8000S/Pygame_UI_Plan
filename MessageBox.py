import pygame

class MessageBox:
    # 初始化函数
    def __init__(self, title="test", text="", size=(400,300), pos=(0,0)) -> None:
        self.size = size
        self.pos = pos
        font = pygame.font.SysFont("SimHei", 16)
        self.image = font.render(text, True, (255,255,255))
        self.title_bar = pygame.rect.Rect(pos[0], pos[1], size[0], 20)
        self.window = pygame.rect.Rect(pos[0], pos[1]+20, size[0], size[1])
        self.window.top = self.title_bar.bottom

    # 绘制函数
    def draw(self, screen) -> None:
        # 窗口绘制
        pygame.draw.rect(screen, (255,0,0), self.title_bar)
        pygame.draw.rect(screen, (0, 255, 0), self.window)
        self.window.top = self.title_bar.bottom
        self.window.x = self.title_bar.x
        # 窗口拖动逻辑
        mouse_pos = pygame.mouse.get_pos()
        Offset_X = self.title_bar.x - mouse_pos[0]
        Offset_Y = self.title_bar.y - mouse_pos[1]
        if self.title_bar.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]:
            self.title_bar.x -= Offset_X + self.title_bar.width/2
            self.title_bar.y -= Offset_Y + 10
            pygame.draw.rect(screen, (255, 0, 0), self.title_bar)
            pygame.draw.rect(screen, (0, 255, 0), self.window)
            print(f"Offset_X:{Offset_X} | Offset_Y:{Offset_Y} | X:{self.title_bar.x} | Y:{self.title_bar.y}")

