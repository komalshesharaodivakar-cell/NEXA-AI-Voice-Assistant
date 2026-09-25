import turtle

screen = turtle.Screen()
screen.bgcolor("white")
pen = turtle.Turtle()
pen.speed(5)
pen.pensize(3)

# Face
pen.penup()
pen.goto(0, -100)
pen.pendown()
pen.circle(100)

# Left Eye
pen.penup()
pen.goto(-35, 30)
pen.pendown()
pen.begin_fill()
pen.circle(12)
pen.end_fill()

# Right Eye
pen.penup()
pen.goto(35, 30)
pen.pendown()
pen.begin_fill()
pen.circle(12)
pen.end_fill()

# Mouth
pen.penup()
pen.goto(-30, -30)
pen.setheading(-60)
pen.pendown()
pen.circle(35, 120)

# Hair
pen.penup()
pen.goto(-90, 90)
pen.setheading(0)
pen.pendown()
for i in range(18):
    pen.forward(10)
    pen.right(100)
    pen.forward(10)
    pen.left(100)

pen.hideturtle()
turtle.done()