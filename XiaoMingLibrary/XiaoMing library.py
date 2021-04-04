from tkinter import *

tk = Tk()
tk.resizable(0, 0)
tk.title('主页')
canvas = Canvas(tk, width=500, height=500, bg='black')
canvas.pack()
canvas.create_text(250, 100, text='欢迎来到小明图书馆!', font=('Arial', 40), fill='yellow')


def all_book():
    tk_all_book = Tk()
    tk_all_book.resizable(0, 0)

    def story():
        tk_story = Tk()
        tk_story.resizable(0, 0)

        def tortoise_hare_race():
            tortoise_hare_race_file = open(
                "C:\\Users\\jerry\\Documents\\GitHub\\Project\\XiaoMingLibrary\\Libraries\\童话_龟兔赛跑.txt",
                encoding='utf8').read()
            tk_tortoise_hare_race = Tk()
            tk_tortoise_hare_race.resizable(0, 0)
            tk_tortoise_hare_race.title('龟兔赛跑')
            canvas = Canvas(tk_tortoise_hare_race, width=700, height=300)
            canvas.pack()
            canvas.create_text(350, 50, text='龟兔赛跑', font=('Arial', 50))
            canvas.create_text(350, 170, text=tortoise_hare_race_file, font=('Arial', 11))

        def Waiting_for_another_hare():
            Waiting_for_another_hare_file = open(
                "C:\\Users\\jerry\\Documents\\GitHub\\Project\XiaoMingLibrary\\Libraries\\童话_农夫与蛇.txt",
                encoding='utf8').read()
            tk_Waiting_for_another_hare = Tk()
            tk_Waiting_for_another_hare.resizable(0, 0)
            tk_Waiting_for_another_hare.title('守株待兔')
            canvas = Canvas(tk_Waiting_for_another_hare, width=640, height=250)
            canvas.pack()
            canvas.create_text(320, 50, text='守株待兔', font=('Arial', 50))
            canvas.create_text(320, 170, text=Waiting_for_another_hare_file, font=('Arial', 10))

        def B():
            tk_ = Tk()
            canvas = Canvas(tk_, width=500, height=500)
            canvas.pack()

        def C():
            tk_ = Tk()
            canvas = Canvas(tk_, width=500, height=500)
            canvas.pack()

        def D():
            tk_ = Tk()
            canvas = Canvas(tk_, width=500, height=500)
            canvas.pack()

        tk_story.title('童话类')
        canvas = Canvas(tk_story, width=500, height=500, bg='black')
        canvas.pack()
        canvas.create_text(250, 50, text='童话类', font=('Arial', 70), fill='white')
        bt_quit_story = Button(tk_story, width=10, height=1, text='退出', fg='red', command=tk_story.quit)
        bt_quit_story.pack()
        bt_quit_story.place(x=400, y=450)
        bt_tortoise_hare_race = Button(tk_story, width=10, height=2, text='龟兔赛跑', command=tortoise_hare_race)
        bt_tortoise_hare_race.pack()
        bt_tortoise_hare_race.place(x=0, y=100)
        bt_Waiting_for_another_hare = Button(tk_story, width=10, height=2, text='守株待兔',
                                             command=Waiting_for_another_hare)
        bt_Waiting_for_another_hare.pack()
        bt_Waiting_for_another_hare.place(x=0, y=150)
        bt_ = Button(tk_story, width=10, height=2, text='', command=B)
        bt_.pack()
        bt_.place(x=0, y=200)
        bt_ = Button(tk_story, width=10, height=2, text='', command=C)
        bt_.pack()
        bt_.place(x=0, y=250)
        bt_ = Button(tk_story, width=10, height=2, text='', command=D)
        bt_.pack()
        bt_.place(x=0, y=300)

    def prose():
        tk_prose = Tk()
        tk_prose.resizable(0, 0)

        def fast():
            fast_file = open("C:\\Users\\jerry\\Documents\\GitHub\\Project\\XiaoMingLibrary\\Libraries\\散文_匆匆.txt",
                             encoding='utf8').read()
            tk_fast = Tk()
            tk_fast.resizable(0, 0)
            tk_fast.title('匆匆')
            canvas = Canvas(tk_fast, width=740, height=400)
            canvas.pack()
            canvas.create_text(370, 50, text='匆匆', font=('Arial', 50))
            canvas.create_text(370, 250, text=fast_file, font=('Arial', 12))

        def C():
            tk_ = Tk()
            canvas = Canvas(tk_, width=500, height=500)
            canvas.pack()

        def D():
            tk_ = Tk()
            canvas = Canvas(tk_, width=500, height=500)
            canvas.pack()

        tk_prose.title('散文类')
        canvas = Canvas(tk_prose, width=500, height=500, bg='black')
        canvas.pack()
        canvas.create_text(250, 50, text='散文类', font=('Arial', 70), fill='white')
        bt_quit_prose = Button(tk_prose, width=10, height=1, text='退出', fg='red', command=tk_prose.quit)
        bt_quit_prose.pack()
        bt_quit_prose.place(x=400, y=450)
        bt_fast = Button(tk_prose, width=10, height=2, text='匆匆', command=fast)
        bt_fast.pack()
        bt_fast.place(x=0, y=100)
        bt_ = Button(tk_prose, width=10, height=2, text='', command=C)
        bt_.pack()
        bt_.place(x=0, y=150)
        bt_ = Button(tk_prose, width=10, height=2, text='', command=D)
        bt_.pack()
        bt_.place(x=0, y=200)

    tk_all_book.title('全部图书')
    canvas = Canvas(tk_all_book, width=500, height=500, bg='black')
    canvas.pack()
    canvas.create_text(250, 50, text='全部图书', font=('Arial', 70), fill='blue')
    bt_quit_all_book = Button(tk_all_book, width=10, height=1, text='退出', fg='red', command=tk_all_book.quit)
    bt_quit_all_book.pack()
    bt_quit_all_book.place(x=400, y=450)
    bt_story = Button(tk_all_book, width=20, height=5, text='童话类', command=story)
    bt_story.pack()
    bt_story.place(x=0, y=100)
    bt_prose = Button(tk_all_book, width=20, height=5, text='散文类', command=prose)
    bt_prose.pack()
    bt_prose.place(x=0, y=200)


bt_all_book = Button(tk, width=20, height=5, text='所有图书', command=all_book)
bt_all_book.pack()
bt_all_book.place(x=50, y=300)
bt_quit = Button(tk, width=20, height=5, text='退出', fg='red', command=tk.quit)
bt_quit.pack()
bt_quit.place(x=300, y=300)
tk.mainloop()
