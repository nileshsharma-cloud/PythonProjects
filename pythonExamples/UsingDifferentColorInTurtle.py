import turtle
wn = turtle.Screen()
wn.title("Nilesh --Turtle Demo Using Different Color")
wn = turtle.Screen()
wn.bgcolor("Black")

alex = turtle.Turtle()
colour = ['Red', 'yellow', 'orange', 'white']

def draw_multicolor_square(alex,sz):
    for i in colour:
        alex.color(i)
        alex.forward(sz)
        alex.left(90)


alex.pensize(4)

size = 20
for i in range(20):
    draw_multicolor_square(alex,size)
    size = size+4
    alex.speed(15)
    alex.forward(size)
    alex.right(90)

wn.mainloop()