from tkinter import *
import graphics as gr
import random
root = Tk()
root.geometry("1000x600")
canvas = Canvas(root, bg='white')

canvas.pack(fill=BOTH, expand=1)

balls = []
for i in range(5):
    color = gr.color_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    xb = random.randint(50, 250)
    yb = random.randint(50, 250)
    rb = random.randint(20, 50)
    dxb = random.randint(3, 10)
    dyb = random.randint(3, 10)
    ovall = canvas.create_oval(xb-rb, yb-rb, xb+rb, yb+rb, fill=color)
    ball = [xb, yb, rb, dxb, dyb, ovall]
    balls.append(ball)


def is_collide(x, range, side):
    if side == 1:
        if x > range - 100:
            return (True)
    if side == 0:
        if x < 0:
            return (True)
    return(False)


def tick_handler():
    global balls
    for i in range(len(balls)):
        x, y, r, dx, dy, ovall = balls[i]
        if is_collide(x, 1000, 1) is True:
            x = 900
            dx = -dx
        if is_collide(x, 0, 0) is True:
            x = 0
            dx = -dx
        if is_collide(y, 600, 1) is True:
            y = 500
            dy = -dy
        if is_collide(y, 0, 0) is True:
            y = 0
            dy = -dy
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
    sleep_dt = 110 - 10*speed
    root.after(sleep_dt, time_handler)


def unfreezer():
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
