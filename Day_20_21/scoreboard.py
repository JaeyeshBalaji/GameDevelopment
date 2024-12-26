import turtle as tr

class ScoreBoard(tr.Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0, 450)
        self.penup()
        self.color("white")
        self.hideturtle()
        self.write(f"Score : {self.score}", align="center", font=("Courier", 25, "bold")) # Here bold is case-sensitive

    def up_sc(self):
        self.clear()
        self.score += 1
        self.write(f"Score : {self.score}", align="center", font=("Courier", 25, "bold")) # Here bold is case-sensitive

    def game_over(self):
        self.home()
        self.write("Game Over", align="center", font=("Courier", 25, "bold")) # Here bold is case-sensitive


