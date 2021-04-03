import time
from tkinter import *


def get_time():  # 定义函数
    t = time.localtime()  # 获取时间
    year = t[0]  # 用时间定义变量(7-13)
    month = t[1]
    month_day = t[2]
    hour = t[3]
    minute = t[4]
    second = t[5]
    week_day = t[6] + 1
    canvas.itemconfig(hour_minute_second,
                      text='%s:%s:%s' % (hour, minute, second))  # 将28-30的文本改为时间变量(14-16),第二次开始改动上一次改完的文本
    canvas.itemconfig(year_month_day, text='%s年%s月%s日' % (year, month, month_day))
    canvas.itemconfig(week, text='星期%s' % week_day)
    tk.after(100, get_time)  # 隔0.1秒重复执行自己(那个数字代表100毫秒,等于0.1秒)


tk = Tk()
tk.title('时间')  # 标题
canvas = Canvas(tk, width=500, height=200, bg='yellow', highlightthickness=0)  # 创建画布(22-23)
canvas.pack()
canvas.create_line(0, 150, 500, 150)  # 画出分格(25-26)
canvas.create_line(300, 150, 300, 200)
hour_minute_second = canvas.create_text(250, 100, text='', font=('Arial', 100))  # 创建文本,用函数来不断改动(25-29)
year_month_day = canvas.create_text(150, 180, text='', font=('Arial', 30))
week = canvas.create_text(400, 180, text='', font=('Arial', 30))
get_time()  # 第一次运行函数
tk.mainloop()
