while True:
    head = eval(input('头数:'))
    feet = eval(input('脚数:'))
    hare = (feet - head * 2) / 2
    chicken = head - hare
    print('兔子有%s只,鸡有%s只' % (hare, chicken))