from turtle import *

# change colors :
colors = ["brown2", "lime", "blue4", "skyblue", "green", "gold"]


def curve():
    for i in range(200):
        right(1)
        forward(1)


bgcolor("black")
pensize(3)
begin_fill()
curve()
speed(0)
delay(0)
ht()

for i in range(200):
    for j in range(len(colors)):
        color(colors[j])
        forward(i)
        curve()
        begin_fill()
        right(91)
    color(colors[i % 6])

    forward(i)
    left(91)
