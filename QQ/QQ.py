import pyautogui as gui
import time
filename = '刷屏用语.txt'
with open(file=filename, encoding='utf8') as word:
    word = word.read()
    word=(word.split(','))
    num=int(word[0])
    word=word[1]
for i in range(0, num):
    gui.typewrite(message='%s' % (word))
    gui.hotkey('enter')