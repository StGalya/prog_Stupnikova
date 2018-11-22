import turtle

turtle.shape('turtle')

for j in range (10):
    for i in range (4):
        turtle.pendown()
        turtle.forward(20+j*20)
        turtle.left(90)
        turtle.penup()
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.right(90)
