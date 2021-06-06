import pyautogui as gui

filename = '刷屏用语.txt'
with open(file=filename)as word:
    word = word.read
for i in range(1, 500):
    gui.typewrite(message='%s' % (word))
    gui.hotkey('enter')
