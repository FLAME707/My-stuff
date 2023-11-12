import turtle as trtl
pen = trtl.Turtle()
wn = trtl.Screen()

pen.pensize(40)
pen.circle(20)

w = 6
y = 70
z = 380 / w
pen.pensize(5)

time = 0
while (time < w):
    pen.goto(0,0)
    pen.setheading(z*time)
    pen.forward(y)
    time+=1

pen.hideturtle()

wn.mainloop()
