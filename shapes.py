import turtle
import time

a=turtle.Turtle()
b=turtle.Turtle()
turtle.ht()

a.circle(100) # 100 is radius
a.goto(0,100)
# a.dot(100) # 100 is diameter

b.goto(0,0)
b.goto(100,0)
b.goto(100,100)
b.goto(0,100)
time.sleep(5)