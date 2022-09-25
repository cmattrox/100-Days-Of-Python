import time
from turtle import Screen, up
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
screen.onkey(player.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    # Detect if the player reaches the finish line
    if player.ycor() >= 280:
        player.reset()
        scoreboard.score_point()
        car_manager.speed_up()

    # Detect if a car hits the player
    for car in car_manager.cars:
        if car.distance(player) < 20:
            scoreboard.end_game()
            game_is_on = False

        # If the car has made it to the otherside of the screen remove it from list
        if car.xcor() < -320:
            car_manager.cars.remove(car)

screen.exitonclick()