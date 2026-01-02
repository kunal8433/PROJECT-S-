from turtle import *

speed(0)
bgcolor("black")
colors = ["red", "yellow", "cyan", "magenta", "lime"]

hideturtle()

for i in range(72):
    color(colors[i % 5])
    circle(120)
    left(5)

done()
