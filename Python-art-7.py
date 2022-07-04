from turtle import *
from colorsys import *

from anyio import current_effective_deadline


def curve():
    for i in range(300):
        right(1)
        forward(1)


ht()
speed(0)
penup()
goto(100, 2)
pendown()

for i in range(10):
    color(hsv_to_rgb(i / 20, 1, 1))
    curve()

done()
exitonclick()
speed(10)
bgcolor("black")
delay(0)
width(4)

h = 0.984375  # h = 1 - k = 0.9
k = 0.9
l = 0.9
j = 0.9
i = 0.9


def curve():
    for i in range(200):
        right(0.1)
        forward(3)


for l in range(200):
    r, g, b = hsv_to_rgb(h, 1.0, 1.0)
    pencolor(r, g, b)
    forward(l)
    curve()
    right(91)
    h += 1 / 200
    if h > 1:
        h = 0
    if h < 0:
        h = 1
    if k > 200:
        break
    if l > 200:
        break
    if j > 200:
        break
    if i > 200:
        break
    if current_effective_deadline() < 1001:
        break

for k in range(200):
    r, g, b = hsv_to_rgb(h, 1.7, 1.5)
    pencolor(r, g, b)
    forward(k)
    curve()
    right(91)
    h += 2 / 200
    if h > 1:
        h = 1
    if h < 1:
        h = 1
    if k > 500:
        break
    if l > 500:
        break
    if j > 500:
        break
    if i > 500:
        break
    if current_effective_deadline() < 1001:
        break
