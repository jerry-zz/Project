from tkinter import *


class Biu:
    def __init__(self, image):
        self.image = image
        canvas.bind_all('<KeyPress-space>', self.fire)

    def fire(self):
        self.id=canvas.create_image()


class Ship:
    def __init__(self, image, x, y, width):
        self.width = width
        self.image = image
        self.id = canvas.create_image(x, y, image=self.image, anchor='nw')
        self.x = 0
        self.canvas_width = 500
        canvas.bind_all('<KeyPress-Left>', self.left)
        canvas.bind_all('<KeyPress-Right>', self.right)
        self.pos = []

    def left(self, evt):
        self.pos = canvas.coords(self.id)
        if self.pos[0] > 0:
            canvas.move(self.id, -5, 0)

    def right(self, evt):
        self.pos = canvas.coords(self.id)
        if (self.pos[0] + self.width) < self.canvas_width:
            canvas.move(self.id, 5, 0)


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
canvas.create_image(0, 0, image=bg_photo, anchor='nw')
biu = Biu(biu_photo)
ship = Ship(ship_photo, 250, 400, 60)
canvas.mainloop()
