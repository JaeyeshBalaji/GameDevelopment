import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

HEIGHT, WIDTH = 1000, 1200

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.tracer(0)

p = Player()
c = []
s = Scoreboard()

for _ in range(random.randint(int(HEIGHT*0.02), int(HEIGHT*0.03))):
    c.append(CarManager())

screen.listen()
screen.onkey(p.move, "Up")

sp = 0.01
game_is_on = True
while game_is_on:
    time.sleep(sp)
    screen.update()

    for i in c:
        i.move()

    if p.ycor() > HEIGHT/2 -50 :
        p.refresh()
        s.level_up()
        sp *= 0.7

    for j in c:
        if p.distance(j) < 20 :
            s.game_over()
            game_is_on = False

screen.exitonclick()
