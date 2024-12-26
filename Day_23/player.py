import turtle as tr

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
HEIGHT, WIDTH = 1000, 1200


class Player(tr.Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.goto(0, -HEIGHT/2 + 50)
        self.setheading(90)

    def move(self):
        self.forward(10)

    def refresh(self):
        self.goto(0, -HEIGHT/2 + 50)