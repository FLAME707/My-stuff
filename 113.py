import turtle as trtl
pen = trtl.Turtle()
wn = trtl.Screen()
pen.hideturtle()
pen.pensize(30)
pen.pencolor("green")
wn.bgcolor("black")
#flower
pen.penup()
pen.home()
pen.setheading(270)
pen.pendown()
pen.forward(200)
pen.left(180)
pen.forward(100)
pen.left(90)
pen.forward(20)
pen.right(180)
pen.forward(20)
pen.left(90)
pen.forward(50)
pen.right(90)
pen.forward(20)
pen.left(180)
pen.forward(20)
pen.right(90)
pen.forward(50)
pen.penup()
pen.shape("circle")
pen.turtlesize(3)
pen.color("red")
pen.setheading(198)
for i in range(10):
    pen.right(36)
    pen.forward(50)
    pen.stamp()
pen.turtlesize(2)
pen.color("orange")
pen.setheading(90)
pen.forward(32.5)
pen.setheading(198)
for i in range(10):
    pen.right(36)
    pen.forward(30)
    pen.stamp()
pen.setheading(90)
pen.forward(48.75)
pen.pensize(5)
pen.setheading(0)
pen.pendown()
pen.speed(100)
for i in range(10):
    pen.pencolor("black")
    pen.forward(30)
    pen.right(180)
    pen.forward(60)
    pen.right(180)
    pen.forward(30)
    pen.right(137.5)
    pen.pencolor("yellow")
    pen.forward(30)
    pen.right(180)
    pen.forward(60)
    pen.right(180)
    pen.forward(30)
    pen.right(137.5)
wn.mainloop()