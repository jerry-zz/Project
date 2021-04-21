import time
from tkinter import *
class Ship:
    def __init__(self,image):
        self.image=image
        self.id=canvas.create_image(250,500,image=self.image)
tk=Tk()
canvas=Canvas(tk,width=500,height=500)
canvas.pack()
ship_photo=PhotoImage(file='飞船.gif')
ship=Ship(ship_photo)
def go():
    canvas.move(ship.id,0,-1)
tk.mainloop()
while 1:
    go()
    time.sleep(0.01)