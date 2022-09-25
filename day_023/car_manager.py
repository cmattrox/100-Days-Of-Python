from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

# Once cars get to the end of the screen remove them from self.cars[]

class CarManager():
    def __init__(self):
        self.cars = []
        self.move_distance = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == random.randint(1,6):
            new_car = Turtle("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.goto(300, random.randrange(-240, 270, 30))
            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.backward(self.move_distance)

    def check_collision(self, player):
        for car in self.cars:
            if car.xcor() < -320:
                self.cars.remove(car)


            if car.distance(player) <= 20:
                return True
            else:
                return False

    def speed_up(self):
        self.move_distance += MOVE_INCREMENT