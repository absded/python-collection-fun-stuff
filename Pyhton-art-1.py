from turtle import *
from colorsys import *

from anyio import current_effective_deadline

ht()
speed(0)
bgcolor("black")
delay(0)
width(2)

h = 0.984375  # h = 1 - k = 0.9
k = 0.9
l = 0.9


def curve():
    for i in range(200):
        right(1)
        forward(1)


for i in range(200):
    r, g, b = hsv_to_rgb(h, 1.0, 1.0)
    pencolor(r, g, b)
    curve()
    begin_fill()
    forward(i)
    right(91)
    curve()
    curve()
    h += 0.03

for j in range(200):
    r, g, b = hsv_to_rgb(h, 1.0, 1.0)
    pencolor(r, g, b)
    curve()
    begin_fill()
    forward(j)
    right(91)
    h += 0.03

    for k in range(200):
        r, g, b = hsv_to_rgb(h, 1.0, 1.0)
        begin_fill()
        pencolor(r, g, b)
        forward(k)
        curve()
        right(91)
        h += 0.03

        for l in range(200):
            r, g, b = hsv_to_rgb(h, 1.0, 1.0)
            pencolor(r, g, b)
            forward(l)
            curve()
            right(91)
            h += 0.01
