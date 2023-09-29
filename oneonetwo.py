import turtle as trtl
pen = trtl.Turtle()
X = 0
screen = trtl.Screen()
screen.setup(1.0, 1.0)
trtl.bgcolor("red")
pen.pencolor("blue")
for i in range(200):
  pen.forward(X)
  pen.right(X)
  pen.speed(X)
  X+=1
pen.hideturtle()

wn = trtl.Screen()
wn.mainloop()
