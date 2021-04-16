import time
from tkinter import *


def play():
    bt_start.place(x=10000000000, y=100000000000000)

    class Ship:
        def __init__(self):
            ship_image = PhotoImage(file='飞船.gif')
            self.id = canvas.create_image(250, 400, image=ship_image, anchor='nw')
            self.x = 0
            self.y = -1

        def move(self):
            canvas.move(self.id, self.x, self.y)

    ship = Ship()
    while True:
        ship.move()
        time.sleep(0.01)
        tk.update()


tk = Tk()
tk.title('外星入侵')
tk.resizable(0, 0)
canvas = Canvas(tk, width=500, height=500, bd=0, highlightthickness=0)
canvas.pack()
Image = PhotoImage(file='背景.gif')
canvas.create_image(0, 0, image=Image, anchor='nw')
ship_image = PhotoImage(file='飞船.gif')
id = canvas.create_image(250, 400, image=ship_image, anchor='nw')
bt_start = Button(tk, width=20, height=5, text='开始', command=play)
bt_start.pack()
bt_start.place(x=180, y=240)
tk.mainloop()
