import turtle

turtle.shape('turtle')

y=1
x=360
turtle.left(90)
for i in range (7):
    for j in range (360):
        turtle.left(1)
        turtle.forward(y)
    
    for k in range (360):
        turtle.right(1)
        turtle.forward(y)
    
    y=y+0.1
   
    
