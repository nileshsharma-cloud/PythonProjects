import turtle

turtle.screensize(500,600)
wn = turtle.Screen()
wn.title("Using timer")
wn.bgcolor("lightgreen")

alex = turtle.Turtle()
alex.color("red")
alex.pensize(5)

def h1():
    alex.forward(90)
    alex.left(100)
    alex.forward(100)
    wn.ontimer(h1,5)

h1()
wn.mainloop()