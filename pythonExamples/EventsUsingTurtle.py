import turtle

turtle.screensize(400,500)
wn = turtle.Screen()
wn.title("Nilesh's turtle demo")
wn.bgcolor("red")
tess = turtle.Turtle()

def h1():
    tess.forward(60)

def h2():
    tess.left(50)

def h3():
    wn.bye()

wn.onkey(h1, "Up")
wn.onkey(h2,"Down")
wn.onkey(h3,"q")

wn.listen()
wn.mainloop()