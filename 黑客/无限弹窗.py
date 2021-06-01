import random
from tkinter import *
while 1:
    tk = Tk()
    tk.resizable(0,0)
    tk.title('呵呵')
    canvas = Canvas(tk, width=500, height=500, bg='green', highlightthickness=0)
    canvas.pack()
    canvas.create_text(250, 250, text='呵呵', font=('Arial', random.randint(50, 300)))
    tk.update()
