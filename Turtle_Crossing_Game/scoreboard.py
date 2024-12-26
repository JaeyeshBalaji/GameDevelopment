import turtle as tr

FONT = ("Courier", 30, "bold")
HEIGHT, WIDTH = 1000, 1200


class Scoreboard(tr.Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.goto(-WIDTH/2+30,HEIGHT/2-70)
        self.show()

    def show(self):
        self.clear()
        self.write(f"LEVEL : {self.level}", align="left", font=FONT)

    def level_up(self):
        self.level += 1
        self.show()

    def game_over(self):
        self.home()
        self.write("Game Over", align="center", font=FONT)
