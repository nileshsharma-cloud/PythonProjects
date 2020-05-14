import turtle
wn = turtle.Screen()
wn.title("Nilesh First demo Screen")
wn.bgcolor("lightgreen")
wn.getshapes()

alex = turtle.Turtle()
alex.shape("turtle")
for x in range(6):
    alex.forward(60)
    alex.left(100)


size = 20
for c in range(30):
    alex.speed(5)
    alex.stamp()
    size = size + 3
    alex.forward(size)
    alex.right(100)

wn.mainloop()