from tkinter import *
import graphics as gr
import time



window = gr.GraphWin("picture.1", 450, 450)

def draw_grass():
    tr = gr.Rectangle(gr.Point(0, 240), gr.Point(450, 450))
    tr.draw(window)
    tr.setFill('green')

def draw_face_left():
    facel = gr.Circle(gr.Point(200, 250), 50)
    facel.draw(window)
    facel.setFill('yellow')

def draw_eye_face_left():
    eyell = gr.Circle(gr.Point(180, 235), 10)
    eyell.draw(window)
    eyell.setFill('forestgreen')
    eyerl = gr.Circle(gr.Point(220, 235), 10)
    eyerl.draw(window)
    eyerl.setFill('forestgreen')


    eyezll = gr.Circle(gr.Point(180, 235), 3)
    eyezll.draw(window)
    eyezll.setFill('black')
    eyezrl = gr.Circle(gr.Point(220, 235), 3)
    eyezrl.draw(window)
    eyezrl.setFill('black')

def draw_leg_face_left():
    nll = gr.Line(gr.Point(180, 295), gr.Point(170, 320))
    nll.draw(window)
    nrl = gr.Line(gr.Point(220, 295), gr.Point(230, 320))
    nrl.draw(window)

def draw_arm_face_left():
    rll = gr.Line(gr.Point(154, 265), gr.Point(143, 290))
    rll.draw(window)
    rrl = gr.Line(gr.Point(246, 265), gr.Point(257, 290))
    rrl.draw(window)

def draw_face_right():
    face2 = gr.Circle(gr.Point(320, 250), 50)
    face2.draw(window)
    face2.setFill('yellow')

def draw_eye_face_right():
    eyelr = gr.Circle(gr.Point(300, 235), 10)
    eyelr.draw(window)
    eyelr.setFill('mediumturquoise')
    eyerr = gr.Circle(gr.Point(340, 235), 10)
    eyerr.draw(window)
    eyerr.setFill('mediumturquoise')

    eyezlr = gr.Circle(gr.Point(300, 235), 3)
    eyezlr.draw(window)
    eyezlr.setFill('black')
    eyezrr = gr.Circle(gr.Point(340, 235), 3)
    eyezrr.draw(window)
    eyezrr.setFill('black')

def draw_leg_face_right():
    nlr = gr.Line(gr.Point(300, 295), gr.Point(290, 320))
    nlr.draw(window)
    nrr = gr.Line(gr.Point(340, 295), gr.Point(350, 320))
    nrr.draw(window)

def draw_arm_face_right():
    rlr = gr.Line(gr.Point(274, 265), gr.Point(257, 290))
    rlr.draw(window)
    rrr = gr.Line(gr.Point(366, 265), gr.Point(386, 290))
    rrr.draw(window)

def draw_mouths():
    mth1 = gr.Line(gr.Point(173, 262), gr.Point(185, 272))
    mth1.draw(window)
    mth2 = gr.Line(gr.Point(340, 262), gr.Point(330, 272))
    mth2.draw(window)





skam = gr.Rectangle(gr.Point(130, 170), gr.Point(390, 200))
skam.draw(window)
skam.setFill('sienna')

def draw_flower():
    ob = gr.Circle(gr.Point(101, 320), 15)
    ob.draw(window)
    ob.setFill('magenta')
    ob = gr.Circle(gr.Point(128, 325), 15)
    ob.draw(window)
    ob.setFill('magenta')
    ob = gr.Circle(gr.Point(133, 353), 15)
    ob.draw(window)
    ob.setFill('magenta')
    ob = gr.Circle(gr.Point(108, 368), 15)
    ob.draw(window)
    ob.setFill('magenta')
    ob = gr.Circle(gr.Point(88, 346), 15)
    ob.draw(window)
    ob.setFill('magenta')
    ob = gr.Circle(gr.Point(112, 342), 20)
    ob.draw(window)
    ob.setFill('deeppink')

def draw_cloud(x,y,r):
    ob1 = gr.Circle(gr.Point(x, y), r)
    ob1.draw(window)
    ob1.setFill('skyblue')
    
    ob2 = gr.Circle(gr.Point(x-24, y), r+1)
    ob2.draw(window)
    ob2.setFill('skyblue')
    
    ob3 = gr.Circle(gr.Point(x-29, y-4), r-2)
    ob3.draw(window)
    ob3.setFill('skyblue')
    
    ob4 = gr.Circle(gr.Point(x-14,y-6 ), r+3)
    ob4.draw(window)
    ob4.setFill('skyblue')
    
    ob5 = gr.Circle(gr.Point(x-14,y-6 ), r+2)
    ob5.draw(window)
    ob5.setFill('skyblue')
   
    ob6 = gr.Circle(gr.Point(x-4,y-4), r)
    ob6.draw(window)
    ob6.setFill('skyblue')

def moov_cloud():

    ob1 = gr.Circle(gr.Point(399, 110), 20)
    ob1.draw(window)
    ob1.setFill('skyblue')
    
    ob2 = gr.Circle(gr.Point(399-24, 110), 20+1)
    ob2.draw(window)
    ob2.setFill('skyblue')
    
    ob3 = gr.Circle(gr.Point(399-29, 110-4), 20-2)
    ob3.draw(window)
    ob3.setFill('skyblue')
    
    ob4 = gr.Circle(gr.Point(399-14,110-6 ), 20+3)
    ob4.draw(window)
    ob4.setFill('skyblue')
    
    ob5 = gr.Circle(gr.Point(399-14,110-6 ), 20+2)
    ob5.draw(window)
    ob5.setFill('skyblue')
   
    ob6 = gr.Circle(gr.Point(399-4,110-4), 20)
    ob6.draw(window)
    ob6.setFill('skyblue')
    
    for i in range(50):
        time.sleep(0.1)
        ob1.move(2,0)
        ob2.move(2,0)
        ob3.move(2,0)
        ob4.move(2,0)
        ob5.move(2,0)
        ob6.move(2,0)

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
    draw_cloud(119,80,20)
    draw_cloud(249,40,20)
    
    moov_cloud()
    
draw_picture()

window.getMouse()
window.close()



