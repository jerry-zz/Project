from tkinter import *

hour = 0
minute = 0
second = 0
tk = Tk()
tk.title('倒计时')
tk.resizable(0, 0)
canvas = Canvas(tk, width=500, height=400, bg='black', highlightthickness=0)
canvas.pack()
canvas.create_text(150, 150, text='时', fill='yellow', font=('Arial', 70))
canvas.create_text(300, 150, text='分', fill='yellow', font=('Arial', 70))
canvas.create_text(450, 150, text='秒', fill='yellow', font=('Arial', 70))
hour_text = canvas.create_text(75, 150, text=hour, fill='white', font=('Arial', 70))
minute_text = canvas.create_text(225, 150, text=minute, fill='white', font=('Arial', 70))
second_text = canvas.create_text(375, 150, text=second, fill='white', font=('Arial', 70))


def return_home():
    global hour
    global minute
    global second
    hour = 0
    minute = 0
    second = 0
    canvas.itemconfig(hour_text, text=hour)
    canvas.itemconfig(minute_text, text=minute)
    canvas.itemconfig(second_text, text=second)


def hour_up():
    global hour
    hour = hour + 1
    canvas.itemconfig(hour_text, text=hour)


def hour_down():
    global hour
    if hour > 0:
        hour = hour - 1
        canvas.itemconfig(hour_text, text=hour)


bt_hour_up = Button(tk, text='+1', command=hour_up)
bt_hour_up.pack()
bt_return_home = Button(tk, text='重置', command=return_home, font=('Arial', 40))
bt_return_home.pack()
bt_return_home.place(x=50, y=300)
tk.mainloop()
