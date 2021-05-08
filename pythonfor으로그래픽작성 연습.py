import turtle
import random
t=turtle.Pen()
x=20
y=100
for i in range(1,36):
    t.color(random.random(),random.random(),random.random())
    x+=5
    y+=5
    t.begin_fill()
    t.forward(x)
    t.left(y)
    t.end_fill()

