import turtle as tr

WIDTH, HEIGHT = 1200, 1000

class ScoreBoard(tr.Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.l_score = 0
        self.r_score = 0

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, HEIGHT/2 - 50)
        self.write(self.l_score, align="center", font=("Courier", 30, "bold"))
        self.goto(100, HEIGHT/2 - 50)
        self.write(self.r_score, align="center", font=("Courier", 30, "bold"))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()
