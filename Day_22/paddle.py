import turtle as tr

class Paddle(tr.Turtle):

    def __init__(self, xpos, ypos):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.setheading(90)   # Instead of this we could aswell have used goto in up and down functions
        self.goto(xpos, ypos)

    def up(self):
        self.forward(20)

    def dowm(self):
        self.backward(20)