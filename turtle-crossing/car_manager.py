from turtle import Turtle
from random import randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

cars = []


class CarManager:

    def __init__(self):
        self.cars = []
        self.move_speed = STARTING_MOVE_DISTANCE

    def add_cars(self):
        if not randint(0, 5):
            car = Turtle()
            car.penup()
            car.hideturtle()
            car.goto(300, randint(-240, 240))
            car.shape("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(COLORS[randint(0, 5)])
            car.showturtle()
            self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            new_x = car.xcor() - self.move_speed
            car.goto(new_x, car.ycor())

    def increase_speed(self):
        self.move_speed += MOVE_INCREMENT

    def detect_collision(self, player):
        for car in self.cars:
            if car.ycor() + 20 > player.ycor() > car.ycor() - 20 and car.xcor() + 30 > 0 > car.xcor() - 30:
                return True
