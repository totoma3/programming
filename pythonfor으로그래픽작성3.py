import turtle
import random
t=turtle.Pen()
for i in range(1,36):
    a=random.randint(20,50)
    b=random.randint(10,360)
    t.forward(a)
    t.left(b)

