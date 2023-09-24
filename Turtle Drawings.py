#Drawing with the turtles package
import turtle

#set-up
turtle.bgcolor("black") #background color
turtle.pensize(2)
turtle.color("white")
turtle.speed(3)

#square
#turtle.forward(50)
#turtle.left(90)
#turtle.forward(50)
#turtle.left(90)
#turtle.forward(50)
#turtle.left(90)
#turtle.forward(50)
#turtle.left(90)
#turtle.done()

#circles pattern 1
#for colors in ["red", "orange", "yellow", "green", "blue", "purple"]:
    #turtle.color(colors)
    #turtle.circle(150)
    #turtle.left(60)
#turtle.done()

#circles pattern 2
# for i in range(12):
#  for colors in ["red", "orange", "yellow", "green", "blue", "purple"]:
#   turtle.color(colors)
#   turtle.circle(150)
#   turtle.left(5)
# turtle.done()

#spider web
for i in range(10, 200, 30):
    turtle.circle(i)
    turtle.pu()
    turtle.right(90)
    turtle.fd(30)
    turtle.left(90)
    turtle.pd()

for i in range(15):
    turtle.pu()
    turtle.goto(0, 10)
    turtle.left(24)
    turtle.pd()
    turtle.fd(250)


turtle.done()
