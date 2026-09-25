import turtle
import colorsys

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Colorful Heart")

t = turtle.Turtle()
t.speed(0)
t.width(3)

h = 0

for i in range(360):
    color = colorsys.hsv_to_rgb(h, 1, 1)
    t.pencolor(color)

    t.penup()
    t.goto(0, 0)
    t.pendown()

    t.setheading(i)
    t.forward(2)

    # Draw heart
    t.begin_fill()
    t.left(140)
    t.forward(111.65)
    t.circle(-55.82, 200)
    t.left(120)
    t.circle(-55.82, 200)
    t.forward(111.65)
    t.end_fill()

    h += 0.003

t.hideturtle()
turtle.done()