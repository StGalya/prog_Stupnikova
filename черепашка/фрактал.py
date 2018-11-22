import turtle
turtle.shape('turtle')

def fractal():
    turtle.forward(20)
    turtle.left(60)
    turtle.forward(20)
    turtle.right(120)
    turtle.forward(20)
    turtle.left(60)
    turtle.forward(20)
    
def fractal2():
    for i in range (3):
        fractal()
        turtle.left(60)
        fractal()
        turtle.right(120)
        fractal()
        turtle.left(60)
        fractal()
        turtle.right(120)
fractal2()