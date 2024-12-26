import random
import turtle as tr

class Food(tr.Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("BLUE")   # case of color text does not matter
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.goto(random.randint(-580,580), random.randint(-480,445))

