from turtle import *

# choose a color:
colors = [
    "red",
    "blue",
    "green",
    "yellow",
    "orange",
    "purple",
    "brown",
    "pink",
    "white",
    "black",
    "cyan",
    "lime",
    "skyblue",
    "gold",
    "violet",
    "indigo",
]


bgcolor("black")
pensize(5)
speed(0)
delay(0)
ht()


def curve():
    for i in range(200):
        right(1)
        forward(1)


for i in range(900):

    for k in range(len(colors)):
        curve()
        color(colors[k])
        forward(i)
        right(120)
        curve()
    for j in range(len(colors)):
        color(colors[j])
        forward(i)
        right(91)
    color(colors[i % len(colors)])
    forward(i)
    left(120)
