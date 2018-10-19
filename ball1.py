from tkinter import *
from random import randrange as rnd, choice
import random
import time
counter=0
color=['red','green','yellow','blue','black','pink']

def tick():
    global x,y,r
    root.after(1000, tick)
    canv.delete(ALL)
    x=random.randint(100,700)
    y=random.randint(100,500)
    r=random.randint(20,100)
    canv.create_oval(x-r, y-r, x+r, y+r, fill = choice(color))
    canv.create_text(300,50, text=counter)
    canv.create_text(150,50, text="Попадания:", font = 'Arial 20')
def click(event):
    xc=event.x
    yc=event.y
    global counter
    if (x-xc)**2+(y-yc)**2 < r**2:
        counter+=1

root = Tk()
root.geometry('800x600')

canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)

root.after_idle(tick)
root.bind('<Button-1>', click)



root.mainloop()
