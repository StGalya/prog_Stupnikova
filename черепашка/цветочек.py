import turtle

turtle.shape('turtle')

x=360
for i in range (3):
    for j in range (360):
        turtle.forward(1)
        turtle.left(1)
    turtle.right(2)
    for k in range (360):
        turtle.right(1)
        turtle.forward(1)
    turtle.left(60)
    

