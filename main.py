import pygame
import sys
import Button
import Input

pygame.init()
pygame.display.init()
screen = pygame.display.set_mode((800, 600))

font = pygame.font.SysFont("微软雅黑", 20)
text = font.render("NB", True, (255, 255, 255))

btn = Button.Button("BB", 60, 70, scale=5, fg=(0,0,0))
btn.draw(screen)
ins = Input.Input(20, 20, 100, 30, font_size=25)
ins.draw(screen)

while True:
    pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if btn.get_button_state():
            print("Hi")
        if event.type == pygame.KEYDOWN:
            ins.start(event)

    
    
    screen.fill((0, 63, 54))
    btn.draw(screen, (255,0,0), (0,255,0))
    ins.draw(screen)
    pygame.display.update()