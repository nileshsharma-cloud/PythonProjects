import turtle


def screen_shape(color, name_of_screen):
    """
    Set up the window screen size and title.
    """

    wn = turtle.Screen()
    wn.bgcolor(color)
    wn.title(name_of_screen)
    return wn


def turtle_shape(color):
    """
    Set up the turtle with given shape and size
    """

    alex = turtle.Turtle()
    alex.color(color)
    return alex


def main_function(c):
    for i in range(4):
        alex.forward(50+c)
        alex.left(90+c)


size = 0

wn = screen_shape("white", "Nilesh Demo")
alex = turtle_shape("red")
for c in range(5):


    main_function(size)
    size = size+20

wn.mainloop()
