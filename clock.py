import time
from tkinter import *


def gettime():
    time.sleep(1)
    t = time.localtime()
    year = t[0]
    month = t[1]
    month_day = t[2]
    hour = t[3]
    minute = t[4]
    second = t[5]
    week_day = t[6] + 1
    H_M_S.configure(text='%s:%s:%s' % (hour, minute, second))
    Y_M_D.configure(text='%s年%s月%s日' % (year, month, month_day))
    W.configure(text='星期%s' % week_day)

    tk.after(1, gettime)  # 每隔1s调用函数gettime自身获取时间


tk = Tk()
tk.title("时钟")
canvas = Canvas(tk, width=500, height=300)
canvas.pack()
H_M_S = Label(tk, text='', font=('Arial', 80))
H_M_S.pack()
H_M_S.place(x=40, y=100)
Y_M_D = Label(tk, text='', font=('Arial', 50))
Y_M_D.pack()
Y_M_D.place(x=40, y=300)
W = Label(tk, text='', font=('Arial', 50))
W.pack()
W.place(x=200, y=300)
gettime()
tk.mainloop()
