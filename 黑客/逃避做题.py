import random
from tkinter import *

mainloop = True
while mainloop == True:
    def yes():
        global mainloop
        mainloop = False
        tk.quit()


    def no():
        x = random.randint(0, 400)
        y = random.randint(0, 400)
        bt_no.place(x=x, y=y)


    tk = Tk()
    tk.title('请假书')
    tk.resizable(0, 0)
    canvas = Canvas(tk, width=500, height=500, bg='black', highlightthickness=0)
    canvas.pack()
    canvas.create_text(250, 100, text='''我不想再做题了,
   您老同意否?''', font=('Arial', 50), fill='white')
    canvas.create_text(180, 450, text='注:不要试图关掉我,你做不到.', font=('Arial', 20), fill='red')
    bt_yes = Button(tk, text='同意', font=('Arial', 50), command=yes)
    bt_yes.pack()
    bt_yes.place(x=30, y=250)
    bt_no = Button(tk, text='不同意', font=('Arial', 50), command=no)
    bt_no.pack()
    bt_no.place(x=230, y=250)
    tk.mainloop()
tk_886 = Tk()
tk_886.resizable(0, 0)
tk_886.title('感谢')
canvas_886 = Canvas(tk_886, width=500, height=150, bg='yellow', highlightthickness=0)
canvas_886.pack()
canvas_886.create_text(250, 25, text='感谢母亲,拜拜!－＝≡ヘ(*・ω・)ノ', font=('Arial', 25))


def ok():
    tk_886.quit()


bt_ok = Button(tk_886, text='好的', font=('Arial', 30), command=ok)
bt_ok.pack()
bt_ok.place(x=200, y=50)
tk_886.mainloop()
