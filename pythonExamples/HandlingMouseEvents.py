import turtle

turtle.screensize(400, 500)
wn = turtle.Screen()
wn.title("Handling mouse clicks")
wn.bgcolor("green")

alex = turtle.Turtle()
alex.color("pink")
tess = turtle.Turtle()
tess.color("Yellow")
tess.forward(40)

def handler_for_tess(x,y):
    wn.title("tess clicked at {0} {1}".format(x, y))
    tess.left(80)
    tess.forward(80)

def handler_for_alex(x,y):
    wn.title("alex clicked at {0} {1}".format(x, y))
    tess.right(70)
    tess.forward(100)

tess.onclick(handler_for_tess)
alex.onclick(handler_for_alex)

wn.mainloop()