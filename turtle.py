import turtle
myturtle=turtle.Turtle()
myturtle.speed(0)

def square(length,angle):
    for i in range (4):
        my_turtle.forward(length)
        my_turtle.right(angle)

for i in range(100):
    square(100, 90)
    myturtle.right(11)