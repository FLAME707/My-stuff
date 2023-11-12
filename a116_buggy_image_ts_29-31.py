import turtle as trtl
pen = trtl.Turtle()
wn = trtl.Screen()

#spider head--------
pen.goto(0,-10)
pen.pensize(40)
pen.circle(20)

legs = 4
leglength = 70
angle = 90 / legs
pen.pensize(5)
time = 0

#spider legs--------
pen.setheading(303.75)
while (time < legs):
    pen.goto(0,10)
    pen.left(angle)
    pen.forward(leglength)
    time+=1
time = 0
pen.left(90)
while (time < legs):
    pen.goto(0,10)
    pen.left(angle)
    pen.forward(leglength)
    time+=1
pen.penup()

#eyes
trtl.color("red")
trtl.shape("circle")

pen.goto(15,47)
pen.setheading(320)
pen.pendown()
pen.stamp()
pen.penup()

pen.goto(-15,47)
pen.setheading(220)
pen.pendown()
pen.stamp()
pen.penup()

pen.hideturtle()

wn.mainloop()
