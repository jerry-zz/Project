import time
from tkinter import *


def egg():  # 创建一个彩蛋
    tk_egg = Tk()
    tk_egg.resizable(0, 0)
    tk_egg.title('彩蛋')
    canvas_egg = Canvas(tk_egg, width=500, height=500, bg='black', highlightthickness=0)
    canvas_egg.pack()
    canvas_egg.create_text(250, 250, text='''小赖赖
  生日
  快乐!''', font=('Arial', 50), fill='white')
    happy_birthday_photo = PhotoImage(file="C:\\Users\\jerry\\Documents\\GitHub\\Project\\Clock\\Birthday.gif")
    canvas_egg.create_image(0, 0, anchor=NW, image=happy_birthday_photo)
    tk_egg.mainloop()


def get_time():  # 定义函数
    global egg_go_birthday_1
    global egg_go_birthday_2
    t = time.localtime()  # 获取时间
    year = t[0]  # 用时间定义变量
    month = t[1]
    month_day = t[2]
    hour = t[3]
    minute = t[4]
    second = t[5]
    week_day = t[6] + 1
    if month == 4 and month_day == 4:
        egg_go_birthday_2 = True
    if egg_go_birthday_1 == True and egg_go_birthday_2 == True:  # 彩蛋触发条件
        canvas.itemconfig(hour_minute_second,
                          text='%s:%s:%s' % (hour, minute, second))  # 将28-30的文本改为时间变量(14-16),第二次开始改动上一次改完的文本
        canvas.itemconfig(year_month_day, text='%s年%s月%s日' % (year, month, month_day))
        canvas.itemconfig(week, text='星期%s' % week_day)
        tk.after(100, get_time)  # 隔0.1秒重复执行自己(那个数字代表100毫秒,等于0.1秒)
        egg_go_birthday_1 = False  # 取消条件(只执行一次彩蛋)
        egg()  # 执行彩蛋
    else:
        canvas.itemconfig(hour_minute_second,
                          text='%s:%s:%s' % (hour, minute, second))  # 将文本改为时间变量,第二次开始改动上一次改完的文本
        canvas.itemconfig(year_month_day, text='%s年%s月%s日' % (year, month, month_day))
        canvas.itemconfig(week, text='星期%s' % week_day)
        tk.after(100, get_time)  # 隔0.1秒重复执行自己(那个数字代表100毫秒,等于0.1秒)


tk = Tk()
tk.title('时间')  # 标题
canvas = Canvas(tk, width=500, height=200, bg='yellow', highlightthickness=0)  # 创建画布
canvas.pack()
canvas.create_line(0, 150, 500, 150)  # 画出分格
canvas.create_line(300, 150, 300, 200)
hour_minute_second = canvas.create_text(250, 100, text='', font=('Arial', 100))  # 创建文本,用函数来不断改动画布文本
year_month_day = canvas.create_text(150, 180, text='', font=('Arial', 30))
week = canvas.create_text(400, 180, text='', font=('Arial', 30))
egg_go_birthday_1 = True  # 设置彩蛋触发条件变量
egg_go_birthday_2 = False
get_time()  # 第一次运行时钟函数
tk.mainloop()
