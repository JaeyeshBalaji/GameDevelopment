import turtle as tr
from Snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

# High Score Feature can also be added and it can also be saved in a file

s = tr.Screen()
s.setup(width = 1200, height = 1000)
s.bgcolor("black")
s.title("Snake Game")
s.tracer(0)

snake = Snake()
food = Food()
score_board = ScoreBoard()

s.listen()
s.onkey(snake.up, "Up")
s.onkey(snake.down, "Down")
s.onkey(snake.left, "Left")
s.onkey(snake.right, "Right")

is_game_on = True
while is_game_on:
    s.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        score_board.up_sc()
        snake.extend()

    if not(-580<snake.head.xcor()<580) or not(-480<snake.head.ycor()<480):
        score_board.game_over()
        is_game_on = False

    for seg in snake.t[1:]:
        if snake.head.distance(seg)<10:
            score_board.game_over()
            is_game_on = False

s.exitonclick()