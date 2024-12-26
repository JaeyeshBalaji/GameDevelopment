import turtle as tr

class Ball(tr.Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.xmove = 4
        self.ymove = 4
        self.move_speed = 0.01

    def move(self):
        self.goto(self.xcor()+self.xmove, self.ycor()+self.ymove)

    def wall_bounce(self):
        self.ymove *= -1

    def paddle_bounce(self):
        self.xmove *= -1
        #self.move_speed *= 0.5 # increase speed after each correct bounce with the paddle

    def refresh(self):
        self.home()
        self.paddle_bounce()
        #self.move_speed = 0.01


