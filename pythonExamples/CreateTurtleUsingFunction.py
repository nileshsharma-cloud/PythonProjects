import turtle


def screen_shape(color, name_of_screen):
    """
    Set up the window screen size and title.
    """

    wn = turtle.Screen()
    wn.bgcolor(color)
    wn.title(name_of_screen)
    return wn


def turtle_shape(color, size):
    """
    Set up the turtle with given shape and size
    """

    alex = turtle.Turtle()
    alex.color(color)
    alex.pensize(size)
    return alex


wn = screen_shape("brown", "Nilesh Demo Screen")
tess = turtle_shape("black", 25)
alex = turtle_shape("white", 30)
wn.mainloop()
