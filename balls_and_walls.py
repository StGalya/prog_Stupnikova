from tkinter import *
from random import randrange as rnd, choice
import random
color = ['red', 'green', 'yellow', 'blue', 'black', 'pink']

root = Tk()
root.geometry("300x300")
canvas = Canvas(root, bg='white')

canvas.pack(fill=BOTH, expand=1)

balls = []
for i in range(5):
    xb = random.randint(50, 250)
    yb = random.randint(50, 250)
    rb = random.randint(20, 50)
    dxb = random.randint(3, 10)
    dyb = random.randint(3, 10)
    ovall = canvas.create_oval(xb-rb, yb-rb, xb+rb, yb+rb, fill=choice(color))
    ball = [xb, yb, rb, dxb, dyb, ovall]
    balls.append(ball)


def tick_handler():
    global balls
    for i in range(len(balls)):
        x, y, r, dx, dy, ovall = balls[i]
        if x < 0:
            dx = -dx
            x = 0
        elif x > 300-40:
            dx = -dx
            x = 300-40
        if y < 0:
            dy = -dy
            y = 0
        elif y > 300-40:
            dy = -dy
            y = 300-40
        x = x + dx
        y = y + dy
        canvas.move(ovall, dx, dy)
        balls[i] = [x, y, r, dx, dy, ovall]


def time_handler():
    global freeze
    speed = speed_scale.get()
    if speed == 0:

        freeze = True
        return
    tick_handler()
    sleep_dt = 1100 - 100*speed
    root.after(sleep_dt, time_handler)


def unfreezer(event):
    global freeze
    if freeze is True:
        speed = speed_scale.get()
        if speed != 0:
            freeze = False
            root.after(0, time_handler)


speed_scale = Scale(root, orient=HORIZONTAL, length=300,
from_=0, to=10, tickinterval=1, resolution=1)
speed_scale.pack()

speed_scale.set(1)
freeze = False

root.after(10, time_handler)
speed_scale.bind("<Motion>", unfreezer)

root.mainloop()
