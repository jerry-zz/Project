from tkinter import *


def home():
    tk = Tk()
    tk.title('不用尝试了')
    tk.resizable(0, 0)
    canvas = Canvas(tk, width=500, height=300, highlightthickness=0, bg='black')
    canvas.pack()
    canvas.create_text(250, 150, text='''相信我吧
你关不掉我的''', fill='red', font=('Arial', 50))
    tk.mainloop()


def screen2():
    tk1 = Tk()
    tk1.title('都叫你相信我了')
    tk1.resizable(0, 0)
    canvas = Canvas(tk1, width=500, height=500, highlightthickness=0, bg='yellow')
    canvas.pack()
    canvas.create_text(250, 250, text='''放弃
挣扎
吧!''', fill='blue', font=('Arial', 100))
    tk1.mainloop()


while 1:
    home()
    screen2()
