import time
from tkinter import *


class Biu:
    def __init__(self, image, ship):
        self.ship = ship
        self.image = image
        canvas.bind_all('<space>', self.fire)

    def fire(self, evt):
        ship_pos = canvas.coords(self.ship.id)
        self.id = canvas.create_image(ship_pos[0]+self.ship.width/2,ship_pos[1],image=self.image)
        canvas.move(self.id, 0, -1)


class Ship:
    def __init__(self, image, x, y, width,height,v):
        self.image = image
        self.width = width
        self.height = height
        self.v = v
        self.id = canvas.create_image(x-self.width/2, y-self.height/2, image=self.image,anchor='nw')
        self.x = 0
        self.canvas_width = 500
        canvas.bind_all('<KeyPress-Left>', self.left)
        canvas.bind_all('<KeyPress-Right>', self.right)
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
canvas.pack()
bg_photo = PhotoImage(file='背景.gif')
ship_photo = PhotoImage(file='飞船.gif')
biu_photo = PhotoImage(file='子弹.gif')
spaceman_photo = PhotoImage(file='外星人.gif')
bomb_photo = PhotoImage(file='爆炸.gif')
canvas.create_image(250, 250, image=bg_photo)
ship = Ship(ship_photo, 250, 400, 60,60,5)
biu = Biu(biu_photo,ship)
tk.mainloop()