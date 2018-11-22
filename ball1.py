from tkinter import *
from random import randrange as rnd, choice
import random
import time
counter = 0
color = ['red', 'green', 'yellow', 'blue', 'black', 'pink']


def tick():
    global xx, yy, r, counter
    root.after(1000, tick)
    canv.delete(ALL)
    xx = random.randint(100, 700)
    yy = random.randint(100, 500)
    r = random.randint(20, 100)
    canv.create_oval(xx-r, yy-r, xx+r, yy+r, fill=choice(color))
    canv.create_text(150, 50, text="Попадания: " + str(counter),
                     font='Arial 20')


def click(event):
    global xx, yy
    xc = event.x
    yc = event.y
    global counter
    if (xx-xc)**2+(yy-yc)**2 < r**2:
        counter += 1
        canv.delete(ALL)
        xx = 1000
        yy = 1000
        canv.create_text(150, 50,
        text="Попадания: " + str(counter), font='Arial 20')         
root = Tk()
root.geometry('800x600')

canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)

root.after_idle(tick)
root.bind('<Button-1>', click)
root.mainloop()

