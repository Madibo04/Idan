from turtle import *
color('blue')
bgcolor('black')
speed(10)
hideturtle()
b = 0
while b < 200:
    right(b)
    forward(b * 3)
    b += 1