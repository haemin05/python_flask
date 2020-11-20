import turtle
'''
color('red', 'yellow')
shape("circle")
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()
'''
turtle.color('black', 'blue')
turtle.begin_fill()

def koch(t, order, size):
    """
       Make turtle t draw a Koch fractal of 'order' and 'size'.
       Leave the turtle facing the same direction.
    """

    if order == 0:  # The base case is just a straight line
        t.forward(size)
    else:
        koch(t, order - 1, size // 3)  # Go 1/3 of the way
        t.left(60)
        koch(t, order - 1, size // 3)
        t.right(120)
        koch(t, order - 1, size // 3)
        t.left(60)
        koch(t, order - 1, size // 3)

def koch2(t, order, size):
    if order == 0:  # The base case is just a straight line
        t.backward(size)
    else:
        koch2(t, order - 1, size // 3)  # Go 1/3 of the way
        t.left(60)
        koch2(t, order - 1, size // 3)
        t.right(120)
        koch2(t, order - 1, size // 3)
        t.left(60)
        koch2(t, order - 1, size // 3)

# ----------
size = 400
turtle.penup()
turtle.goto(-size // 2, 0)
turtle.pendown()
turtle.speed(300)
koch(turtle, 5, size)
koch2(turtle, 5, size)

turtle.end_fill()
turtle.done()