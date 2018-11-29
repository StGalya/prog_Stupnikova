from tkinter import *
import graphics as gr
import time

window = gr.GraphWin("picture.1", 450, 450)


def draw_grass():
    tr = gr.Rectangle(gr.Point(0, 240), gr.Point(450, 450))
    tr.draw(window)
    tr.setFill('green')


def draw_circle(x, y, r, col):
    obj = gr.Circle(gr.Point(x, y), r)
    obj.setFill(col)
    obj.draw(window)

def make_circle(x, y, r, col):
    obj = gr.Circle(gr.Point(x, y), r)
    obj.setFill(col)
    obj.draw(window)
    return(obj)
    
def draw_line(x1, y1, x2, y2):
    obj = gr.Line(gr.Point(x1, y1), gr.Point(x2, y2))
    obj.draw(window)
    
    
def draw_face_left():
    facel = gr.Circle(gr.Point(200, 250), 50)
    facel.draw(window)
    facel.setFill('yellow')


def draw_eye_face_left():
    draw_circle(180, 235, 10, 'forestgreen')
    draw_circle(220, 235, 10, 'forestgreen')
    draw_circle(180, 235, 3, 'black')
    draw_circle(220, 235, 3, 'black')


def draw_leg_face_left():
    draw_line(180, 295, 170, 320)
    draw_line(220, 295, 230, 320)


def draw_arm_face_left():
    draw_line(154, 265, 143, 290)
    draw_line(246, 265, 257, 290)


def draw_face_right():
    face_left_girl = gr.Circle(gr.Point(320, 250), 50)
    face_left_girl.draw(window)
    face_left_girl.setFill('yellow')


def draw_eye_face_right():
    draw_circle(300, 235, 10, 'mediumturquoise')
    draw_circle(340, 235, 10, 'mediumturquoise')
    draw_circle(300, 235, 3, 'black')
    draw_circle(340, 235, 3, 'black')


def draw_leg_face_right():
    draw_line(300, 295, 290, 320)
    draw_line(340, 295, 350, 320)


def draw_arm_face_right():
    draw_line(274, 265, 257, 290)
    draw_line(366, 265, 386, 290)


def draw_mouths():
    draw_line(173, 262, 185, 272)
    draw_line(340, 262, 330, 272)


skam = gr.Rectangle(gr.Point(130, 170), gr.Point(390, 200))
skam.draw(window)
skam.setFill('sienna')


def draw_flower():
    draw_circle(101, 320, 15, 'magenta')
    draw_circle(128, 325, 15, 'magenta')    
    draw_circle(133, 353, 15, 'magenta')
    draw_circle(108, 368, 15, 'magenta')
    draw_circle(88, 346, 15, 'magenta')
    draw_circle(112, 342, 20, 'deeppink')


def draw_cloud(x, y, r):
    draw_circle(x, y, r, 'skyblue')  
    draw_circle(x - 24, y, r + 1, 'skyblue')
    draw_circle(x - 29, y - 4, r - 2, 'skyblue')  
    draw_circle(x - 14, y - 6, r + 3, 'skyblue')
    draw_circle(x - 14, y - 6, r + 2, 'skyblue')
    draw_circle(x - 4, y - 4, r, 'skyblue')


def moov_cloud():
    ob1 = make_circle(399, 110, 20, 'skyblue')
    ob2 = make_circle(399 - 24, 110, 20 + 1, 'skyblue')
    ob3 = make_circle(399 - 29, 110 - 4, 20 - 2, 'skyblue')
    ob4 = make_circle(399 - 14, 110 - 6, 20 + 2, 'skyblue')
    ob5 = make_circle(399 - 14, 110 - 6, 20 + 2, 'skyblue')
    ob6 = make_circle(399 - 4, 110 - 4, 20, 'skyblue')
    for i in range(50):
        time.sleep(0.1)
        ob1.move(2, 0)
        ob2.move(2, 0)
        ob3.move(2, 0)
        ob4.move(2, 0)
        ob5.move(2, 0)
        ob6.move(2, 0)


def draw_picture():
    draw_grass()
    draw_face_left()
    draw_eye_face_left()
    draw_leg_face_left()
    draw_arm_face_left()
    draw_face_right()
    draw_eye_face_right()
    draw_leg_face_right()
    draw_arm_face_right()
    draw_mouths()
    draw_flower()
    draw_cloud(119, 80, 20)
    draw_cloud(249, 40, 20)
    moov_cloud()
draw_picture()

window.getMouse()
window.close()



