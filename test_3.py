import turtle
def move(s):
    turtle.forward(s)
    turtle.left(90)
def draw_square(s):
    for i in range(4):
        move(s)
def draw_squareColor(s, color):
    turtle.color(color)
    turtle.begin_fill()
    for i in range(4):
        move(s)
    turtle.end_fill()

turtle.speed(1)

draw_squareColor(60, 'blue')
turtle.goto(150,150)
draw_squareColor(120, 'red')