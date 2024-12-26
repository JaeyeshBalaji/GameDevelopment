import turtle as tr
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
HEIGHT, WIDTH = 1000, 1200


class CarManager(tr.Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(COLORS))
        self.goto(random.randint(int(-WIDTH/2+50), int(WIDTH/2-50)), random.randint(int(-HEIGHT/2+50), int(HEIGHT/2-50)))

    def move(self):
        self.backward(random.random()*5)

        if self.xcor() < -WIDTH/2+50 :
            self.goto(WIDTH / 2 - 50, random.randint(int(-HEIGHT / 2 + 50), int(HEIGHT / 2 - 50)))

