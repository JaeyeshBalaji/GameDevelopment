import turtle as tr
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

WIDTH, HEIGHT = 1200, 1000

scr = tr.Screen()
scr.setup(width=WIDTH, height=HEIGHT)
scr.bgcolor("Black")
scr.title("PONG GAME")
scr.tracer(0)

paddle_right = Paddle((WIDTH/2)-50,0)
paddle_left = Paddle(-(WIDTH/2)+50, 0)
ball = Ball()
score_board = ScoreBoard()

scr.listen()
scr.onkey(paddle_right.up, "Up")   # Up and Down are case-sensitive
scr.onkey(paddle_right.dowm, "Down")
scr.onkey(paddle_left.up, "w")   # in some computers w key moves paddle only once at a time and not continious it is error with turtle
scr.onkey(paddle_left.dowm, "s")

is_game_on = True
while is_game_on:
    scr.update()
    time.sleep(ball.move_speed)
    ball.move()

    if not((-HEIGHT/2 +20) < ball.ycor() < (HEIGHT/2 -20)):
        ball.wall_bounce()

    if (ball.distance(paddle_right) < 51 and ball.xcor() > (WIDTH/2-80)) or (ball.distance(paddle_left) < 51 and ball.xcor() < (-WIDTH/2+80)) :
        ball.paddle_bounce()

    if (-WIDTH/2+20) > ball.xcor():
        score_board.r_point()
        ball.refresh()

    if ball.xcor() > (WIDTH/2-20):
        score_board.l_point()
        ball.refresh()

