import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)

    car_manager.add_cars()
    car_manager.move_cars()

    if car_manager.detect_collision(player):
        game_is_on = False

    if player.finish_level():
        scoreboard.update_scoreboard()
        car_manager.increase_speed()
        player.reset_position()

    screen.update()

scoreboard.game_over()
screen.exitonclick()
