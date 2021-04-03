from tkinter import *
import time
def get_time():
    t=time.localtime()

tk = Tk()
canvas = Canvas(tk, width=500, height=500)
canvas.pack()
bt = Button(tk, text='获取时间')
bt.pack()
h_m_s=canvas.create_text(250,250,text='')
tk.mainloop()
