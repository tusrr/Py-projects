import turtle
import time
# turtle.ht()
turtle.title("Tusrr")
t1=turtle.Turtle()
t2=turtle.Turtle()
# t1.pencolor("Yellow")
# t1.shape("classic")
# t1.shape("circle/triangle/arrow/classic")

# t1.shapesize(10,14,13)

t2.pencolor("yellow")
t2.shape("turtle")
t2.shapesize(7,7,5)  

for angle in range(0,901,45):
    t2.lt(angle)
    if (angle%10==0):
        t2.lt(angle)
        t2.pencolor("red")
        t2.fillcolor("cyan")
    else:
        t2.lt(angle)
        t2.pencolor("yellow")
        t2.fillcolor("grey")


time.sleep(1)
