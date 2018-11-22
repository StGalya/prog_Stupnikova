import turtle

turtle.shape('turtle')

n=3
x=15

turtle.left(30)
for i in range (10):
    for j in range (n):
        turtle.right(360/n)
        turtle.forward(x)
    n=n+1
    x=x+10
    turtle.left(60)
    turtle.penup()
    turtle.forward(5)
    turtle.pendown()
    turtle.right(60)
    
