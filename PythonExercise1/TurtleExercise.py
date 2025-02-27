import turtle
turtle.pensize(5)
turtle.right(45)
for x in range(0,9):
    if x < 4:
        turtle.forward(100)
        turtle.left(90)
    elif x>4:
        turtle.backward(100)
        turtle.left(90)
turtle.done()

