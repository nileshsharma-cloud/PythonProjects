import turtle
wn = turtle.Screen()
wn.title("Nilesh --Turtle Clock Demo")
wn.bgcolor("BlanchedAlmond")

alex = turtle.Turtle()
tex = turtle.Turtle()

for i in range(12):
    tex = turtle.Turtle()
    tex.shape("turtle")
    tex.speed(10)
    tex.color("red")
    tex.penup()
    tex.stamp()
    tex.left(30*i)
    tex.forward(100)

wn.mainloop()