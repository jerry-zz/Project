import random
import time
from tkinter import *

tk = Tk()
tk.title('抽奖工具')
tk.resizable(0, 0)
canvas = Canvas(tk, width=500, height=300, bg='black', bd=0, highlightthickness=0)
canvas.pack()
a = canvas.create_text(250, 100, text='预备', font=('Arial', 50), fill='yellow')


def start():
    filename = '内容.txt'
    with open(file=filename, encoding='utf8') as f:
        f = f.read()
        try:
            file = int(f) + 1
            file = list(range(1, file))
            file = random.choice(file)
            canvas.itemconfig(a, text=file)
            time.sleep(0.1)
        except:
            file = (f.split(','))
            file = random.choice(file)
            canvas.itemconfig(a, text=file)


def quit():
    tk.quit()


bt_start = Button(tk, width=20, height=5, text='开始', command=start)
bt_start.pack()
bt_start.place(x=200, y=150)
bt_quit = Button(tk, width=10, height=2, text='退出', command=quit)
bt_quit.pack()
bt_quit.place(x=400, y=250)
tk.mainloop()
