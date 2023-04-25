import time
from lib2to3.pgen2 import driver
import pyautogui as pg
from pynput import mouse, keyboard
time.sleep(1) # 休眠5秒
m_mouse = mouse.Controller() # 创建一个鼠标
m_keyboard = keyboard.Controller() # 创建一个键盘
#m_mouse.position =(850,670) # 将鼠标移动到指定位置
m_mouse.position = (850, 670)
m_mouse.click(mouse.Button.left) # 点击鼠标左键 获取焦点
m_keyboard.type('22')

for i in range(30):
    m_keyboard.type('hello')
    m_keyboard.type('11')
    m_keyboard.press(keyboard.Key.enter) # 按下enter

    time.sleep(1) # 间隔0.1秒ello
    m_keyboard.press(keyboard.Key.enter)  # 松开.发送信息


# 控制鼠标键盘

# print(int(4000+6000+4000+1000+5000+4000+4000))

