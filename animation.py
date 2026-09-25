import turtle
import colorsys

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Python Animation")

# Turtle setup
pen = turtle.Turtle()
pen.speed(0)
pen.width(2)

h = 0

for i in range(360):
    color = colorsys.hsv_to_rgb(h, 1, 1)
    pen.pencolor(color)

    pen.forward(i)
    pen.left(59)

    h += 0.005

pen.hideturtle()
turtle.done()
