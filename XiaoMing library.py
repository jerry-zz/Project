from tkinter import *

tk = Tk()
canvas = Canvas(tk, width=500, height=500, bg='black')
canvas.pack()
canvas.create_text(250, 100, text='欢迎来到小明图书馆!', font=('Arial', 40), fill='yellow')


def all_book():
    tk_all_book = Tk()
    canvas = Canvas(tk_all_book, width=500, height=500, bg='black')
    canvas.pack()
    canvas.create_text(250, 50, text='全部图书', font=('Arial', 70), fill='blue')
    bt_break_all_book = Button(tk_all_book, width=20, height=5, text='退出', fg='red', command=tk_all_book.quit)
    bt_break_all_book.pack()
    bt_break_all_book.place(x=300, y=400)


bt_all_book = Button(tk, width=20, height=5, text='所有图书', command=all_book)
bt_all_book.pack()
bt_all_book.place(x=50, y=300)
bt_break = Button(tk, width=20, height=5, text='退出', fg='red', command=tk.quit)
bt_break.pack()
bt_break.place(x=300, y=300)
tk.mainloop()
