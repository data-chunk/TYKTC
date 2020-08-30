#ColorSpiral.py
import turtle

t = turtle.Pen()
turtle.bgcolor("black")
t.speed(0)
sides = 3
colors = ["red", "yellow", "blue", "orange", "green", "purple"]
for x in range(720):
    t.pencolor(colors[x % sides])
    t.forward(x * 3 / sides + x)
    t.left(360 / sides + 1)
    t.width(x * sides / 100)