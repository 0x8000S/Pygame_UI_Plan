import pygame

class slidebar():
    def __init__(self,x, y,  width, max_values) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.max_values = max_values
        self.values = 0
        self.bg = pygame.rect.Rect(self.x, self.y, self.width, 10)
        self.re = pygame.rect.Rect(self.bg.left, self.bg.y - 1, 15, 12)
        self.min_width = self.width/max_values
    def draw(self, screen) -> None:
        pygame.draw.rect(screen, (255,255,255), self.bg)
        pygame.draw.rect(screen, (255, 0, 0), self.re)
        pos = pygame.mouse.get_pos()
        if self.bg.collidepoint(pos) and pygame.mouse.get_pressed()[0]:
            self.re.x = pos[0]
    def get_values(self) -> int:
        add_values = self.re.x - self.x
        return round(add_values/self.min_width)