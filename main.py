import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.tracer(0)
player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()
screen.listen()
screen.onkey(player.move, "Up")
game_is_on = True

while game_is_on:
    car_manager.create_cars()
    car_manager.car_move()

    # collision with wall
    if player.ycor() > 290:
        player.goto(0, -280)
        car_manager.increment_move()
        scoreboard.increment_lvl()
        scoreboard.show()

    # collision with wall
    for car in car_manager.traffic:
        if player.distance(car) < 20:
            player.dot(30, "red")
            game_is_on = False
            scoreboard.game_over()

    time.sleep(0.1)
    screen.update()

screen.exitonclick()
