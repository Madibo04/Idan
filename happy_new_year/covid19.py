from turtle import *
color('yellow')
bgcolor('black')
speed(10)
hideturtle()
b = 0
while b < 200:
    right(b)
    forward(b * 3)
    b += 1