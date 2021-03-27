from tkinter import *

tk = Tk()
canvas = Canvas(tk, width=500, height=500, bg='black')
canvas.pack()
canvas.create_text(250, 100, text='欢迎来到小明图书馆!', font=('Arial', 40), fill='yellow')


def all_book():
    tk_all_book = Tk()

    def story():
        tk_story = Tk()

        def tortoise_hare_race():
            tk_tortoise_hare_race = Tk()
            canvas = Canvas(tk_tortoise_hare_race, width=590, height=300)
            canvas.pack()
            canvas.create_text(295, 50, text='龟兔赛跑', font=('Arial', 40))
            canvas.create_text(300, 100, text='在一个风和日丽的上午，小兔和小乌龟去山上看鲜花，小兔一蹦一跳地跑在前面，小乌龟慢吞', font=('Arial', 10))
            canvas.create_text(280, 115, text='吞地在后面爬，小兔觉得小乌龟爬得太慢了，就傲慢地对小乌龟说：“嗨，小乌龟，我们来一', font=('Arial', 10))
            canvas.create_text(180, 130, text='场比赛吧，看看谁先到达山顶。”“哼，比就比。”小乌龟说。', font=('Arial', 10))
            canvas.create_text(290, 145, text='于是，它们请来斑马当裁判。枪声一响，小兔就像离弦的剑一样跑了出去，一下就不见了踪', font=('Arial', 10))
            canvas.create_text(280, 160, text='影，小兔跑啊跑，回头一看，小乌龟才刚刚爬过起跑线，心想：“小乌龟爬得太慢，一定追不', font=('Arial', 10))
            canvas.create_text(150, 175, text='上我，我也有点累了，休息一下睡一会儿也没关系。”', font=('Arial', 10))
            canvas.create_text(300, 190, text='小兔躺在草地上呼呼大睡，过了一会儿，小乌龟追了上来，它看见小兔在睡觉，便不顾劳累，', font=('Arial', 10))
            canvas.create_text(95, 205, text='鼓足劲，努力地向终点爬去。', font=('Arial', 10))
            canvas.create_text(300, 220, text='小兔一觉醒来，还不见小乌龟的踪影，便不紧不慢地向山顶跑去，到了终点，小兔看见大家都', font=('Arial', 10))
            canvas.create_text(250, 235, text='在向小乌龟表示祝贺，惭愧地低下了头，灰溜溜地走了，心想：“我以后再也不能骄傲了。”', font=('Arial', 10))

        def A():
            tk_ = Tk()
            canvas = Canvas(tk_, width=3000, height=700)
            canvas.pack()

        def B():
            tk_ = Tk()
            canvas = Canvas(tk_, width=3000, height=700)
            canvas.pack()

        def C():
            tk_ = Tk()
            canvas = Canvas(tk_, width=3000, height=700)
            canvas.pack()

        def D():
            tk_ = Tk()
            canvas = Canvas(tk_, width=3000, height=700)
            canvas.pack()

        canvas = Canvas(tk_story, width=500, height=500, bg='black')
        canvas.pack()
        canvas.create_text(250, 50, text='童话类', font=('Arial', 70), fill='white')
        bt_quit_story = Button(tk_story, width=10, height=1, text='退出', fg='red', command=tk_story.quit)
        bt_quit_story.pack()
        bt_quit_story.place(x=400, y=450)
        bt_ = Button(tk_story, width=10, height=2, text='龟兔赛跑', command=tortoise_hare_race)
        bt_.pack()
        bt_.place(x=0, y=100)
        bt_ = Button(tk_story, width=10, height=2, text='', command=A)
        bt_.pack()
        bt_.place(x=0, y=150)
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
        canvas = Canvas(tk_prose, width=500, height=500, bg='black')
        canvas.pack()
        canvas.create_text(250, 50, text='散文类', font=('Arial', 70), fill='white')
        bt_quit_prose = Button(tk_prose, width=10, height=1, text='退出', fg='red', command=tk_prose.quit)
        bt_quit_prose.pack()
        bt_quit_prose.place(x=400, y=450)

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
