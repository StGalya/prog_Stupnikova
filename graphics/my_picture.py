import graphics as gr

window = gr.GraphWin("picture.1", 450, 450)


def draw_grass():
    grass = gr.Rectangle(gr.Point(0, 240), gr.Point(450, 450))
    grass.draw(window)
    grass.setFill('green')


def draw_face_left():
    face_left_guy = gr.Circle(gr.Point(200, 250), 50)
    face_left_guy.draw(window)
    face_left_guy.setFill('yellow')


def draw_eye_face_left():
    eye_left_guy = gr.Circle(gr.Point(180, 235), 10)
    eye_left_guy.draw(window)
    eye_left_guy.setFill('forestgreen')
    eye_right_guy = gr.Circle(gr.Point(220, 235), 10)
    eye_right_guy.draw(window)
    eye_right_guy.setFill('forestgreen')
    apple_of_left_eye_guy = gr.Circle(gr.Point(180, 235), 3)
    apple_of_left_eye_guy.draw(window)
    apple_of_left_eye_guy.setFill('black')
    apple_of_right_eye_guy = gr.Circle(gr.Point(220, 235), 3)
    apple_of_right_eye_guy.draw(window)
    apple_of_right_eye_guy.setFill('black')


def draw_leg_face_left():
    leg_left_guy = gr.Line(gr.Point(180, 295), gr.Point(170, 320))
    leg_left_guy.draw(window)
    leg_right_guy = gr.Line(gr.Point(220, 295), gr.Point(230, 320))
    leg_right_guy.draw(window)


def draw_arm_face_left():
    arm_left_guy = gr.Line(gr.Point(154, 265), gr.Point(143, 290))
    arm_left_guy.draw(window)
    arm_right_guy = gr.Line(gr.Point(246, 265), gr.Point(257, 290))
    arm_right_guy.draw(window)


def draw_face_right():
    face_left_girl = gr.Circle(gr.Point(320, 250), 50)
    face_left_girl.draw(window)
    face_left_girl.setFill('yellow')


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
    leg_left_girl = gr.Line(gr.Point(300, 295), gr.Point(290, 320))
    leg_left_girl.draw(window)
    leg_right_girl = gr.Line(gr.Point(340, 295), gr.Point(350, 320))
    leg_right_girl.draw(window)


def draw_arm_face_right():
    arm_left_girl = gr.Line(gr.Point(274, 265), gr.Point(257, 290))
    arm_left_girl.draw(window)
    leg_right_girl = gr.Line(gr.Point(366, 265), gr.Point(386, 290))
    leg_right_girl.draw(window)


def draw_mouths():
    mth1 = gr.Line(gr.Point(173, 262), gr.Point(185, 272))
    mth1.draw(window)
    mth2 = gr.Line(gr.Point(340, 262), gr.Point(330, 272))
    mth2.draw(window)


def draw_cloud(x, y, r):
    ob = gr.Circle(gr.Point(x, y), r)
    ob.draw(window)
    ob.setFill('skyblue')
    ob = gr.Circle(gr.Point(x-24, y), r+1)
    ob.draw(window)
    ob.setFill('skyblue')
    ob = gr.Circle(gr.Point(x-29, y-4), r-2)
    ob.draw(window)
    ob.setFill('skyblue')
    ob = gr.Circle(gr.Point(x-14, y-6), r+3)
    ob.draw(window)
    ob.setFill('skyblue')
    ob = gr.Circle(gr.Point(x-14, y-6), r+2)
    ob.draw(window)
    ob.setFill('skyblue')
    ob = gr.Circle(gr.Point(x-4, y-4), r)
    ob.draw(window)
    ob.setFill('skyblue')
skam = gr.Rectangle(gr.Point(130, 170), gr.Point(390, 200))
skam.draw(window)
skam.setFill('sienna')


def draw_flower():
    fl = gr.Circle(gr.Point(101, 320), 15)
    fl.draw(window)
    fl.setFill('magenta')
    fl = gr.Circle(gr.Point(128, 325), 15)
    fl.draw(window)
    fl.setFill('magenta')
    fl = gr.Circle(gr.Point(133, 353), 15)
    fl.draw(window)
    fl.setFill('magenta')
    fl = gr.Circle(gr.Point(108, 368), 15)
    fl.draw(window)
    fl.setFill('magenta')
    fl = gr.Circle(gr.Point(88, 346), 15)
    fl.draw(window)
    fl.setFill('magenta')
    fl = gr.Circle(gr.Point(112, 342), 20)
    fl.draw(window)
    fl.setFill('deeppink')


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
    draw_cloud(399, 110, 20)
draw_picture()

window.getMouse()
window.close()
