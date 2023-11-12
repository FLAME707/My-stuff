import turtle as trtl
pen = trtl.Turtle()
wn = trtl.Screen()

#spider head--------
pen.goto(0,-10)
pen.pensize(40)
pen.circle(20)

legs = 8
leglength = 70
angle = 360 / legs
pen.pensize(5)
time = 0

#spider legs--------
while (time < legs):
    pen.goto(0,10)
    pen.setheading(angle*time)
    pen.forward(leglength)
    time+=1

pen.hideturtle()

wn.mainloop()
