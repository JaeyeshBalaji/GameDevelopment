import turtle as tr

MOVE_DISTANCE = 20
UP, DOWN, LEFT, RIGHT = 90, 270, 180, 0
POSITION = [(0,0), (-20,0), (-40,0)]

class Snake:

    def __init__(self):
        self.t = []
        for i in POSITION:
            self.add_segment(i)
        self.head = self.t[0]

    def move(self):
        for i in range(len(self.t) - 1, 0, -1):
            self.t[i].goto(self.t[i - 1].xcor(), self.t[i - 1].ycor())
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def add_segment(self, position):
        tur = tr.Turtle(shape="square")
        tur.penup()
        tur.goto(position)
        tur.color("white")
        self.t.append(tur)

    def extend(self):
        self.add_segment(self.t[-1].position())