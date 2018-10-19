from tkinter import *
from random import randrange as rnd, choice
root = Tk()
root.geometry('800x600')
canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)

color=['red','green','yellow','blue','black','pink']
def left_click(event):
    canv.create_oval(200, 200, 500, 500, fill = choice(color))

def right_click(event):
    canv.delete(ALL)

canv.bind('<Button-1>', left_click)
canv.bind('<Button-3>', right_click)

mainloop()
