#Drawing with the turtles package
import turtle

#set-up
turtle.bgcolor("black") #background color
turtle.pensize(2)
turtle.color("pink")
turtle.speed(10.5)

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
for i in range(12):
 for colors in ["red", "orange", "yellow", "green", "blue", "purple"]:
  turtle.color(colors)
  turtle.circle(150)
  turtle.left(5)
turtle.done()
