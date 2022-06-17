from turtle import *

turtle = [Turtle() for i in range(6)]

x = 180
bgcolor("#1E0394")
color("#ff5f1f")
pensize(3)
ht()
pu()
fd(x)
seth(90)
pd()
circle(x / 2, 180)
c = ["brown2", "gold"]

for index, t in enumerate(turtle):
    t.color(c[index % 2])
    t.pu()
    t.fd(x / 5)
    t.seth(90)
    t.pd()
    t.circle(x / 8, 180)
    t.pensize(3)
    t.pu()
    t.circle(x * 3 / 3, 180)
    t.color(c[1])
    t.circle((x * 2 / 6 + x / 2) / 2, 180)
