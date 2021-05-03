import random
import time
from tkinter import *


class Spaceman:
    def __init__(self, spaceman_image, bom_image, width, height):
        self.width = width
        self.height = height
        self.bom_image = bom_image
        self.image = spaceman_image
        self.id_x = random.randint(0, 500)
        self.id = canvas.create_image(self.id_x, 0, image=self.image)
        while True:
            canvas.move(self.id, 0, 1)
            self.pos = canvas.coords(self.id)
            self.pos.append(self.pos[0] + self.width)
            tk.update()
            time.sleep(0.01)

    def die(self):
        canvas.itemconfig(self.id, image=self.bom_image)


class Biu:  # 创建子弹类
    def __init__(self, image, ship):
        self.spaceman = spaceman
        self.ship = ship
        self.image = image
        canvas.bind_all('<space>', self.fire)  # 用空格控制

    def fire(self, evt):
        ship_pos = canvas.coords(self.ship.id)  # 检测飞船位置
        self.id = canvas.create_image(ship_pos[0] + self.ship.width / 4, ship_pos[1], image=self.image,
                                      anchor='nw')  # 插入子弹图像
        while True:
            self.pos = canvas.coords(self.id)
            if self.pos[1] > 0:
                canvas.move(self.id, 0, -5)
                tk.update()
                time.sleep(0.01)  # 移动
            else:
                canvas.delete(self.id)


class Ship:
    def __init__(self, image, x, y, width, height, v):
        self.image = image
        self.width = width
        self.height = height
        self.v = v
        self.id = canvas.create_image(x - self.width / 2, y - self.height / 2, image=self.image, anchor='nw')  # 插入飞船图像
        self.x = 0
        self.canvas_width = 500
        canvas.bind_all('<KeyPress-Left>', self.left)
        canvas.bind_all('<KeyPress-Right>', self.right)  # 用'左','右'键控制
        self.pos = []

    def left(self, evt):
        self.pos = canvas.coords(self.id)
        if self.pos[0] > 0:
            canvas.move(self.id, -self.v, 0)

    def right(self, evt):
        self.pos = canvas.coords(self.id)
        if (self.pos[0] + self.width) < self.canvas_width:
            canvas.move(self.id, self.v, 0)


tk = Tk()
tk.title('外星入侵')
tk.resizable(0, 0)
canvas = Canvas(tk, width=500, height=500, bd=0, highlightthickness=0)
canvas.pack()  # 创建画布
bg_photo = PhotoImage(file='背景.gif')
ship_photo = PhotoImage(file='飞船.gif')
biu_photo = PhotoImage(file='子弹.gif')
spaceman_photo = PhotoImage(file='外星人.gif')
bomb_photo = PhotoImage(file='爆炸.gif')  # 填入图像文件
canvas.create_image(250, 250, image=bg_photo)  # 插入背景图像
ship = Ship(ship_photo, 250, 400, 60, 60, 5)
biu = Biu(biu_photo, ship)
spaceman = Spaceman(spaceman_photo, bomb_photo, 60, 60)
tk.mainloop()
