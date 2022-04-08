from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.traffic = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.frequency_car = 51
        self.car_move()
        self.list_trues = 10
        self.car_start = 10
        self.start()

    def create_cars(self, position_x=340):
        traffic = random.randint(1, self.frequency_car)
        if traffic in range(self.list_trues):
            position_y = random.randint(-301, 301)
            car = Turtle()
            car.shape('square')
            car.color(random.choice(COLORS))
            car.penup()
            car.turtlesize(1, 2)
            car.setheading(180)
            car.goto(position_x, position_y)
            self.traffic.append(car)

    def car_move(self):
        for car in self.traffic:
            car.forward(self.car_speed)
            if car.xcor() < -280:
                car.hideturtle()
                self.traffic.remove(car)

    def increment_move(self):
        self.car_speed += MOVE_INCREMENT
        self.list_trues += 2

    def start(self):
        for _ in range(self.car_start):
            self.create_cars(random.randint(230, 300))
