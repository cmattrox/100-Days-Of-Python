import time
from turtle import  Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard 

screen = Screen()
screen.setup(width=1600, height=1200)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((700,0))
l_paddle = Paddle((-700,0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(r_paddle.Up, "Up")
screen.onkey(r_paddle.Down, "Down")
screen.onkey(l_paddle.Up, "w")
screen.onkey(l_paddle.Down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Detect if the ball hits the top wall or bottom wall
    if ball.ycor() >= 580 or ball.ycor() <= -580:
        ball.bounce()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 120 and ball.xcor() > 640 or ball.distance(l_paddle) < 120 and ball.xcor() < -640:
        ball.hit()

    # Detect if the ball goes past the r_paddle
    if ball.xcor() > 760:
        ball.reset_position()
        scoreboard.l_point()

    # Detect if the ball goes past the l_paddle
    if ball.xcor() < -760:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
