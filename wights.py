# 导库
import pygame
import sys
import SlideBar
import Button
import Input
import RadioButton
import MessageBox
# Pygame 初始化
pygame.init()
# 创建控件
a = SlideBar.slidebar(100, 200, 200, 50) # 创建拖动条控件
screen = pygame.display.set_mode((800,600)) # 创建窗口
a.draw(screen) # 拖动条绘制
b = Button.Button("Hello", 50, 50, scale=2) # 创建按钮控件
c = Input.Input(150, 70, 100, 20) # 创建输入框控件
c.draw(screen) # 输入框控件绘制
d = RadioButton.RadioButton("Hello", 400, 400, scale=2, font_size=16, border=6) # 创建单选框控件
e = RadioButton.RadioButton("Hellos", 400, 440, scale=2, font_size=16, border=6) # 创建单选框控件
message = MessageBox.MessageBox() # 创建弹窗控件
while True: # 游戏主循环
    for event in pygame.event.get(): # 获取事件
        if event.type == pygame.QUIT: # 退出事件
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN: # 输入框获取内容
            c.start(event)
    screen.fill((0,0,0)) # 填充窗口背景
    a.draw(screen) # 拖动条绘制
    b.draw(screen) # 按钮绘制
    c.draw(screen) # 输入框控件绘制
    d.draw(screen) # 单选框控件绘制
    e.draw(screen) # 单选框控件绘制
    message.draw(screen) # 弹窗控件绘制
    pygame.display.update() # 更新窗口
