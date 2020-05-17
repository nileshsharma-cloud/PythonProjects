import turtle

wn = turtle.Screen()
alex = turtle.Turtle()
alex.shapesize(5,5,20)
class MyTurtle(turtle.Turtle):
    def glow(self,x,y):
        self.fillcolor("red")
    def unglow(self,x,y):
        self.fillcolor("")

turtle = MyTurtle()
turtle.onclick(turtle.glow)
turtle.onrelease(turtle.unglow)

wn.mainloop()