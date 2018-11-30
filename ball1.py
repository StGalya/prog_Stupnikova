from tkinter import *

import random
import time

counter = 0
color = ['red', 'green', 'yellow', 'blue', 'black', 'pink']

    

def tick():
    global x_centre_ball, y_centre_ball, r_ball, counter
    root.after(1000, tick)
    canv.delete(ALL)
    x_centre_ball = random.randint(100, 700)
    y_centre_ball = random.randint(100, 500)
    r_ball = random.randint(20, 100)
    canv.create_oval(x_centre_ball - r_ball, y_centre_ball - r_ball,
                     x_centre_ball + r_ball,
                     y_centre_ball + r_ball, fill=random.choice(color))
    canv.create_text(150, 50, text="Попадания: " + str(counter),
                     font='Arial 20')


def click(event):
    global x_centre_ball, y_centre_ball
    xc = event.x
    yc = event.y
    global counter
    if (x_centre_ball - xc) ** 2 + (y_centre_ball - yc) ** 2 < r_ball ** 2:
        counter += 1
        canv.delete(ALL)
        x_centre_ball = 1000
        y_centre_ball = 1000
        canv.create_text(150, 50,
                         text="Попадания: " + str(counter), font='Arial 20')


root = Tk()
root.geometry('800x600')

canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)

root.after_idle(tick)
root.bind('<Button-1>', click)
root.mainloop()