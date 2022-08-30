import turtle as t
import random

def initiate(turtle, color, y):
    turtle.pencolor(color)
    turtle.fillcolor(color)
    turtle.penup()
    turtle.shape("turtle")
    turtle.goto(-350, y)

def move_turtle(turtle):
    distance = random.randint(10,50)
    turtle.forward(distance)

screen = t.Screen()
bet = screen.textinput("Bet On A Turtle", "Which turtle do you think is going to win the race? [red/orange/yellow/green/blue/indigo/violet]?:")

red = t.Turtle()
initiate(red, "red", -150)
orange = t.Turtle()
initiate(orange, "orange", -100)
yellow = t.Turtle()
initiate(yellow, "yellow", -50)
green = t.Turtle()
initiate(green, "green", 0)
blue = t.Turtle()
initiate(blue, "blue", 50)
indigo = t.Turtle()
initiate(indigo, "indigo", 100)
violet = t.Turtle()
initiate(violet, "violet", 150)

game_over = False

while game_over != True:
    move_turtle(red)
    move_turtle(orange)
    move_turtle(yellow)
    move_turtle(green)  
    move_turtle(blue)
    move_turtle(indigo)
    move_turtle(violet)

    if (red.xcor() >= 300):
        game_over = True
        winner = "red"
    elif (orange.xcor() >= 300):
        game_over = True
        winner = "orange"
    elif (yellow.xcor() >= 300):
        game_over = True
        winner = "yellow"
    elif (green.xcor() >= 300):
        game_over = True    
        winner = "green"
    elif (blue.xcor() >= 300):
        game_over = True
        winner = "blue"
    elif (indigo.xcor() >= 300):
        game_over = True
        winner = "indigo"
    elif (violet.xcor() >= 300):
        game_over = True
        winner = "violet"

if bet == winner:
    print(f"You were right! The {winner} turtle was the winner.")
else:
    print(f"You were wrong. The {winner} turtle was the winner.")

screen.exitonclick()