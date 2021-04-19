from tkinter import *


def ship(image, x, y):
    ship_id = canvas.create_image(x, y, image=image, anchor='nw')


tk = Tk()
tk.title('外星入侵')
tk.resizable(0, 0)
canvas = Canvas(tk, width=500, height=500, bd=0, highlightthickness=0)
canvas.pack()
ship(PhotoImage(file='飞船.gif'), 250, 400)
canvas.mainloop()
